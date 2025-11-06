# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file
COPY offline-news-sms-bot/requirements.txt .

RUN pip install --default-timeout=200 --retries 3 --no-cache-dir -r requirements.txt
# Copy project files
COPY . .

# Expose port (change if your app uses different port)
EXPOSE 8081

# Start the app (change main file if needed)
CMD ["python", "offline-news-sms-bot/send_daily.py"]
