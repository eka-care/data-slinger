# Data Slinger

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

### 2. Create a `.env` File

Before building or running the Docker container, create a `.env` file in the root of the project directory with the following content:

```env
OTEL_RESOURCE_ATTRIBUTES=service.name=<service-name>
OTEL_EXPORTER_OTLP_HEADERS=api-key=<your-license-key>
OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=https://otlp.nr-data.net/v1/metrics
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=https://otlp.nr-data.net/v1/traces
```

### 3. Build the Docker Image

Build the Docker image using the following command:

```bash
docker build -t data-slinger-image .
```

This command does the following:

 - Reads the Dockerfile in the current directory.
 - Creates an image tagged data-slinger-image.


### 4. Run the Docker Container

Once the image is built, run it to test the application using:

```bash
docker run --rm -p 8000:8000 --env-file .env data-slinger-image
```

This will start the Django server on port 8000, integrated with OpenTelemetry and uWSGI.
