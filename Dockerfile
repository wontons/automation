FROM node:18-alpine AS build

WORKDIR /app/

COPY app/ ./

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]
