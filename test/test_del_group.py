from model.group import Group
import random


def test_delete_some_group(app, db):
#    if app.group.count() == 0:
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
#    index = randrange(len(old_groups))
    app.group.delete_group_by_id(group.id)
#    app.group.delete_group_by_index(index)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(group)
#    old_groups[index:index+1] = []
    assert old_groups == new_groups
    if db.check_ui == "true":
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        new_groups = map(clean, db.get_group_list())
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

