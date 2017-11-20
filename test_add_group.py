# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application



@pytest.fixture
def app(request):
    fixture =Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_add_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="11111", header="1111111", footer="111111111"))
        app.logout()


def test_test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.create_group(Group(name="", header="", footer=""))
        app.logout()




