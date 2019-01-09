FROM php:5.6-apache

RUN apt-get update
RUN apt-get install -y net-tools
RUN docker-php-ext-install pdo pdo_mysql
RUN docker-php-ext-install sockets

RUN a2enmod rewrite
RUN a2enmod ssl

ADD 000-default.conf /etc/apache2/sites-enabled/
ADD default-ssl.conf /etc/apache2/sites-anabled/
ADD apache2.conf /etc/apache2/
ADD localhost.crt /etc/ssl/certs/
ADD localhost.key /etc/ssl/certs/
#ADD www-server/ www-server/

ADD www /var/www/site

EXPOSE 443

#RUN service apache2 start

CMD /usr/sbin/apache2ctl -D FOREGROUND
