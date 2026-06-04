# Quick Hire

## Overview

Quick Hire is a Python-based Recruitment Management System developed using the Tkinter GUI framework and MySQL database. The application is designed to help Human Resource (HR) departments efficiently manage applicant records, recruitment information, job postings, and user accounts through a simple graphical interface.

The system centralizes recruitment-related data, reduces manual paperwork, and provides quick access to applicant and job information.

---

## Features

* Applicant registration and management
* Job posting and management
* HR and Admin account management
* Secure text-based login system
* Password change functionality
* Recruitment data storage and retrieval
* PDF report generation
* Printing and exporting records
* User-friendly graphical interface

---

## Technologies Used

* Python
* Tkinter
* MySQL
* mysql-connector-python
* ReportLab / FPDF
* Pillow (PIL)

---

## Project Structure

### Main Application Files

| File Name          | Description                                       |
| ------------------ | ------------------------------------------------- |
| QuickHire.py       | Main entry point of the application               |
| Homepage.py        | Main dashboard/home screen                        |
| Applicant.py       | Applicant registration and management             |
| Addjobs.py         | Add and manage job vacancies                      |
| JobData.py         | Display and manage job records                    |
| RecruitmentData.py | Display recruitment information                   |
| UserData.py        | Display registered user information               |
| CreateAdmin.py     | Create administrator accounts                     |
| CreateUser.py      | Create HR/user accounts                           |
| LoginText.py       | User authentication through username and password |
| ChangePassword.py  | Password update functionality                     |
| details.py         | Display detailed applicant information            |
| PrintData.py       | Generate printable reports                        |

---

## Database

The project uses a MySQL database.

Database schema file:

* quick_hire.sql

This file contains all tables and database structures required by the application.

---

## Generated Reports

The application can generate the following reports:

* JobData.pdf
* RecruitmentData.pdf
* UserData.pdf

These reports help HR staff maintain and share recruitment records efficiently.



## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/quick-hire.git
cd quick-hire
```

### Install Required Packages

```bash
pip install mysql-connector-python
pip install pillow
pip install reportlab
```

### Configure Database

Create a MySQL database and import the SQL file:

```sql
CREATE DATABASE quick_hire;
```

Import the schema:

```bash
mysql -u root -p quick_hire < quick_hire.sql
```

### Run the Application

```bash
python QuickHire.py
```

---

## Modules

### Authentication Module

* User login
* Password management

### Job Management Module

* Add new job vacancies
* View available jobs
* Maintain job records

### Applicant Management Module

* Register applicants
* Store applicant information
* Track recruitment records

### User Management Module

* Create admin accounts
* Create HR accounts
* Manage users

### Reporting Module

* Generate PDF reports
* Print recruitment records
* Export data

---

## Future Enhancements

* Resume upload functionality
* Interview scheduling system
* Email notifications
* Candidate skill-based ranking
* Cloud database integration
* Web-based deployment

---

## Screenshots

Add screenshots of:

1. Login Window
   <img width="747" height="533" alt="Screenshot 2025-12-09 201608" src="https://github.com/user-attachments/assets/dc6fbde0-fd6e-4a6e-b3a5-94f29fa988d7" />
2. Homepage Dashboard
   <img width="1919" height="1018" alt="Screenshot 2025-12-09 155033" src="https://github.com/user-attachments/assets/88d0275a-277d-4881-85db-519172569f37" />
3. Applicant Registration Form
   <img width="1920" height="1080" alt="Screenshot 2025-12-09 165953" src="https://github.com/user-attachments/assets/93de3bca-667b-454a-a232-ddf2f06d621d" />
4. Job Management Window
   <img width="1297" height="854" alt="Screenshot 2025-12-09 170723" src="https://github.com/user-attachments/assets/8a545c06-d1b9-422e-84a6-7906f531450f" />
5. Recruitment Data Window
   <img width="1617" height="865" alt="Screenshot 2025-12-09 171123" src="https://github.com/user-attachments/assets/687f289c-1fdf-44e4-892f-3e4b59bdce08" />
6. Generated Reports
   <img width="1762" height="919" alt="Screenshot 2025-12-09 201925" src="https://github.com/user-attachments/assets/761ea61b-5108-4485-b093-af258751c177" />


---

## Authors

Developed as an academic project to simplify recruitment and applicant data management for HR departments using Python and MySQL.

---

## License

This project is developed for educational and learning purposes.
