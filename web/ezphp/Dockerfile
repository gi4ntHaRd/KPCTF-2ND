FROM php:7.4-apache

COPY ./src/ /var/www/html/
RUN chmod 755 /var/www/html && \
    chown root:root /var/www/html
ENV flag=flag{f1266cb9-d076-11ed-bbf0-70a8d34ece37}

CMD apache2-foreground