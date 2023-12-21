## Volleyball Skill Strategy Analyser

<p align="center">
  <img src="https://github.com/SawanoLab/VSSA_backend/assets/55621861/8eb11b71-8086-49e1-bf21-e9d567e97a60" width="100" alt="Volleyball Skill Strategy Analyser Logo"><br>
</p>
<p align="center"><em>Empowering Volleyball Strategies with Cutting-Edge Analysis</em></p>

## Prerequisites
Before you begin, ensure you have Docker installed on your system. Docker is a platform for developing, shipping, and running applications. 

If you haven't installed Docker yet, you can download it from the official Docker website.

## Installation Steps
Start Docker Containers
Launch your Docker containers using the following command. This command sets up and runs all the required services in the background.

`$ docker-compose up -d`

Access the API Container
Once the Docker containers are up and running, access the API container with this command:

`$ docker-compose run api bash`

Database Migration
Inside the API container, navigate to the database directory and run the Alembic upgrade to set up the database schema:

`(api)$ cd /usr/src/app/db && alembic upgrade head`

With these steps, your Volley Station Clone should be set up and ready to use. If you encounter any issues during the setup process, please refer to the Docker and Alembic documentation for additional guidance.

The file structure is based on the recommendations found in this article:　https://zenn.dev/yusugomori/articles/a3d5dc8baf9e386a58e5
