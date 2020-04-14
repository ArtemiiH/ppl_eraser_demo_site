FROM python:3.7-buster

ARG FLASK_ENV=production
ARG INPAINT_API_URL

COPY requirements.txt /app/
COPY demo_site /app/demo_site
COPY cmd.sh /app/
WORKDIR /app/

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r requirements.txt && \
    python3 -m pip install gunicorn

ENV FLASK_ENV=${FLASK_ENV}
ENV FLASK_APP="demo_site:create_app('${FLASK_ENV}')"
ENV FLASK_RUN_PORT=80
ENV PORT=80
ENV INPAINT_API_URL=${INPAINT_API_URL}
EXPOSE ${FLASK_RUN_PORT}

RUN groupadd -r ppl_eraser && useradd -r -g ppl_eraser ppl_eraser
RUN chown -R ppl_eraser:ppl_eraser /app
USER ppl_eraser

CMD ["./cmd.sh"]
