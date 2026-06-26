# Node 24 to match the local dev toolchain (npm 11) that generated package-lock.json.
# Mismatched npm versions make `npm ci` reject the lock file.
FROM node:24-slim

# Where our code lives inside the container
WORKDIR /app

# Copy dependency manifests first, then install (lets Docker cache this layer).
# We use `npm install` rather than the stricter `npm ci` because the lock file is
# generated on macOS/arm64 and lacks the Linux variants of some native-binding
# optional deps (@emnapi/*), which makes `npm ci` fail in this Linux image.
# (Strict `npm ci` is fine once the lock is generated on Linux, e.g. in CI.)
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the production version of the Next.js app
RUN npm run build

# Next.js serves on port 3000
EXPOSE 3000

# Default command: start the production server
CMD ["npm", "start"]
