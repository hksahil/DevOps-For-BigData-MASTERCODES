FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install streamlit pandas
EXPOSE 8501
CMD ["streamlit","run","app.py"]