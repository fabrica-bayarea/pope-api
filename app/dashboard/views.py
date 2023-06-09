# -*- coding: utf-8 -*-
from flask import render_template
from flask_login import login_required
from . import dashboard
from app.models.area import Area
from app.models.attendance import Attendance
from app.models.organization import Organization


@dashboard.route('/')
@login_required
def dashboard():
    data = []
    return render_template('index.html', data=data)
