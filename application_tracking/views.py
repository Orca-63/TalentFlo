from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponseForbidden
from django.core.paginator import Paginator
from accounts.models import User
from application_tracking.enums import ApplicationStatus
from .forms import JobAdvertForm, JobApplicationForm
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import JobAdvert, JobApplication
from common.tasks import send_email
from application_tracking.enums import ApplicationStatus

@login_required
def create_advert(request: HttpRequest):
    form = JobAdvertForm(request.POST or None)

    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.created_by = request.user
        instance.save()

        messages.success(
            request, "Advert created. You can now receive applications.")
        return redirect(instance.get_absolute_url())

    context = {
        "job_advert_form": form,
        "title": "Create a new advert",
        "btn_text": "Create advert"
    }

    return render(request, "create_advert.html", context)


def list_adverts(request: HttpRequest):

    active_jobs = JobAdvert.objects.filter(
        is_published=True, deadline__gte=timezone.datetime.now().date())

    paginator = Paginator(active_jobs, 10)
    requested_page = request.GET.get("page")
    paginated_adverts = paginator.get_page(requested_page)

    context = {
        "job_adverts": paginated_adverts
    }
    return render(request, "home.html", context)


def get_advert(request: HttpRequest, advert_id):
    form = JobApplicationForm()

    job_advert = get_object_or_404(JobAdvert, pk=advert_id)
    context = {
        "job_advert": job_advert,
        "application_form": form,
    }
    return render(request, "advert.html", context)


def apply(request: HttpRequest, advert_id):
    advert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.method == "POST":
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():

            email = form.cleaned_data["email"]
            if advert.applications.filter(email__iexact=email).exists():
                messages.error(
                    request, "You have already applied for this position")
                return redirect("job_advert", advert_id=advert_id)

            application: JobApplication = form.save(commit=False)
            application.job_advert = advert
            application.save()
            messages.success(request, "Application submitted successfully.")
            return redirect("job_advert", advert_id=advert_id)

    else:
        form = JobApplicationForm()

    context = {
        "job_advert": advert,
        "application_form": form
    }
    return render(request, "advert.html", context)


@login_required
def my_applications(request: HttpRequest):
    user: User = request.user
    email = user.email
    applications = JobApplication.objects.filter(email=user.email)
    paginator = Paginator(applications, 10)
    requested_page = request.GET.get("page")
    paginated_applications = paginator.get_page(requested_page)
    context = {
        "my_applications": paginated_applications
    }
    return render(request, "my_applications.html", context)


def my_jobs(request: HttpRequest):
    user: User = request.user
    jobs = JobAdvert.objects.all()
    paginator = Paginator(jobs, 10)
    requested_page = request.GET.get("page")
    paginated_jobs = paginator.get_page(requested_page)

    context = {
        "my_jobs": paginated_jobs,
        "current_date": timezone.now().date()
    }

    return render(request, "my_jobs.html",  context)


def update_advert(request: HttpRequest, advert_id):
    user: User = request.user
    advert: JobAdvert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.user != advert.created_by:
        return HttpResponseForbidden("You can only update an advert created by you.")
    form = JobAdvertForm(request.POST or None, instance=advert)
    if form.is_valid():
        instance: JobAdvert = form.save(commit=False)
        instance.save()
        messages.success(request, "Advert updated successfully.")
        return redirect(instance.get_absolute_url())

    context = {
        "job_advert_form": form,
        "btn_text": "Update advert"
    }
    return render(request, "create_advert.html", context)


@login_required
def delete_advert(request: HttpRequest, advert_id):
    advert: JobAdvert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.user != advert.created_by:
        return HttpResponseForbidden("You can only delete an advert created by you.")

    advert.delete()
    messages.success(request, "Advert deleted successfully.")
    return redirect("my_jobs")


@login_required
def advert_applications(request: HttpRequest, advert_id):
    advert: JobAdvert = get_object_or_404(JobAdvert, pk=advert_id)
    if request.user != advert.created_by:
        return HttpResponseForbidden("You can only see applications for an advert created by you.")

    applications = advert.applications.all()
    paginator = Paginator(applications, 10)
    requested_page = request.GET.get("page")
    paginated_applications = paginator.get_page(requested_page)

    context = {
        "applications": paginated_applications,
        "advert": advert
    }
    return render(request, "advert_applications.html", context)

@login_required
def decide(request: HttpRequest, job_application_id):
    job_application:JobApplication = get_object_or_404(JobApplication, pk = job_application_id)
    if(request.user != job_application.job_advert.created_by):
        return HttpResponseForbidden("You cannot make verdict on this application")
    
    if request.method == "POST":
        status = request.POST.get("status")
        job_application.status = status
        job_application.save(update_fields=["status"])
        messages.success(request, f"Application status updated to {status}")

    if status == ApplicationStatus.REJECTED:
            context = {
                "applicant_name":job_application.name,
                "job_title":job_application.job_advert.title,
                "company_name":job_application.job_advert.company_name,
            }
            send_email.delay(
                f'Application Outcome for {job_application.job_advert.title}',
                [job_application.email],
                "emails/job_application_update.html",
                context
            )
    return redirect("advert_applications", advert_id = job_application.job_advert.id)        

def search(request: HttpRequest):
    keyword = request.GET.get("keyword")
    location = request.GET.get("location")
    result = JobAdvert.objects.search(keyword, location)
    paginator = Paginator(result, 10)
    requested_page = request.GET.get("page")
    paginated_adverts = paginator.get_page(requested_page)

    context = {
        "job_adverts": paginated_adverts
    }
    return render(request, "home.html", context)

