FROM node:11.13.0-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN apk update && apk upgrade && apk add git

ADD ./web /usr/src/app

RUN npm i -g
RUN rm -f package-lock.json

ENV HOST 0.0.0.0
EXPOSE 3000

RUN npm install
RUN npm run build

CMD ["npm", "start"]

