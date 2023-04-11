FROM registry.digital-insider.ru/di/devops/images/python:3.8.11-buster

# Extra python env
ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=magazine.settings

ARG PYPI_TOKEN_READ

WORKDIR /app
RUN apt-get update \
 && apt-get install -y -qq --no-install-recommends curl nano iputils-ping ethtool tcpdump jq \
 && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
COPY requirements.txt .

# устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


COPY . /app

RUN touch /tmp/touch.reload
RUN chmod +x /app/docker/cmd.sh

EXPOSE 8585
CMD ["/app/docker/cmd.sh"]
