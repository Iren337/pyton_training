

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def Create(self, contact):
        wd = self.app.wd
        self.app.return_to_home_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.app.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contract
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def fill_contact_form(self, contact):
            wd = self.app.wd
            # fill contact form
            self.change_field_value("firstname", contact.firstname)
            self.change_field_value("middlename", contact.middlename)
            self.change_field_value("lastname", contact.lastname)
            self.change_field_value("nickname", contact.nickname)
            self.change_field_value("title", contact.title)
            self.change_field_value("company", contact.company)
            self.change_field_value("address", contact.address)
            self.change_field_value("home", contact.home_phone)
            self.change_field_value("mobile", contact.mobile)
            self.change_field_value("work", contact.work_phone)
            self.change_field_value("fax", contact.fax)
            self.change_field_value("email", contact.email)
            self.change_field_value("email2", contact.email2)
            self.change_field_value("email3", contact.email3)
            self.change_field_value("homepage", contact.homepage_ru)
            self.change_field_value("byear", contact.byear)
            self.change_field_value("ayear", contact.ayear)
            self.change_field_value("address2", contact.address2)
            self.change_field_value("phone2", contact.phone2)
            self.change_field_value("notes", contact.notes)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_edit_button()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        self.select_contact_update_button()
        self.app.return_to_home_page()

    def select_contact_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def select_contact_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))


