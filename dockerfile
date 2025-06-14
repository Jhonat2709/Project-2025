FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy the application code
COPY . .

# Run the build script
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Give permissions to the entrypoint and build scripts
RUN chmod +x entrypoint.sh

# Entrypoint to run the appplication
ENTRYPOINT [ "/app/entrypoint.sh" ]
