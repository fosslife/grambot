#Create a ubuntu base image with python 3 installed.
FROM pypy:slim-bullseye

WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Copy the .env file to the container
COPY .env .

# Set environment variables if necessary
# ENV VARIABLE_NAME value

# Expose any necessary ports
# EXPOSE port_number

# Run the command to start the application
CMD [ "python", "-m", "userbot" ]