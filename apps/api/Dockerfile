# Start from a small official Python 3.12 image
FROM python:3.12-slim

# Where our code lives inside the container
WORKDIR /app

# Copy just the requirements first, then install them.
# (Doing this before copying the code lets Docker cache the install step.)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the backend code into the container
COPY . .

# Document that the app listens on port 8000
EXPOSE 8000

# Default command: start the API server
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
