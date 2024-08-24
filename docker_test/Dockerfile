# Use a base Linux image with Python
FROM python:3.9

# Set the working directory
WORKDIR /code

# Copy the requirements.txt file into the container
COPY requirements.txt /code/

# Install the required Python packages
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /code/requirements.txt

# Copy the rest of the application code into the working directory
COPY . /code/

# Expose the port on which the app will run
EXPOSE 8000

# Set the defaultnd to run the application
CMD ["uvicorn", "app.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]

