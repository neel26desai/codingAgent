# Use an Nginx base image for the frontend
FROM nginx:alpine

# Set the working directory for Nginx
WORKDIR /usr/share/nginx/html

# Remove default Nginx HTML files
RUN rm -rf ./*

# Copy the frontend files to the container
COPY index.html ./ 

# Expose the frontend port
EXPOSE 80
