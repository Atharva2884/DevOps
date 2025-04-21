FROM python:3.9-slim

# Install git
RUN apt-get update && apt-get install -y git

# Clone the repo inside the container
RUN git clone https://github.com/Atharva2884/DevOps.git /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
