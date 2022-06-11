#
# @__init__.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft .
#

import requests
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
r = "postgresql://ngimluxm:zK59sGLE3DXX41RwivZ3MoceL5zGMqSu@stampy.db.elephantsql.com:5432/ngimluxm"
app.config["SQLALCHEMY_DATABASE_URI"] = r
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
