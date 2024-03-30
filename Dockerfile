# Use a lightweight Nginx image
FROM nginx:alpine

# Set up application directory
WORKDIR /app

# Copy web application files into the container
COPY html_templates/index.html /usr/share/nginx/html/index.html
COPY css/index.css /usr/share/nginx/html/css/index.css
COPY js/index.js /usr/share/nginx/html/js/index.js

COPY html_templates/data_entry.html /usr/share/nginx/html/data_entry.html
COPY css/data_entry.css /usr/share/nginx/html/css/data_entry.css
COPY js/data_entry.js /usr/share/nginx/html/js/data_entry.js


EXPOSE 80

