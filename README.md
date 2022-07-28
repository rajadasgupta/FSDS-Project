# FSDS-Project
Housing price detection

HEROKU_EMAIL: raja.s.dasgupta@gmail.com
HEROKU_API_KEY: c9df8ecc-7eda-4598-abfc-386968998824
HEROKU_APP_NAME: ml-housing-project


List docker images
docker images
#to run docker image
docker run -p 5000:5000 -e PORT=5000 45d78ee557cb
docker stop <containerID> # to stop container
docker ps # to check running containers

Once the CI/CD pipeline is created
Now create 
a. Housing folder and __init__.py file
b. create a setup.py file so that we do not have to run the requirenments.txt file everytime to install various libraries
run command python setup.py install
 #########################################################################################################################
 
Software and account Requirement.
Github Account
Heroku Account
VS Code IDE
GIT cli
GIT Documentation
Creating conda environment

conda create -p venv python==3.7 -y
conda activate venv/
OR

conda activate venv
pip install -r requirements.txt
To Add files to git

git add .
OR

git add <file_name>
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status

git status
To check all version maintained by git

git log
To create version/commit all changes by git

git commit -m "message"
To send version/changes to github

git push origin main
To check remote url

git remote -v
To setup CI/CD pipeline in heroku we need 3 information

docker build -t <image_name>:<tagname> .
Note: Image name for docker must be lowercase

To list docker image

docker images
Run docker image

docker run -p 5000:5000 -e PORT=5000 f8c749e73678
To check running container in docker

docker ps
Tos stop docker conatiner

docker stop <container_id>
python setup.py install
Install ipykernel

pip install ipykernel
Data Drift: When your datset stats gets change we call it as data drift

Write a function to get training file path from artifact dir