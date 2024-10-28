FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# RUN pip install --no-cache-dir -r requirements.txt

COPY data/kenya_health_facilities_clean.csv data/kenya_health_facilities_clean.csv

COPY healthcare_assistant .

EXPOSE 8000

ENTRYPOINT ["python", "app.py"]

# Run the FastAPI application with uvicorn
# CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
