# Employee Management System
 ## Overview
   The Employee Management System (EMS) is a Django-based application designed to efficiently manage employee information. It provides functionality for creating, 
   reading, updating, and deleting employee records, along with email verification through Gmail and pagination for better data handling.

 ## Features
 * Create: Add new employee records.
 * Read: View details and list employee records.
 * Update: Modify existing employee information.
 * Delete: Remove employee records.
 * Email Verification: Verify employee email addresses using Gmail.
 * Pagination: Manage and navigate employee records in a paginated view.

 ## Prerequisites
  Ensure you have the following installed:
 * Python (version 3.8 or higher)
 * Django (version 5.0.4)
 * A Gmail account for email verification
 * MySQL Database

 ## Installation
 #### 1. Clone the Repository:
    git clone https://github.com/Shirodkar-Shubham-GitHub/Employee_Management_System
    cd EMS
 #### 2. Create a Virtual Environment:
    python -m venv my_env
    my_env\Scripts\activate
 #### 3. Install Dependencies:
    pip install -r requirements.txt
 #### Configure Email Verification:
 * Create a .env file in the root directory of the project.
 * Add the following environment variables:
   
       EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
       EMAIL_HOST=smtp.gmail.com
       EMAIL_PORT=587
       EMAIL_USE_TLS=True
       EMAIL_HOST_USER=your-email@gmail.com
       EMAIL_HOST_PASSWORD=your-email-password
 #### 4. Apply Migrations:
    python manage.py migrate
 #### 5. Create a Superuser (for admin access):
    python manage.py createsuperuser
 #### 6. Run the Development Server:
    python manage.py runserver
    
 ## Usage
 #### 1. Access the Application:
   Open your web browser and go to http://localhost:8000.
 #### 2. Admin Interface:
   Access the Django admin interface at http://localhost:8000/admin to manage employee records and perform other administrative tasks.
 ## Configuration
 * Database Configuration:
   Update settings.py with your database configuration if not using the default SQLite.
 * Email Verification Settings:
   Ensure your .env file has the correct Gmail credentials and settings for email verification.
 ## Contributing
   Contributions are welcome! To contribute:

    1. Fork the repository.
    2. Create a new branch for your feature or fix.
    3. Submit a pull request with a description of your changes.
 ## License
   This project is licensed under the MIT License. See the LICENSE file for details.
