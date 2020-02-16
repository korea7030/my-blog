#FROM node:11.13.0-alpine
FROM node

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD ./web /usr/src/app

RUN npm install
RUN npm run build


RUN rm -f package-lock.json
ENV HOST 0.0.0.0
EXPOSE 3000

ARG APP_NODE_ENV=production
ENV NODE_ENV ${APP_NODE_ENV}

CMD ["npm", "start"]

