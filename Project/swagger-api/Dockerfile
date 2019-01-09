FROM ubuntu
MAINTAINER AryDwiMarta

#update, upgrade, and install maven
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install maven

#to fix Warning: JAVA_HOME environment variable is not set.
#ENV export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
#ENV export PATH=$JAVA_HOME/bin:$PATH

ADD export.sh /root/export.sh

CMD [./export.sh]

#CMD export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64
#CMD export PATH=$JAVA_HOME/bin:$PATH


#copy file
#COPY ./path