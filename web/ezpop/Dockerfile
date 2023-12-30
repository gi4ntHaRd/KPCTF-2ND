FROM php:7.4-apache

COPY ./src/ /var/www/html/
RUN chmod 755 /var/www/html && \
    chown root:root /var/www/html

CMD apache2-foreground