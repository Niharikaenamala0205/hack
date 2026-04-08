FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install gradio fastapi uvicorn openai requests
CMD ["python", "app.py"]
