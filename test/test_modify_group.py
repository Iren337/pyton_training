from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first_group(Group(name="222"))


def test_modify_group_header(app):
    app.group.modify_first_group(Group(header="2222"))


def test_modify_group_footer(app):
    app.group.modify_first_group(Group(footer="22222"))
