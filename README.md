Movies Api
==========

This is an example of my code, using Django as the main framework. Here you will find versioning of rest api, authentication with jwt, management of settings and requirements for different environments, examples of object-oriented programming, technologies such as Celery and Redis, and much more

---

# Let's go 🚀

_These instructions will allow you to get a working copy of the project on your local machine for development and testing purposes._

# Prerequisites 📋

- [Python 3.8.10](https://rometools.github.io/rome/) or higher, on linux you can use the following commands if you don't have it

```bash
sudo apt update
sudo apt install python3
```

- [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/)
  
# Requirements 🔧

  Here you will find requirements for local and production environments:

- Local

```bash
pip install -r requirements/local.txt 
```

- Production

```bash
pip install -r requirements/prod.txt 
```

# Setting Environment Variables

Create an **.env file** with the following settings, you will also find an example **.env.dist file**

```
DEBUG = True
CELERY_BROKER_URL = "replace_with your_value" #"redis://localhost:6379"
CELERY_RESULT_BACKEND = "replace_with your_value" #"redis://localhost:6379"
```

# Running the project ⚙️

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

# [Endpoints](extra/ENDPOINTS.md)

Below is a list of the available endpoints, which will have 3 types of permissions: all_users, auth_users and admin_users

- ## [JWT](extra/ENDPOINTS.md#jwt)

- ## [User](extra/ENDPOINTS.md#user)

- ## [Alias](extra/ENDPOINTS.md#alias)

- ## [Movie](extra/ENDPOINTS.md#movie)

- ## [Genre](extra/ENDPOINTS.md#genre)

# Tools 🛠️

- [Python](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
- [Django](https://maven.apache.org/) - Manejador de dependencias
- [DjangoRestFramework](https://maven.apache.org/) - Manejador de dependencias
- [Celerey](https://rometools.github.io/rome/) - Usado para generar RSS
- [Redis](https://rometools.github.io/rome/) - Usado para generar RSS

# Authors ✒️

- **Mauricio Aguilera** - _IT Enginneer_
  - [Github](https://github.com/maguilera0810)
  - [Linkedin](https://www.linkedin.com/in/maguilera-jaramillo/)

---
⌨️ with ❤️ by [Mauricio Aguilera](https://github.com/maguilera0810) 😊
