FROM ubuntu
MAINTAINER AryDwiMarta

#update, upgrade, and install maven
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install maven && apt-get -y install nodejs && apt-get -y install nodejs-legacy && apt-get -y install npm && apt-get -y install wget && apt-get -y install unzip && apt-get -y install git

RUN npm install -g http-server
RUN wget https://github.com/swagger-api/swagger-editor/archive/v3.5.5.zip

#to fix Warning: JAVA_HOME environment variable is not set.
#ENV export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
#ENV export PATH=$JAVA_HOME/bin:$PATH

RUN unzip v3.5.5.zip

RUN mv swagger-editor-3.5.5/* /

RUN git clone https://github.com/swagger-api/swagger-ui.git

RUN mv swagger-ui/* /

EXPOSE 8080

CMD [ "http-server" ]
#RUN http-server swagger-editor -D BACKGROUND