FROM python:3.11-slim-bullseye


WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY wf /app/wf
COPY main.py /app
COPY images /app/images


EXPOSE 8501

CMD ["streamlit", "run", "main.py"]
