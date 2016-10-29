# -*- coding: utf-8 -*-

from . import spiders

@spiders.route('/test/', methods=['GET', 'POST'])
def test():
    return 'Everything is OK!'
