#  TalentFlo 💻
**Campus Recruitment Automation Platform**

## 📖 Overview

TalentFlo is a comprehensive Django-based web platform designed to revolutionize campus recruitment processes through intelligent automation. Built with scalability and efficiency in mind, the platform streamlines the entire recruitment workflow from job posting to candidate selection, ensuring seamless communication between recruiters, students, and administrators.

### 🎯 Key Objectives
- **Automate repetitive recruitment tasks** to reduce manual workload
- **Enhance communication** through real-time notifications and updates
- **Provide comprehensive tracking** of recruitment processes
- **Ensure reliable task execution** with robust background processing

## 📸 Screenshots

### 🏠 Homepage & Job Search

*Clean and intuitive job search interface with filtering capabilities*
<img width="1911" height="899" alt="Screenshot 2025-07-24 221934" src="https://github.com/user-attachments/assets/682ec989-7a21-4e67-973d-223b75062519" />

### 💼 Job Listings

*Browse available positions with detailed information cards*
<img width="1919" height="906" alt="Screenshot 2025-06-14 235549" src="https://github.com/user-attachments/assets/9ab262b6-8ae6-4a90-96ad-4e1d8e9ec256" />

### 📊 Admin Dashboard

*Comprehensive job management with application tracking*
<img width="1906" height="912" alt="Screenshot 2025-07-24 215017" src="https://github.com/user-attachments/assets/28636bb5-c17f-44b5-b318-c77f9e014791" />



### 📝 Application Process

*Streamlined application form with file upload support*

<img width="1907" height="908" alt="Screenshot 2025-07-24 215119" src="https://github.com/user-attachments/assets/8b4b174e-a345-45e2-b10a-de7004581b00" />

### 👥 Applicant Management
<img width="1909" height="783" alt="Screenshot 2025-07-24 215503" src="https://github.com/user-attachments/assets/3bce880e-4feb-4ddb-9183-1028916854fc" />

*Review and manage applications with decision workflows*

## ✨ Features

### 🏢 For Recruiters & Administrators
- **Job Management**: Create, edit, and manage job postings with detailed requirements
- **Application Tracking**: Monitor application status and candidate progress in real-time
- **Automated Workflows**: Streamline recruitment processes with intelligent automation
- **Analytics Dashboard**: Gain insights into recruitment metrics and performance
- **Bulk Operations**: Perform mass actions on applications and communications

### 🎓 For Students
- **Job Discovery**: Browse and search through available job opportunities
- **One-Click Applications**: Simple and intuitive application process
- **Real-time Updates**: Receive instant email notifications about application status
- **Application History**: Track all submitted applications and their progress

### 🔧 System Features
- **Asynchronous Processing**: Handle high-volume operations without blocking the main application
- **Real-time Monitoring**: Track background tasks and system performance
- **Reliable Email Delivery**: Ensure critical notifications reach recipients



### Component Breakdown

#### 🌐 Django Web Framework
- **Role**: Main application server and user interface
- **Responsibilities**: 
  - Handle HTTP requests and responses
  - Manage user authentication and authorization
  - Render templates and serve static content
 

#### ⚡ Celery Task Queue
- **Role**: Asynchronous task processor
- **Responsibilities**:
  - Process email notifications in the background
  - Handle bulk operations without blocking UI
  - Execute scheduled tasks and periodic jobs
 

#### 🔄 Redis Message Broker
- **Role**: Message queue and caching layer
- **Responsibilities**:
  - Queue tasks for Celery workers
  - Cache frequently accessed data
  - Handle session storage for improved performance
  - Provide pub/sub messaging capabilities

#### 🌸 Flower Monitoring
- **Role**: Real-time task monitoring and management
- **Responsibilities**:
  - Monitor active, failed, and completed tasks
  - Provide web-based dashboard for task inspection
  - Enable task management and debugging
  - Track worker performance and health

## 🛠️ Technology Stack

| Layer | Technology | Version | Purpose |
|-------|------------|---------|---------|
| **Backend Framework** | Django | 4.x+ | Web application framework |
| **Task Queue** | Celery | 5.x+ | Asynchronous task processing |
| **Message Broker** | Redis | 7.x+ | Task queuing and caching |
| **Task Monitoring** | Flower | 1.x+ | Real-time task monitoring |
| **Email Service** | Brevo | API v3 | Transactional email delivery |
| **Containerization** | Docker | 20.x+ | Service containerization |
| **Frontend** | HTML/CSS/JS | - | User interface |
| **Database** | SQLite | - | Data persistence |

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- Docker Desktop

### 📥 Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/Orca-63/TalentFlo.git
cd Recruitment Platform
```

#### 2. Set Up Python Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
# Install from requirements.txt file 
pip install -r requirements.txt
```

#### 4. Environment Configuration
Create a `.env` file in the project root


### 🐳 Service Setup

#### 1. Start Redis Server
```bash
# Using Docker (Recommended)
docker run -d -p 6379:6379 redis
```

#### 2. Database Setup
```bash
# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser
```

### 🏃‍♂️ Running the Application

You'll need to run multiple processes for full functionality. Open separate terminal windows for each:

#### Terminal 1: Django Development Server
```bash
python manage.py runserver
```
Access the application at: `http://localhost:8000`

#### Terminal 2: Celery Worker
```bash
celery -A RecruitmentPlatform worker --pool=solo --loglevel=info
```

#### Terminal 3: Flower Monitoring Dashboard
```bash
celery -A RecruitmentPlatform flower
```
Access Flower dashboard at: `http://localhost:5555`


## 📊 Usage Guide

### 🔐 Admin Access
1. Navigate to `http://localhost:8000/admin`
2. Login with your superuser credentials
3. Manage users, job postings, and applications

### 👥 User Workflows

#### For Recruiters:
1. **Create Job Postings**: Add new opportunities with detailed requirements
2. **Review Applications**: Evaluate submitted applications
3. **Send Notifications**: Automated emails for status updates
4. **Track Progress**: Monitor recruitment pipeline

#### For Students:
1. **Browse Jobs**: View available opportunities
2. **Submit Applications**: Apply with required documents
3. **Track Status**: Monitor application progress
4. **Receive Updates**: Get notified of status changes


## 📈 Monitoring & Debugging

### Flower Dashboard Features
- **Task Overview**: Monitor all task types and their status
- **Worker Management**: View active workers and their health
- **Task Details**: Inspect individual task execution
- **Performance Metrics**: Track throughput and response times


## 🤝 Contributing

We welcome contributions to TalentFlo! Here's how you can help:

### 📋 Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with appropriate tests
4. Commit your changes: `git commit -m "Add feature description"`
5. Push to your branch: `git push origin feature-name`
6. Submit a pull request


---

**Built with 💜 for streamlined campus recruitment**
