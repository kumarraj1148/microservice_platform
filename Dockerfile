# FROM python:alpine3.17

# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY src src 
# EXPOSE 5000
# HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=5 CMD curl -f http://localhost:5000/health || exit 1
# ENTRYPOINT [ "python", "./src/app.py"]


FROM python:3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
