# HealthCare Project

A Django RESTful API backend for managing patients, doctors, and their mappings in a healthcare system.

## Live Deployment

The API is live at:  
**[https://health-care-rohan.vercel.app/](https://health-care-rohan.vercel.app/)**  

## Features

- Patient CRUD (Create, Read, Update, Delete)
- Doctor CRUD
- Patient-Doctor mapping management
- JWT authentication
- CORS support for frontend integration
- PostgreSQL database support

## Project Structure

```
HospitalBackend/
├── healthcare/
│   ├── account/
│   ├── api/
│   ├── HealthCare/
│   └── manage.py
├── .env
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository

```sh
git clone <repository-url>
cd HospitalBackend
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
venv\Scripts\activate   # On Windows
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your-django-secret-key
DEBUG=True
DATABASE_URL=postgres://username:password@localhost:5432/healthcare
```

### 5. Apply migrations

```sh
python manage.py migrate
```

### 6. Create a superuser (optional)

```sh
python manage.py createsuperuser
```

### 7. Run the development server

```sh
python manage.py runserver
```

## API Endpoints

- `/api/patient/` - List & create patients
- `/api/patient/<int:pk>` - Retrieve, update, delete patient
- `/api/doctors/` - List & create doctors
- `/api/doctors/<int:pk>/` - Retrieve, update, delete doctor
- `/api/mappings/` - List & create patient-doctor mappings
- `/api/mappings/patient/<int:patient_id>/` - Get mappings by patient
- `/api/mapping/<int:pk>/` - Delete a specific mapping

## Environment Variables

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `True` for development
- `DATABASE_URL`: PostgreSQL connection string

## License

This project is for educational purposes.
