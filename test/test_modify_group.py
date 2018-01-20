from model.group import Group
from random import randrange
import random

#def test_modify_group_name(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    index = randrange(len(old_groups))
#    group = Group(name="222")
#    group.id = old_groups[index].id
#    app.group.modify_group_by_index(index, group)
#    assert len(old_groups) == app.group.count()
#    new_groups = app.group.get_group_list()
#    old_groups[index] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_modify_group_name2(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group1 = random.choice(old_groups)
    group = Group(name="222")
    #group.id = old_groups[index].id
    app.group.modify_group_by_id(group1.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    new_old_groups = []
    for old_group in old_groups:
        if old_group.id == group1.id:
            old_group.name = group.name
        new_old_groups.append(old_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if db.check_ui == 'true':
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)




#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="2222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_modify_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="test"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(footer="22222"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
