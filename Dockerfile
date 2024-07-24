FROM python:3.8-alpine
WORKDIR /app
ENV PYTHONUNBUFFERED=1\
    # чтобы логи нормально вылезали из контейнера
    PYTHONDONTWRITEBYTECODE=1
    #кэш питон-кода
COPY requirements.txt /app/requirements.txt
RUN set -ex \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && python --version \
  && pip --version
COPY . /app
RUN  set -ex \
     && ls -al
CMD  ["python", "src/Main.py"]
