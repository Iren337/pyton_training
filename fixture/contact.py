

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def Create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # init group creation
        wd.find_element_by_link_text("add new").click()
        # fill group form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage_ru)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit group creation
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
            # fill group form
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
        # fill group form
        self.fill_contact_form(new_contact_data)
        self.select_contact_update_button()
        self.app.return_to_home_page()

    def select_contact_update_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form[1]/input[22]").click()

    def select_contact_edit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()


