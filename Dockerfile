FROM python:3.10.13-bookworm

# Set the working directory to /app
WORKDIR /app
COPY ["predict.py", "requirements.txt", "./"]

WORKDIR /app/models
COPY ["models/.", "./"]


WORKDIR /app
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
# CMD ["python", "/app/predict.py"]

# Make port 6969 available to the world outside this container
EXPOSE 6969

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:6969", "predict:app"]

# docker build -t parkinson-predict .
# docker run -it --rm -p 6969:6969 parkinson-predict
