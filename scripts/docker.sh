#!/bin/bash
# Show help message
# Define variables
IMAGE_NAME="todo"
CONTAINER_NAME="todo"
PORT_MAPPING="8000:8000"

# Build the Docker image
if [ "$(docker images -a $IMAGE_NAME)" ]; then
    echo "Removing existing image: $IMAGE_NAME..."
    docker rmi -f $IMAGE_NAME
fi
echo "Building Docker image: $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

# Check if a container with the same name already exists
if [ "$(docker ps -aq -f name=$CONTAINER_NAME)" ]; then
    echo "Removing existing container: $CONTAINER_NAME..."
    docker rm -f $CONTAINER_NAME
fi

# Run the Docker container
echo "Running container: $CONTAINER_NAME..."
docker run --name $CONTAINER_NAME -p $PORT_MAPPING -v ./src:/app/src -it $IMAGE_NAME:latest
