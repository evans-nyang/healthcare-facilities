FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the data and the app
COPY data/kenya_health_facilities_clean.csv data/kenya_health_facilities_clean.csv

COPY healthcare_assistant .

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]
