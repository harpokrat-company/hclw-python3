#!/usr/bin/env python3

import ctypes.util


class HCLW:
    def __init__(self, encoding='utf-8'):
        hcl_library_name = ctypes.util.find_library('hcl')
        if hcl_library_name is None:
            raise ModuleNotFoundError('Library HCL (Harpokrat Cryptographic Library) not found')
        self.hcl_library = ctypes.cdll.LoadLibrary(hcl_library_name)
        self.initialize_api_types()
        self.encoding = encoding

    def initialize_api_types(self):
        # TODO Simpler type initialization/declaration (ex: split into static methods in classes)
        # Common functions
        self.hcl_library.GetBasicAuthString.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.hcl_library.GetBasicAuthString.restype = ctypes.c_void_p
        self.hcl_library.GetDerivedKey.argtypes = [ctypes.c_char_p]
        self.hcl_library.GetDerivedKey.restype = ctypes.c_void_p
        self.hcl_library.GetCharArrayFromString.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetCharArrayFromString.restype = ctypes.c_char_p
        self.hcl_library.DeleteString.argtypes = [ctypes.c_void_p]
        self.hcl_library.DeleteString.restype = None
        # Secret functions
        self.hcl_library.GetSecretFromContent.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        self.hcl_library.GetSecretFromContent.restype = ctypes.c_void_p
        self.hcl_library.CreateSecret.argtypes = []
        self.hcl_library.CreateSecret.restype = ctypes.c_void_p
        self.hcl_library.CorrectSecretDecryption.argtypes = [ctypes.c_void_p]
        self.hcl_library.CorrectSecretDecryption.restype = ctypes.c_bool
        self.hcl_library.GetNameFromSecret.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetNameFromSecret.restype = ctypes.c_char_p
        self.hcl_library.GetLoginFromSecret.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetLoginFromSecret.restype = ctypes.c_char_p
        self.hcl_library.GetPasswordFromSecret.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetPasswordFromSecret.restype = ctypes.c_char_p
        self.hcl_library.GetDomainFromSecret.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetDomainFromSecret.restype = ctypes.c_char_p
        self.hcl_library.UpdateSecretName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateSecretLogin.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateSecretPassword.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateSecretDomain.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.GetContentStringFromSecret.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.GetContentStringFromSecret.restype = ctypes.c_void_p
        self.hcl_library.DeleteSecret.argtypes = [ctypes.c_void_p]
        # User functions
        self.hcl_library.CreateUser.argtypes = [ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_char_p]
        self.hcl_library.CreateUser.restype = ctypes.c_void_p
        self.hcl_library.GetEmailFromUser.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetEmailFromUser.restype = ctypes.c_char_p
        self.hcl_library.GetPasswordFromUser.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetPasswordFromUser.restype = ctypes.c_char_p
        self.hcl_library.GetFirstNameFromUser.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetFirstNameFromUser.restype = ctypes.c_char_p
        self.hcl_library.GetLastNameFromUser.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetLastNameFromUser.restype = ctypes.c_char_p
        self.hcl_library.UpdateUserEmail.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateUserPassword.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateUserFirstName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdateUserLastName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.DeleteUser.argtypes = [ctypes.c_void_p]

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

    def get_derived_key(self, password):
        auth = self.hcl_library.GetDerivedKey(self.encode_string(password))
        return self.decode_hcl_string(auth)
