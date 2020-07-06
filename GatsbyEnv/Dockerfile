FROM node:12-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

RUN npm init -y
RUN npm install -g gatsby
RUN npm install gh-pages
RUN apt-get update
RUN apt-get install -y git
RUN gatsby new my-blog https://github.com/gatsbyjs/gatsby-starter-blog

