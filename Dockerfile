FROM python:3.6
COPY . /app
WORKDIR /app
EXPOSE 4002
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
