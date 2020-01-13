#!/usr/bin/env python3

from hclw.HCLW import HCLW


class Secret:
    def __init__(self, wrapper: HCLW, content):
        self.wrapper = wrapper
        self.hcl_secret = self.wrapper.hcl_library.GetSecretFromContent(self.wrapper.encode_string(content))

    def __del__(self):
        self.hcl_library.DeleteSecret(self.hcl_secret)

    def get_raw_content(self):
        return self.wrapper.decode_hcl_string(self.hcl_library.GetContentStringFromSecret(self.hcl_secret))

    @property
    def hcl_library(self):
        return self.wrapper.hcl_library

    @property
    def name(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetNameFromSecret(self.hcl_secret))

    @name.setter
    def name(self, name):
        self.hcl_library.UpdateSecretName(self.hcl_secret, self.wrapper.encode_string(name))

    @property
    def login(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetLoginFromSecret(self.hcl_secret))

    @login.setter
    def login(self, login):
        self.hcl_library.UpdateSecretLogin(self.hcl_secret, self.wrapper.encode_string(login))

    @property
    def password(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetPasswordFromSecret(self.hcl_secret))

    @password.setter
    def password(self, password):
        self.hcl_library.UpdateSecretPassword(self.hcl_secret, self.wrapper.encode_string(password))

    @property
    def domain(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetDomainFromSecret(self.hcl_secret))

    @domain.setter
    def domain(self, domain):
        self.hcl_library.UpdateSecretDomain(self.hcl_secret, self.wrapper.encode_string(domain))
