FROM python:alpine
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5001
COPY . /app
ENV PYTHONUNBUFFERED True
CMD ["python", "world.py"]