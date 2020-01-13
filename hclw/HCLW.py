#!/usr/bin/env python3

import ctypes.util


class HCLW:
    def __init__(self, encoding='utf-8'):
        hcl_library_name = ctypes.util.find_library('hcl')
        if hcl_library_name is None:
            raise ModuleNotFoundError('Library HCL (Harpokrat Cryptographic Library) not found')
        self.hcl_library = ctypes.cdll.LoadLibrary(hcl_library_name)
        self.encoding = encoding

    def encode_string(self, string):
        return string.encode(self.encoding)

    def hcl_string_to_char_array(self, hcl_string):
        return self.hcl_library.GetCharArrayFromString(hcl_string)

    def decode_char_array(self, char_array):
        string = ctypes.c_char_p(char_array).value.decode(self.encoding)
        return string

    def decode_hcl_string(self, hcl_string):
        char_array = self.hcl_string_to_char_array(hcl_string)
        string = self.decode_char_array(char_array)
        self.hcl_library.DeleteString(hcl_string)
        return string

    # TODO Move following to clean separated classes
    def get_basic_auth(self, email, password):
        auth = self.hcl_library.GetBasicAuthString(self.encode_string(email), self.encode_string(password))
        return self.decode_hcl_string(auth)
