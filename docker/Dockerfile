#from base image
FROM python:3.12-bookworm

WORKDIR /usr/src/soundspruce-site

#prevents python writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE 1
#stops Python from buffering stdout and stderr - apparently this causes problems with docker
ENV PYTHONUNBUFFERED 1

#copy reqs from workdir source to docker dir
COPY ../requirements.txt ./

#install reqs
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the files from that dir
COPY . .

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "soundspruce.wsgi"]
