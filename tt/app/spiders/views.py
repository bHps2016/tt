# -*- coding: utf-8 -*-

import json
from flask import jsonify, Response
from . import spiders
from .weekends import weekends

@spiders.route('/test/', methods=['GET', 'POST'])
def test():
    return 'Everything is OK!'


@spiders.route('/weekend/')
def weekend():
    result_list = weekends()
    return result_list
