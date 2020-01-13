#!/usr/bin/env python3

from hclw.HCLW import HCLW


class User:
    def __init__(self, wrapper: HCLW, email: str, password: str, first_name: str, last_name: str):
        self.wrapper = wrapper
        self.hcl_user = self.wrapper.hcl_library.CreateUser(
            self.wrapper.encode_string(email),
            self.wrapper.encode_string(password),
            self.wrapper.encode_string(first_name),
            self.wrapper.encode_string(last_name)
        )

    def __del__(self):
        self.hcl_library.DeleteUser(self.hcl_user)

    @property
    def hcl_library(self):
        return self.wrapper.hcl_library

    @property
    def email(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetEmailFromUser(self.hcl_user))

    @email.setter
    def email(self, email):
        self.hcl_library.UpdateUserEmail(self.hcl_user, self.wrapper.encode_string(email))

    @property
    def password(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetPasswordFromUser(self.hcl_user))

    @password.setter
    def password(self, password):
        self.hcl_library.UpdateUserPassword(self.hcl_user, self.wrapper.encode_string(password))

    @property
    def first_name(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetFirstNameFromUser(self.hcl_user))

    @first_name.setter
    def first_name(self, first_name):
        self.hcl_library.UpdateUserFirstName(self.hcl_user, self.wrapper.encode_string(first_name))

    @property
    def last_name(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetLastNameFromUser(self.hcl_user))

    @last_name.setter
    def last_name(self, last_name):
        self.hcl_library.UpdateUserLastName(self.hcl_user, self.wrapper.encode_string(last_name))
