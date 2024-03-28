# Use a lightweight Nginx image
FROM nginx:alpine

# Set up your application directory
WORKDIR /app

# Copy your web application files into the container
COPY html_templates/index.html /usr/share/nginx/html/index.html

# Expose port 80 (if your application listens on port 80)
EXPOSE 80

