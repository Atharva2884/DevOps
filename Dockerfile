FROM python:3.9-slim

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone your repository
RUN git clone FROM python:3.9-slim

WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone your repository
RUN git clone https://github.com/Atharva2884/DevOps.git .

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Create startup script
RUN echo '#!/bin/bash\ngit pull\npython app.py' > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"] .

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 5000

# Create startup script
RUN echo '#!/bin/bash\ngit pull\npython app.py' > /app/start.sh
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
