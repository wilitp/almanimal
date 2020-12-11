FROM python:3.8-alpine
EXPOSE 8000
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ADD ./requirements.txt .
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev libressl-dev musl-dev zlib-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN python -m pip install -r requirements.txt
RUN sed -i 's/django.utils.encoding/six/g' /usr/local/lib/python3.8/site-packages/jet/models.py
RUN cat /usr/local/lib/python3.8/site-packages/jet/models.py 
WORKDIR /app
COPY ./proyecto ./
COPY ./docker-entrypoint.sh ./
RUN ["chmod", "+x", "/app/docker-entrypoint.sh"] 
ENTRYPOINT [ "/app/docker-entrypoint.sh" ]
