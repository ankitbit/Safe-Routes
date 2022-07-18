FROM registry.gitlab.com/app-oneragtime/deepdive/ml-engine/ml_engine:latest

WORKDIR .

RUN rm -rf *
COPY . .

EXPOSE 5000
