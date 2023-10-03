# Python Version -- 3.10v
FROM python:3.10

# Define Working Directory
WORKDIR /app

# Copies Requirements Text File into Docker Container(root/.)
COPY requirements.txt .

# PIP Install Dependencies < requirements.txt
RUN pip install -r requirements.txt

# Copy Python Script('semantic.py') into Docker Container(root/.)
COPY semantic.py .

# Copy Python Script('example.py') into Docker Container(root/.)
COPY example.py .

# CLI Command - Run Python Script('semantic.py')
CMD ["python", "semantic.py"]
