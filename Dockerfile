
FROM python:3.11

RUN apt-get update
RUN apt-get install -y git

RUN git clone https://github.com/Rabbbint/Lab4.git

WORKDIR /Laba4

RUN pip install -r requirements.txt

CMD ["python", "Project.py"]