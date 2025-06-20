# 💻 TalentFlo

A web-based recruitment platform built using Django to streamline campus hiring processes.


## 🚀 Features

- 🧑‍🎓 Students can view and apply to job postings
- 📬 Asynchronous email notifications using Celery
- ⚙️ Redis as a message broker for background task handling
- 📈 Real-time task monitoring with Flower
- ✉️ Transactional emails sent via Brevo 
- 🐳 Docker used to containerize Redis for seamless integration

---

## 🛠 Tech Stack

| Layer             | Technology        |
|------------------|-------------------|
| Backend          | Django             |
| Task Queue       | Celery             |
| Message Broker   | Redis              |
| Monitoring       | Flower             |
| Email Service    | Brevo              |
| Containerization | Docker             |

---

##  How to Run the Project Locally

###  1. Clone the repository
git clone https://github.com/Orca-63/TalentFlo

cd RecruitmentPlatform 

###  2. Create and activate a virtual environment
python -m venv venv

venv\Scripts\activate

###  3. Create and activate a virtual environment
pip install django

pip install celery

pip install redis

pip install flower

### 4. Start Redis server via Docker
docker run -p 6379:6379 redis

### 5. Start the Celery worker
celery -A RecruitmentPlatform worker --pool=solo --loglevel=info

### 6. Start the Flower monitoring dashboard
celery -A RecruitmentPlatform flower

### 7. Run the Django development server
python manage.py runserver



