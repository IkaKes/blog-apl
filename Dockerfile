FROM python:3.10.6-buster

ENV APPROOT="/home/app/web" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    VERSION="0.1" 

LABEL base.name="Blog App" \
      base.version="${VERSION}"

RUN groupadd -r -g 2200 app && \
    useradd -rM -g app -u 2200 app

WORKDIR $APPROOT

EXPOSE 5000

RUN apt-get update && apt-get install -y \
    --no-install-recommends netcat \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
COPY backend/requirements.txt $APPROOT/requirements.txt
RUN pip install -r requirements.txt
COPY backend $APPROOT
COPY frontend $APPROOT/frontend

RUN chown -R app:app $APPROOT

USER app

ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
