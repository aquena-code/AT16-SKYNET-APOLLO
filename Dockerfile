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
FROM alpine:3.10

# Runs required features that python needs
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip \

# Setup working directory
WORKDIR /app

# Copy all files to app directory
COPY . /app

# Run requirements to install all packages
RUN pip3 --no-cache-dir install -r requirements.txt

# Run these commands to make graphql work with flask run
RUN set FLASK_APP=app.py
RUN set $env:FLASK_APP="app.py"

# Expose port
EXPOSE 5000
