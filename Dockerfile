# Pulling the Ubuntu image
FROM ubuntu:focal

# Updating the packages
RUN apt-get update -y --fix-missing

# Installing the movie maker 
RUN apt install -y ffmpeg

# Installing pip and python
RUN apt install -y python3-pip

# Setting the working dir 
WORKDIR /app 

# Copying the necesary files 
COPY requirements.txt . 

# Installing the requirements 
RUN pip install -r requirements.txt 

# Making the barplot race 
CMD ["python3", "draw_race.py"]
