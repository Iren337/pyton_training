# -*- coding: utf-8 -*-

from model.group import Group



def test_test_add_group(app):
        app.group.create(Group(name="11111", header="1111111", footer="111111111"))



def test_test_add_empty_group(app):
        app.group.create(Group(name="", header="", footer=""))




