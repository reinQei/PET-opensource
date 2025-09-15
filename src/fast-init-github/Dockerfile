FROM python:3.12

RUN apt-get update && \
    apt-get install -y git && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get install -y git openssh-client

RUN git config --global user.name "fast init script" && \
    git config --global user.email "reinqler@gmail.com"

ENV GIT_SSH_COMMAND="ssh -o StrictHostKeyChecking=accept-new"

WORKDIR /app

RUN mkdir /workspace

COPY fast-init-repos.py .


CMD ["python3", "-u", "fast-init-repos.py"]