#!/usr/bin/env python3

import ctypes.util


class HCLW:
    encoding = 'utf-8'

    def __init__(self):
        hcl_library_name = ctypes.util.find_library('hcl')
        if hcl_library_name is None:
            raise ModuleNotFoundError('Library HCL (Harpokrat Cryptographic Library) not found')
        self.hcl_library = ctypes.cdll.LoadLibrary(hcl_library_name)

    def encode_string(self, string):
        return string.encode(self.encoding)

    def decode_string(self, pointer):
        string = ctypes.c_char_p(pointer).value.decode(self.encoding)
        self.hcl_library.ReleaseAllocatedMemory(pointer)
        return string

    def get_basic_auth(self, email, password):
        auth = self.hcl_library.GetBasicAuth(self.encode_string(email), self.encode_string(password))
        return self.decode_string(auth)
