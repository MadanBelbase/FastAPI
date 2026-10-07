FROM  python:3.11-slim

#set working directory
WORKDIR /app

#copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the application code
COPY . .

# Expose the port that the application will run on
EXPOSE 8000

# Set the command to run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]