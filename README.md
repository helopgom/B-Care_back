# 👵🏻🔁📱 B-Care

## Table of Contents
- [📄 Project Description](#-project-description)
- [🎯 Motivation](#-motivation)
- [🚀 Features](#-features)
- [📅 Project Management](#-project-management)
- [📖 Documentation](#-documentation)
- [🛠 Technologies Used](#-technologies-used)
- [📦 Installation and Configuration](#-installation-and-configuration)
- [🧪 Testing](#-testing)
- [🤝 Contributions](#-contributions)
- [📧 Contact](#-contact)



## 📄 Project Description

**B-Care** is an application that offers conversational accompaniment through an AI engine. The user can talk about their topics of interest, and the AI will respond consistently, adapting to their preferences. 
Through the use of voice recognition, the conversation will be fluid, helping the user to interact in a natural and personalized way with the AI.

## 🎯 Motivation

The motivation for this project stems from the idea of combating loneliness in the elderly, a common problem in today's world. 
## 🚀 Features

### B-Care Users (CRUD Operations)
- **Create**: Register new users in the application
- **Read**: View your data
- **Update**: The user can update data such as their name, by which the application calls them, phone and date of birth.
- **Create**: Add new preferences
- **Delete**: Remove preferences.
- **Read**: View your preferences
- **Update**: The user can update the preferences he/she wants to talk about.

### Conversational engine
- It will interact with the user and, according to his/her preferences and name, will be able to maintain a conversation in simple, slow and short sentences.

## 📅 Project Management
This project was developed by a one developer using SCRUM. Tools like Jira were used for backlog management and sprint planning.


## 📖 Documentation
- **[Algorithm Flowchart](https://drive.google.com/file/d/1jB3S765Ge6C98ey6-QgNvy2_osvMjR_a/view?usp=drive_link)**: Flowchart and workflow illustrating the main algorithms applied in the project as well as the user experience in the application. 
- **[Data Model](https://drive.google.com/file/d/1Wjx8SIKT4ws3qU3Ge7bLQhsrQEziQmO1/view?usp=drive_link)**: A diagram showing the key entities of the system and their relationships, available on Drawio.

## 🛠 Technologies Used

- **Language**: Python (v3.12.4) 
- **Database**: PostgreSQL (v16.2) 
- **Testing**: Pytest, Unittest (integrated with Python)
- **Version Control**: Git (v2.45.2) with GitFlow
- **IDE**: Pycharm
- **Django**
- **Django REST Framework**
- **Psycopg2-binary** 
- **Drawio**

Language: Python (v3.12.4)
Database: PostgreSQL (v16.2)
Testing: Jest (v29.7)
Version Control: Git (v2.45.2) with GitFlow
Agile Methodologies: SCRUM
IDE: Visual Studio Code
Frameworks: React, Django
Design Tool: Figma

## 📦 Installation and Configuration

1. **Clone the repository:**
   ```bash
   git clone
   https://github.com/helopgom/B-Care_back.git
   ```
2. **Create and activate your virtual enviroment:**
    ```bash
    cd B-Care_back
    python -m venv env
    source env/bin/activate  # En Windows usa: env\Scripts\activate
    ```
    
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure the database:**
 Create a database in PostgreSQL with same name the proyect. Add to settings.py:
   ```bash
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': 'nameBBDD',
           'USER': 'your BBDD user',
           'PASSWORD': 'your BBDD password',
           'HOST': 'localhost', #(usually is the same)
           'PORT': '5432' #(usually is the same)
       }
   } 
      ```
5. **Perform the migrations and run server:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
    ```
   
## 🧪 Testing

- **Run integration tests:**

    ```bash
    Pytest
    ```
- Use Gherking test: Given, When Then
    ```bash
       """
        Given valid user data
        When registering a new user
        Then the user should be created
        And a 201 status code should be returned
        """
    ```
### Types of Tests Performed
- **Integration test**: Check the interaction between different parts of the system, such as the database, views, and authentication. For example, when testing a user's registration (test_register_user), you are checking that the entire system works from start to finish, including creating the user in the database.


## 📧 Contact

For any inquiries, you can reach out to us through my GitHub and LinkedIn profiles:
- [![GitHub Octocat](https://img.icons8.com/ios-glyphs/30/000000/github.png)](https://github.com/helopgom)  [![LinkedIn](https://img.icons8.com/ios-glyphs/30/0077b5/linkedin.png)](https://www.linkedin.com/in/helena-lopgom/)  Helena

## 😊 If you've made it this far, feel free to follow me on GitHub or LinkedIn. I'd love to be in touch!
