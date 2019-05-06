FROM python:3.6.3

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install -y --no-install-recommends \
    sudo \
    libpam-systemd \
    systemd-sysv \
    dbus-x11 \
    systemd \
    npm \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    nginx \
    curl \
    openssh-server \
    build-essential \
    openssl \
    zlib1g-dev

RUN mkdir /my-blog
WORKDIR /my-blog
ADD requirements.txt /my-blog/requirements.txt
RUN pip install -r requirements.txt
ADD . /my-blog
RUN ["chmod", "+x", "./config/gunicorn/gunicorn_start.sh"]
ENTRYPOINT ["bash", "./config/gunicorn/gunicorn_start.sh"]
