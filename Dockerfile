# 1. Start with a base image that has Python installed
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy the current directory contents (including app.py) into the container
COPY . /app

# 4. Install dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Expose the port your Flask app will run on
EXPOSE 5000

# 6. Command to run the Flask app (replace app.py with your actual app file)
CMD ["python", "app.py"]
