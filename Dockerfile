#
# @Dockerfile Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

# First line specifies which OS version to use
FROM python:3.8.5-slim-buster
# Setup working directory
WORKDIR /app

# Copy all files to app directory
COPY . /app
# EXPOSE 5000
RUN pip install -r requirements.txt
# Run these commands to make graphql work with flask run
RUN export FLASK_APP=app.py
ENV FLASK_APP=app.py
EXPOSE 6012
CMD ["python3", "app.py"]
