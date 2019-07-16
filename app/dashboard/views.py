# -*- coding: utf-8 -*-
from flask import render_template
from flask_login import login_required
from . import dashboard


@dashboard.route('/')
@login_required
def dashboard():
    data = [{
        "id": 1,
        "first_name": "Leyla",
        "last_name": "Weathers",
        "email": "lweathers0@java.com",
        "city": "Carlton",
        "company_name": "Vidoo"
    }, {
        "id": 2,
        "first_name": "Wandie",
        "last_name": "Shurville",
        "email": "wshurville1@vistaprint.com",
        "city": "Brudzew",
        "company_name": "Youbridge"
    }, {
        "id": 3,
        "first_name": "Gill",
        "last_name": "Tsar",
        "email": "gtsar2@xing.com",
        "city": "Sicheng",
        "company_name": "Blogspan"
    }, {
        "id": 4,
        "first_name": "Carmina",
        "last_name": "Lyon",
        "email": "clyon3@samsung.com",
        "city": "São Manuel",
        "company_name": "Tagopia"
    }, {
        "id": 5,
        "first_name": "Hubert",
        "last_name": "Loxley",
        "email": "hloxley4@studiopress.com",
        "city": "Huancabamba",
        "company_name": "Yotz"
    }, {
        "id": 6,
        "first_name": "Elianore",
        "last_name": "Edgley",
        "email": "eedgley5@opera.com",
        "city": "Wonokromo",
        "company_name": "Kanoodle"
    }, {
        "id": 7,
        "first_name": "Daniela",
        "last_name": "Laxon",
        "email": "dlaxon6@desdev.cn",
        "city": "Halmstad",
        "company_name": "Zoovu"
    }, {
        "id": 8,
        "first_name": "Keely",
        "last_name": "Mac Geaney",
        "email": "kmacgeaney7@weebly.com",
        "city": "Pŭrvomaytsi",
        "company_name": "Skiptube"
    }, {
        "id": 9,
        "first_name": "Alfie",
        "last_name": "Manoch",
        "email": "amanoch8@sina.com.cn",
        "city": "Veguitas",
        "company_name": "Riffwire"
    }, {
        "id": 10,
        "first_name": "Charlotta",
        "last_name": "Madine",
        "email": "cmadine9@whitehouse.gov",
        "city": "Yilongyong",
        "company_name": "Zava"
    }]
    return render_template('index.html', data=data)
