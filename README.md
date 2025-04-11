# Data-Slinger

**Data-Slinger** is a base Docker image designed to run a Django project with integrated telemetry (logging, metrics, and tracing) using OpenTelemetry and uWSGI. It is built to serve as a foundational image that you can extend for your Django applications.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running.
- (Optional) [Git](https://git-scm.com/) to clone the repository.
- (Optional) An existing `.env` file with your environment variables (see _Configuration_ below).

## Getting Started

### 1. Clone the Repository

Clone the repository from GitHub (or your source control) and change into the project directory:

```bash
git clone https://github.com/your-username/data-slinger.git
cd data-slinger
```

### 2. Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t data-slinger-image .
```

This command does the following:

 - Reads the Dockerfile in the current directory.
 - Creates an image tagged data-slinger-image.

### 3. Run the Docker Container (For testing)

Once the image is built, run it to test the application using:

```bash
docker run --rm -p 8000:8000 data-slinger-image
```

This command will:

 - Map port 8000 in the container to port 8000 on your host.
 - Remove the container once it stops (thanks to the --rm flag).

### 4. Test the application

After running the container, open your web browser and navigate to:

```bash
http://localhost:8000
```

After running open newrelic logs to see the first log of `Application Started`



