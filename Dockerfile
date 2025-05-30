FROM python:3.9-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir torch torchvision --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir gunicorn Pillow

ENV PORT=8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
