# Job Interview Scheduler

The **Job Interview Scheduler** is a backend-centric project built using Django. It helps HRs and recruiters efficiently manage the interview scheduling process, track applicants, and assign interview slots to them. 

## Features

### 1. **Applicant Management**
   - **CRUD Operations**: Add, update, view, and delete applicants.

### 2. **Interview Slot Management**
   - **Create/Update/Delete Interview Slots**: Manage available slots for interviews.
   - **Slot Assignment**: Assign interview slots to applicants based on availability.


### 4. **Status Updates**
   - Track the status of applicants (e.g., Pending, Interview Scheduled, Interview Completed).
   - Easy filtering of applicants by their current status.

### 5. **Admin Interface**
   - The built-in Django admin interface allows easy management of applicants, interview slots, and assignments.
   - Provides an intuitive interface for HRs and recruiters.

## Technologies Used

- **Backend**: Django (Python)
- **Admin Interface**: Django Admin
- **CSS**: Tailwind CSS 

## Setup Instructions

Follow the steps below to set up and run the Job Interview Scheduler locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/job-interview-scheduler.git
cd job-interview-scheduler
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **On macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

- **On Windows**:
  ```bash
  .\venv\Scripts\activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up the Database

Run the following commands to apply the migrations and set up the database:

```bash
python manage.py migrate
```



### 5. Run the Development Server

Start the server with:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.


---
