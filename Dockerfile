FROM python:latest
WORKDIR /app
COPY . /app
RUN  pip install -r requirements.txt
EXPOSE 80
CMD ["streamlit", "run", "app.py"]