#!/usr/bin/env python3

from hclw.HCLW import HCLW
from hclw.ASecret import ASecret


class Password(ASecret):
    def __init__(self, wrapper: HCLW, secret=None):
        ASecret.__init__(self, wrapper, secret=(secret if secret is not None else wrapper.hcl_library.CreatePassword()))

    @property
    def name(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetNameFromPassword(self.hcl_secret))

    @name.setter
    def name(self, name):
        self.hcl_library.UpdatePasswordName(self.hcl_secret, self.wrapper.encode_string(name))

    @property
    def login(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetLoginFromPassword(self.hcl_secret))

    @login.setter
    def login(self, login):
        self.hcl_library.UpdatePasswordLogin(self.hcl_secret, self.wrapper.encode_string(login))

    @property
    def password(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetPasswordFromPassword(self.hcl_secret))

    @password.setter
    def password(self, password):
        self.hcl_library.UpdatePasswordPassword(self.hcl_secret, self.wrapper.encode_string(password))

    @property
    def domain(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetDomainFromPassword(self.hcl_secret))

    @domain.setter
    def domain(self, domain):
        self.hcl_library.UpdatePasswordDomain(self.hcl_secret, self.wrapper.encode_string(domain))
