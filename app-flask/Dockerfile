FROM python:3.10.13-bookworm

# Copy the current directory contents into the container at /app/models
WORKDIR /app/models
COPY ["models/.", "./"]

# Set the working directory to /app
WORKDIR /app
COPY ["predict.py", "requirements.txt", "./"]

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 6969 available to the world outside this container
EXPOSE 6969

# Run gunicorn server when the container launches (for production)
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:80", "predict:app"]

# docker build -t parkinson-predict .
# docker run -it --rm -p 6969:80 parkinson-predict
