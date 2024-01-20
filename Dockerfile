# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir --index-url https://pypi.org/simple/ -r requirements.txt
RUN pip install Flask
RUN pip install py-healthcheck 
RUN pip install requests
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
#ENV FLASK_APP=your_app_filename_without_extension.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]

