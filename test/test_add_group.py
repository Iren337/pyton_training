# -*- coding: utf-8 -*-
from model.group import Group


def test_test_add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
#    old_groups = app.group.get_group_list()
    app.group.create(group)
#    db.connection.commit()
    #    assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if db.check_ui =='true':
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_test_add_empty_group(app):
#        old_groups = app.group.get_group_list()
#        group = Group(name="", header="", footer="")
#        app.group.create(group)
#        assert len(old_groups) + 1 == app.group.count()
#        new_groups = app.group.get_group_list()
#        old_groups.append(group)
#        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
