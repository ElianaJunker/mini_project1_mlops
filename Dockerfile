FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirement.txt

# Expose the port that FastAPI will run on
EXPOSE 8005

# Run the FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8005", "--reload"]