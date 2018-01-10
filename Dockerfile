FROM python:3

WORKDIR /opt/personal-website

ADD . ./
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "./run.py"]

EXPOSE 5000
