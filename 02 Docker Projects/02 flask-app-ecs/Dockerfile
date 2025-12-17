FROM python:3.9-slim

# Working directory

WORKDIR /app

# Copy src code to container
COPY . .

# Run the build command
RUN pip install -r requirements.txt

# Expose port 80

EXPOSE 5000

# Command to run the application
CMD ["python", "run.py"]