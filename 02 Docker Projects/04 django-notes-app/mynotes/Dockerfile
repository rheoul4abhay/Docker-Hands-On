# Stage 1: Build and install dependencies
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
# Copy rest of the source code
COPY . . 

# Optional: build step RUN npm run build, then it generates the built file in dist folder

# ---- Stage 2: runtime
FROM node:18-alpine
WORKDIR /app
# copy dependencies from first stage
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package*.json ./

# If you produce build output (preferred):
# COPY --from=builder /app/dist ./dist
# CMD ["node", "dist/server.js"]

# If you run directly from source, then copy only what’s needed:
COPY --from=builder /app/src ./src
COPY --from=builder /app/server.js ./server.js
EXPOSE 3000
CMD ["npm", "start"]
