# NGO CMS – Login & User Authentication Module

This module is a **secure login and registration system** built for the **NGO Content Management System (NGO-CMS)** project.  
It provides role-based access control, session management, password reset, and secure authentication for both **admins** and **users**.

---

## 🚀 Features

- **User Registration** (optional for multiple roles)
  - Registration form for new users (Admin can also add users)
  - Fields: Name, Email, Password, Role
  - Email verification for added security

- **Admin / User Login**
  - Secure login using email and password
  - Authentication checks for credentials
  - Redirect to dashboard on successful login

- **Forgot Password / Reset Password**
  - Password reset link via email
  - Secure token-based reset system

- **Session Management**
  - Auto logout after inactivity
  - Persistent login session tracking

- **Role-Based Access Control**
  - Admins can access all features
  - Other users have restricted access

- **Logout Functionality**
  - Secure logout to prevent unauthorized access

---

## 🧱 Tech Stack

- **Backend Framework:** Django 5.0+  
- **Database:** MySQL  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Authentication:** Django’s built-in auth system  
- **Deployment:** PythonAnywhere  

---

## ⚙️ Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/unknownperson35/ngo-cms-login-module.git
cd ngo-cms-login-module
"# ngo-cms-login-module-v2" 
