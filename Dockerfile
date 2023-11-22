FROM python:3.11-slim

WORKDIR /app
COPY ./.streamlit/ /app/.streamlit/
COPY ./paginas/ /app/paginas/
COPY ./*.py /app/
COPY ./*.sql /app/
COPY ./requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /app/requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
