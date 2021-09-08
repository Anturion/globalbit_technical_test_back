FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
#ENTRYPOINT ["sh", "entrypoint.sh"]
# https://medium.com/@__pamaron__/deploy-a-django-application-connected-to-azure-sql-using-docker-and-azure-app-service-a2c107773c11
