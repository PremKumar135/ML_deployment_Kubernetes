FROM ubuntu:18.04

RUN mkdir /opt/ml/ /opt/ml/Model
ADD Model /opt/ml/Model/
COPY requirements.txt diabetes_predictor.py app.py /opt/ml 

# Install "software-properties-common" (for the "add-apt-repository")
RUN apt-get update && apt-get install -y \
    software-properties-common

# Fix certificate issues
RUN apt-get update && \
    apt-get clean && \
    update-ca-certificates -f \
    rm -rf /var/lib/apt/lists/* 

#install python pip
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

#install requirements.txt
RUN pip3 install -r /opt/ml/requirements.txt

WORKDIR /opt/ml
EXPOSE 8000
ENTRYPOINT ["python3", "app.py"]