# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose FastAPI's default port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "chatbot:app", "--host", "0.0.0.0", "--port", "8000"]
