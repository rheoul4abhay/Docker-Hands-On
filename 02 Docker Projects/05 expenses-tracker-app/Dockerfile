# ---------Stage 1) Build Application
FROM maven:3.9-eclipse-temurin-17 AS builder
WORKDIR /app
COPY . .
# Build application and skips tests
RUN mvn clean install -DskipTests=true

# ---------Stage 2) Run Application in the runtime
FROM eclipse-temurin:17-jre-alpine
WORKDIR /app
# Copy the built jar file from the builder stage, NOTE: that the name "expenseapp.jar" isnt random and it comes from the application properties file so look into it and then name the built jar file accordingly
COPY --from=builder /app/target/*.jar /app/expenseapp.jar

# Expose the application port
EXPOSE 8080

# Start the application
ENTRYPOINT ["java", "-jar", "/app/expenseapp.jar"]