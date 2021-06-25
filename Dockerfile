# init a base image (Alpine is small Linux distro)
FROM python:3.8-slim-buster
# define the present working directory
WORKDIR /docker-neuro
# copy the contents into the working dir
ADD . /docker-neuro
# run pip to install the dependencies of the flask app
RUN pip install -r requirements.txt
# define the command to start the container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]