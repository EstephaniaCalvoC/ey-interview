FROM python:3.11-slim

WORKDIR /ey-interview/back

COPY runtime_requirements.txt .

RUN pip install --no-cache-dir -r runtime_requirements.txt

COPY app app/

EXPOSE 80

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "app.serve:app", "--bind", "0.0.0.0:80"]
