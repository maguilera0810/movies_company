Movies Api
==========

This is an example of my code, using Django as the main framework. Here you will find versioning of rest api, authentication with jwt, management of settings and requirements for different environments, examples of object-oriented programming, tasks running on background and much more

---

# Index

- [Prerequisites](#prerequisites-📋) 📋
- [Requirements](#requirements-🔧) 🔧
- [Setting Environment Variables](#setting-environment-variables-📦) 📦
- [Running the project](#running-the-project-⚙️) ⚙️
- [Test Accounts](#test-accounts-👥) 👥
- [Endpoints](#endpointsextraendpointsmd-📩) 📩
- [Tools](#tools-🛠️) 🛠️
- [Resume Tasks and Explanations](#resume-tasks-and-explanationsextraresumemd-📚) 📚
- [Authors](#authors-️) ✒️

---

# Let's go 🚀

_These instructions will allow you to get a working copy of the project on your local machine for development and testing purposes._

# Prerequisites 📋

[Index](#index)

- [Python 3.8.10](https://rometools.github.io/rome/) or higher, on linux you can use the following commands if you don't have it

```bash
sudo apt update
sudo apt install python3
```

- [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
  
# Requirements 🔧

[Index](#index)

  Here you will find requirements for local and production environments:

- Local

```bash
pip install -r requirements/local.txt 
```

- Production

```bash
pip install -r requirements/prod.txt 
```

# Setting Environment Variables 📦

[Index](#index)

Create an **.env file** with the following settings, you will also find an example **.env.dist file**

```
DEBUG=True
DELAY_API_URL="https://deelay.me"
```

# Running the project ⚙️

[Index](#index)

#### _Running the project in local environment_

```bash
python manage runserver --settings=settings.local
```

#### _Running the project in development environment_

```bash
python manage runserver --settings=settings.dev
```

#### _Running the project in production environment_

```bash
python manage runserver --settings=settings.prod
```

---

# Test Accounts 👥

In order to play with the API, you can use these accounts or create your own ([see](extra/ENDPOINTS.md#create-user)).

- Normal User

  ```json
  {
    "email": "normal_user@gmail.com",
    "password": "123456"
  }
  ```

- Admin User

  ```json
  {
    "email": "admin_user@gmail.com",
    "password": "123456"
  }
  ```

- SurperAdmin User

  ```json
  {
    "email": "super_user@gmail.com",
    "password": "123456"
  }
  ```

# [Endpoints](extra/ENDPOINTS.md) 📩

[Index](#index)

Below is a list of the available endpoints, which will have 3 types of permissions: all_users, auth_users and admin_users

- ## [JWT](extra/ENDPOINTS.md#jwt)

- ## [User](extra/ENDPOINTS.md#user)

- ## [Alias](extra/ENDPOINTS.md#alias)

- ## [Movie](extra/ENDPOINTS.md#movie)

- ## [Genre](extra/ENDPOINTS.md#genre)

# Tools 🛠️

[Index](#index)

- [Python](https://www.python.org/) - is an easy language to read and write due to its great similarity to human language. Plus, it's an open source, cross-platform language and therefore free!

- [Django](https://www.djangoproject.com/) - is one of the most popular frameworks for developing web applications using the Python language. It has advantages such as its use of software architecture patterns, its flexibility, the high quality of its documentation, and its large community of developers.

- [DjangoRestFramework](https://www.django-rest-framework.org/) - is a framework that allows us to easily develop a REST API in Python. It has several advantages such as authentication, security, serialization, pagination, direct interaction with the Django ORM among others.

- [pdb](https://docs.python.org/3/library/pdb.html) - it's a really easy python debugger, to check a code snippets or whole streams, recommended for beginners in debugging
  
- [threading](https://docs.python.org/3/library/threading.html) - is a simple way to carry out tasks running on background

- [Redis](https://rometools.github.io/rome/) - Usado para generar RSS

# [Resume Tasks and Explanations](extra/RESUME.md) 📚

- [Requirements](extra/RESUME.md#requirements)
- [Extra Features](extra/RESUME.md#extra-feature)
- [Deliverables](extra/RESUME.md#deliverables)
- [Extra Credit](extra/RESUME.md#extra-credit)

# Authors ✒️

[Index](#index)

- **Mauricio Aguilera** - _IT Enginneer_
  - [Github](https://github.com/maguilera0810)
  - [Linkedin](https://www.linkedin.com/in/maguilera-jaramillo/)

---
⌨️ with ❤️ by [Mauricio Aguilera](https://github.com/maguilera0810) 😊
