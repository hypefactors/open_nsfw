FROM caffe:cpu

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:80", "app:app" ]
