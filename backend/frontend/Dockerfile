# Use an Nginx image to serve static files
FROM nginx:alpine

# Set the working directory
WORKDIR /usr/share/nginx/html

# Copy the current directory contents into the container
COPY . .

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]
