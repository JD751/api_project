Django API Project

This is a Django project that provides an API for uploading and processing images. The API allows users to upload images, generate thumbnails in different sizes, and manage expiration times for their images. The API has been designed to have good performance, even under load. Strategies like pagination have been used to increase the performance of the API. Tests have been written to test all the functionality of the API. Data Validation has been established in the source code.

Installation:

To install the project, follow these steps:
- Clone the repository to your local machine
- Install the required dependencies using pipenv by running the following command:
pip install -r requirements.txt
Please note that the required dependencies of the project have been defined in the requirements.txt file

- Create a new file named .env in the project's root directory and set the required environment variables. Refer to the .env.example file for the required variables.
- Apply the database migrations using the following command:

python manage.py migrate

Usage:

To run the development server, use the following command:

python manage.py runserver

The API endpoints can be accessed at http://localhost:8000/api/.

Testing:

To run the tests, use the following command:

python manage.py test

API Endpoints:

The following endpoints are available in the API:

| Endpoint          | Method | Description                            |
|-------------------|--------|----------------------------------------|
| /api/images/      | POST   | Upload a new image.                    |
| /api/images/      | GET    | List all uploaded images.              |
| /api/images/<pk>/ | GET    | Retrieve the details of a specific image.   |
| /api/images/<pk>/ | PUT    | Update the details of a specific image.|
| /api/images/<pk>/ | DELETE | Delete a specific image.               |


Contributing:

If you would like to contribute to this project, please follow these guidelines:

Fork the repository
Create a new branch for your changes
Commit your changes
Push the branch to your forked repository
Create a pull request for your changes to be merged with the main branch.

License:

This project is licensed under the MIT license.

Acknowledgments:

Django documentation
Stack Overflow
Various online tutorials and resources