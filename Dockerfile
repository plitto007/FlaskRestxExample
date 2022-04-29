FROM python:3.6.9
RUN apt-get update
COPY / /
RUN pip install -r requirements.txt

# RUN mkdir -p /build
# #
# copy ./ /build
# RUN ls build
# WORKDIR /build
# RUN chmod +x run.sh
RUN export FLASK_APP=run.py
# EXPOSE 5000
RUN ls
# CMD ["run.sh"]
# ENTRYPOINT ["run.sh"]
CMD ["flask","run","--host=0.0.0.0"]