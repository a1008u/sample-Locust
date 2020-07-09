FROM python:3.6-alpine

ADD locust-tasks /locust-tasks
RUN chmod -R 755 /locust-tasks

RUN apk --no-cache add g++ linux-headers \
    && pip install -r /locust-tasks/requirements.txt

EXPOSE 8089 5557 5558
ENTRYPOINT ["/locust-tasks/run.sh"]
