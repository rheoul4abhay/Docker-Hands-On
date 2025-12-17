# Base image
FROM eclipse-temurin:17-jdk-alpine

# Labels
LABEL maintainer="abhayshrivastava830@gmail.com"
LABEL version="1.0"
LABEL description="A simple java application"

# Set the Working directory inside the container
WORKDIR /app

# Copy source code into the container
COPY src/Main.java /app/Main.java

# Compile the java code
RUN javac Main.java

# Run the Java Application when the container starts
CMD ["java", "Main"]