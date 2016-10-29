# -*- coding: utf-8 -*-

from flask import Blueprint

spiders = Blueprint(
        'spiders',
        __name__,
        template_folder = 'templates',
        static_folder = 'static'
        )

from . import views
