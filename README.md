# Django API Project

This is a Django project that provides an API for uploading and processing images. The API allows users to upload images, generate thumbnails in different sizes, and manage expiration times for their images.

This API also uses JWT authentication to authorize and authenticate the users. Moreover, the API provides the ability to assign users to three different plans: Basic, Premium, Enterprise, or to generate custom tiers and define the features of the tiers.

The API has been designed to have good performance, even under load. Strategies like pagination have been used to increase the performance of the API. Tests have been written to test all the functionality of the API. Data validation has been established in the source code. Moreover the project also contains Docker file to easily convert the project into a Docker image.


## Installation

To install the project, follow these steps:

- Clone the repository to your local machine
- Install the required dependencies using pipenv by running the following command:

'pip install -r requirements.txt'


Please note that the required dependencies of the project have been defined in the requirements.txt file

- Create a new file named .env in the project's root directory and set the required environment variables. Refer to the .env.example file for the required variables.
- Apply the database migrations using the following command:

'python manage.py migrate'


## Usage


### Docker Usage


#### Prerequisites

- Install [Docker](https://www.docker.com/get-started) on your machine.


#### Building the Docker Image

1. Open a terminal/command prompt and navigate to the root directory of your Django project (where the Dockerfile is located).

2. Build the Docker image by running the following command:

'docker build -t api_project .'


Replace `api_project` with the desired name for your Docker image. The period at the end of the command specifies that the Dockerfile is located in the current directory.


#### Running the Docker Container

1. After the image has been built, run the following command to start a container:

'docker run -it -p 8000:8000 --name epic_noble api_project'


Replace `epic_noble` with a name for your Docker container, and `api_project` with the name you used when building the Docker image. This command maps port 8000 of the container to port 8000 of the host machine, allowing you to access the Django app on your host machine.

2. Access your Django app on your host machine by opening a web browser and navigating to `http://localhost:8000` or `http://127.0.0.1:8000`.


#### Stopping the Docker Container

1. To stop the container, press `Ctrl+C` in the terminal where the container is running.


#### Starting a Stopped Docker Container

1. To start the container again, use the following command:

'docker start -ai epic_noble'


Replace `epic_noble` with the name you used when running the container.


### Development Server Usage

Alternatively, to run the development server, use the following command:

'python manage.py runserver'


The API endpoints can be accessed at `http://localhost:8000/api/`.


## Testing

To run the tests, use the following command:

'python manage.py test'


## API Endpoints

The following endpoints are available in the API:

| Endpoint          | Method | Description                            |
|-------------------|--------|----------------------------------------|
| /api/images/      | POST   | Upload a new image.                    |
| /api/images/      | GET    | List all uploaded images.              |
| /api/images/<pk>/ | GET    | Retrieve the details of a specific image.|
| /api/images/<pk>/ | PUT    | Update the details of a specific image.|
| /api/images/<pk>/ | DELETE | Delete a specific image.               |


## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository
2. Create a new branch for your changes
3. Commit your changes
4. Push the branch to your forked repository
5. Create a pull request for your changes to be merged with the main branch


## License

This project is licensed under the MIT license.


## Acknowledgments

- Django documentation
- Stack Overflow
- Various online tutorials and resources












