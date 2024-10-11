 # Flask App with MySQL Docker Setup

This is a simple Flask app that interacts with a MySQL database. The app allows users to submit messages, which are then stored in the database and displayed on the frontend.

## Prerequisites

Before you begin, make sure you have the following installed:

- Docker
- Docker Compose
- Git (optional, for cloning the repository)

## Setup

1. Clone this repository (if you haven't already):

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-repo-name
   ```
## Usage

1. Start the containers using Docker Compose:

   ```bash
   docker-compose up --build
   ```

2. Access the Flask app in your web browser:

   - Backend: http://localhost:5000
   
## To run this two-tier application using  without docker-compose

- First create a docker image from Dockerfile
```bash
docker build . -t wedding
```

- Now, make sure that you have created a network using following command
```bash
docker network create wedding
```

- Attach both the containers in the same network, so that they can communicate with each other

i) MySQL container 
```bash
docker run -d \
    --name database \
    -v mysql-data:/var/lib/mysql \
    --network=wedding \
    -e MYSQL_DATABASE=rsvp \
    -e MYSQL_USER=root \
    -e MYSQL_ROOT_PASSWORD=kali \
    -p 3306:3306 \
    mysql:5.7

```
ii) Backend container
```bash
docker run -d \
    --name flaskapp \
    --network=wedding \
    -e MYSQL_HOST=database \
    -e MYSQL_USER=root \
    -e MYSQL_PASSWORD=kali \
    -e MYSQL_DB=rsvp \
    -p 5000:5000 \
    wedding:latest

```

3. Access the Flask app in your web browser:

   - Backend: http://localhost:5000

## Notes

- Make sure to replace placeholders (e.g., `your_username`, `your_password`, `your_database`) with your actual MySQL configuration.

- This is a basic setup for demonstration purposes. In a production environment, you should follow best practices for security and performance.

- Be cautious when executing SQL queries directly. Validate and sanitize user inputs to prevent vulnerabilities like SQL injection.

- If you encounter issues, check Docker logs and error messages for troubleshooting.

```
# Wedding-lite

## Screenshots

### Home Page
![Wedding Lite](Screenshot%202024-10-10%20185613.png)
![Screenshot](https://github.com/Bakhtawarkhan90/Wedding-lite/main/Screenshot%202024-10-10%20185613.png)

### Features Page
![Features Page](https://github.com/Bakhtawarkhan90/Wedding-lite/main/Screenshot%202024-10-10%20185704.png)

### Contact Page
![Contact Page](https://github.com/Bakhtawarkhan90/Wedding-lite/main/Screenshot%202024-10-10%20185750.png)

Welcome to Wedding-lite! 

## Screenshots

### Screenshot 1
![Screenshot 1](./Screenshot%202024-10-10%20185613.png)

### Screenshot 2
![Screenshot 2](./Screenshot%202024-10-10%20185704.png)

### Screenshot 3
![Screenshot 3](./Screenshot%202024-10-10%20185750.png)

