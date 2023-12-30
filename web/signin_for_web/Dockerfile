FROM php:7.4.21-fpm-alpine


RUN rm -rf /var/www/html/*
COPY ./index.php /var/www/html
COPY ./flag.php /var/www/html

WORKDIR /var/www/html
CMD ["php", "-S", "0.0.0.0:80"]


EXPOSE 80

