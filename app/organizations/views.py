# -*- coding: utf-8 -*-
from flask import render_template
from flask_login import login_required
from . import organizations
from app.models.area import Area
from app.models.attendance import Attendance
from app.models.organization import Organization


@organizations.route('/organization', methods=['GET', 'POST'])
@login_required
def dashboard():
    data = []
    return render_template('organizations/form.html')
