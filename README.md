# ITD Martial Arts Academy Management System

A premium, modern Django-based web application designed to manage a Karate Academy. The system streamlines student registrations, fee packages, pending fees, batch allocations, attendance, belt graduation progression, and generates printable/thermal invoices with Parent WhatsApp notification support.

---

## 🌟 Features

- **🥋 Student Management**: Add, edit, and track students with belt ranks (white to black), parent contact info, status, and join dates.
- **📅 Batch & Package Control**: Group students into batches, schedule classes, and link them to flexible fee packages.
- **💰 Fee Tracking & Renewals**: Monitor active memberships, pending fees, and record new payments.
- **📄 Printable Thermal/Standard Invoices**: Instantly generate clean, printable receipts optimized for both standard A4 and 58mm/80mm thermal printers.
- **💬 WhatsApp Notification Hints**: Get rapid WhatsApp template shortcuts to notify parents about fee updates.
- **🐳 Containerized Setup**: Pre-configured Docker & Docker Compose setup for consistent local development and deployment.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django 4.2
- **Database**: PostgreSQL (Production) / SQLite (Development)
- **WSGI Server**: Gunicorn
- **Styling**: Modern, responsive CSS with interactive components
- **Containerization**: Docker, Docker Compose

---

## 🚀 Getting Started

### Method 1: Running with Docker Compose (Recommended)

Make sure you have [Docker](https://www.docker.com/) installed on your machine.

1. **Configure Environment Variables**:
   Create a `.env` file at the root level (copied from `.env.example` or configured with your secret keys).
   
2. **Build and Run the Containers**:
   ```bash
   docker-compose up --build
   ```

3. **Access the Application**:
   Open [http://localhost:8000](http://localhost:8000) in your browser.

---

### Method 2: Running Locally with Python Virtual Environment

1. **Clone & Navigate to Backend**:
   ```bash
   cd backend
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # Linux/macOS:
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to view the app.

---

## 📂 Directory Structure

```text
itd-martial-arts-academy/
├── backend/                  # Django backend application
│   ├── karate_backend/       # Django core configuration (settings, URLs, WSGI)
│   ├── students/             # Main app containing models, views, templates, forms
│   ├── static/               # CSS, JS, and image assets
│   ├── Dockerfile            # Backend Docker instructions
│   └── manage.py             # Django entry point script
├── docker-compose.yml        # Docker orchestration file
├── .dockerignore             # List of files ignored by Docker
├── .env                      # Local environment configuration file
└── README.md                 # Project documentation
```

---

## 📝 License
This project is proprietary and confidential. All rights reserved.
