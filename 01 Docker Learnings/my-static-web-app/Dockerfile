FROM node:alpine
RUN npm install -g http-server
WORKDIR /app
COPY . /app
EXPOSE 8080
CMD ["http-server", ".", "-p", "8080", "-c-1"]
