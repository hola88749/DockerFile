FROM python:3.9-slim
WORKDIR /app
COPY app.py /app
COPY requirements.txt /app
COPY templates/ /app/templates
COPY static/ /app/static
ENV PIP_PROGRESS_BAR=off
RUN PIP_NO_PROGRESS_BAR=off pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "app.py"]

