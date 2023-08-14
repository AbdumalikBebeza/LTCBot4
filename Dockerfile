FROM python:3.10
EXPOSE 5004
RUN mkdir -p /opt/services/bot4/LTCbot4
WORKDIR /opt/services/bot4/LTCbot4

RUN mkdir -p /opt/services/bot4/LTCbot4/requirements
ADD requirements.txt /opt/services/bot4/LTCbot4/

COPY . /opt/services/bot4/LTCbot4/

RUN pip install -r requirements.txt
CMD ["python", "/opt/services/bot4/LTCbot4/main.py"]