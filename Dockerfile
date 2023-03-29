FROM python

ENV PYTHON_VERSION 3.10.5

WORKDIR /PassGenAPI

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /PassGenAPI/passgenapi

COPY /passgenapi .

EXPOSE 8000

WORKDIR /PassGenAPI

CMD ["uvicorn", "passgenapi.main:app", "--host", "0.0.0.0", "--port", "80"]