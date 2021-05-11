FROM python:3.7 AS base
RUN mkdir /forgerock_stocks
WORKDIR /forgerock_stocks
COPY requirements.txt /forgerock_stocks
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY . /forgerock_stocks
EXPOSE 5000
CMD ["python", "main.py"]
