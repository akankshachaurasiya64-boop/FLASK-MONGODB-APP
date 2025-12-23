# 1. Base image (Python)
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy requirements file
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy application code
COPY app.py .

# 6. Expose port (Flask runs on 5000)
EXPOSE 5000

# 7. Run the Flask application
CMD ["python", "app.py"]
