# url-shortener-api

A Flask API that can be used to shorten URLs and retrieve statistics on short URL usages.

# Environment Setup

In order to run the URL Shortener API it is advised that you make use of Docker and Docker Compose.

## Docker

macOS and Windows users can install Docker Desktop which contains both Docker and Docker-Compose tools required to run the project using Docker.

Linux users need to follow the instructions on [Get Docker CE](https://docs.docker.com/engine/install/ubuntu/) for Ubuntu and then Install [Docker Compose](https://docs.docker.com/compose/install/) separately.

# Running the project using Docker

The URL Shortener API has been setup to make use of Docker so that the container can more easily be run or deployed to various environments.

1. Build the image using Docker Compose:
   `docker-compose build`

2. Run Tests to make sure everything is working:
   `TBC`

3. Run the docker image using the .env file to populate required environment variables:
   `docker-compose --env-file .env up`

# Project Concerns / Considerations to address

1. The .env file should not be committed to the code repository and should be kept safe. However, for the purposes of this demo project it has been committed.

2. Use a more lightweight docker base image such as Alpine to improve performance.

3. The Hash ID Salt should be moved to a config or environments file so that it can be secured and configured.

4. Add User Registration and Authentication - In a production system it is unlikely that the statistics of a Shortened URL should be viewable by everyone.

5. Alternate approach: Using Firebase Dynamic Links as the basis for the URL Shortener.

6. wait-for-it.sh is an open source script used to ensure that the database container is up and running before the api container attempts to run DB migrations. A more robust approach should be taken to ensure that the container is up rather than waiting a pre determined amount of time.

7. A database volume has been added to ensure persistency of data when the db container goes down.
