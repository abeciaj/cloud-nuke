FROM amazon/aws-lambda-python:3.9

# Install cloud-nuke
RUN yum install -y wget && \
    wget -O /usr/local/bin/cloud-nuke https://github.com/gruntwork-io/cloud-nuke/releases/download/v0.11.0/cloud-nuke_linux_amd64 && \
    chmod +x /usr/local/bin/cloud-nuke

# Add your function code
COPY app.py ${LAMBDA_TASK_ROOT}

CMD ["app.lambda_handler"]
