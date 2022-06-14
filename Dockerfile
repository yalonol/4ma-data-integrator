FROM python:3.8
MAINTAINER Yalon Fishbein
WORKDIR TODO: /4ma-layer-filter

ADD main.py .
TODO: ADD dict_model_utils/helpers/pattern_generator.py .
COPY requirements.txt requirements.txt
TODO: COPY dict_model_utils/config.yaml dict_model_utils/config.yaml

RUN --mount=type=secret,id=NEXUS_USERNAME,dst=/run/secrets/nexus_user \
    --mount=type=secret,id=NEXUS_PASSWORD,dst=/run/secrets/nexus_password \
    NEXUS_USERNAME=$(cat /run/secrets/nexus_user) NEXUS_PASSWORD=$(cat /run/secrets/nexus_password) pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]