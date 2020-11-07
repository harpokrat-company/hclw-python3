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
        # RSAKeyPair functions
        self.hcl_library.GenerateRSAKeyPair.argtypes = [ctypes.c_int64]
        self.hcl_library.GenerateRSAKeyPair.restype = ctypes.c_void_p
        self.hcl_library.GetPublicKeyFromRSAKeyPair.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetPublicKeyFromRSAKeyPair.restype = ctypes.c_void_p
        self.hcl_library.GetPrivateKeyFromRSAKeyPair.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetPrivateKeyFromRSAKeyPair.restype = ctypes.c_void_p
        self.hcl_library.DeleteRSAKeyPair.argtypes = [ctypes.c_void_p]
        # ASecret functions
        self.hcl_library.DeserializeSecret.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.DeserializeSecret.restype = ctypes.c_void_p
        self.hcl_library.SerializeSecret.argtypes = [ctypes.c_void_p, ctypes.c_void_p]
        self.hcl_library.SerializeSecret.restype = ctypes.c_void_p
        self.hcl_library.GetSecretCorrectDecryption.argtypes = []
        self.hcl_library.GetSecretCorrectDecryption.restype = ctypes.c_bool
        self.hcl_library.SecretInitializeAsymmetricCipher.argtypes = []
        self.hcl_library.SecretInitializeSymmetricCipher.argtypes = []
        self.hcl_library.GetSecretTypeName.argtypes = []
        self.hcl_library.GetSecretTypeName.restype = ctypes.c_void_p
        self.hcl_library.DeleteSecret.argtypes = [ctypes.c_void_p]
        # Password functions
        self.hcl_library.CreatePassword.argtypes = []
        self.hcl_library.CreatePassword.restype = ctypes.c_void_p
        self.hcl_library.GetNameFromPassword.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetNameFromPassword.restype = ctypes.c_char_p
        self.hcl_library.GetLoginFromPassword.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetLoginFromPassword.restype = ctypes.c_char_p
        self.hcl_library.GetPasswordFromPassword.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetPasswordFromPassword.restype = ctypes.c_char_p
        self.hcl_library.GetDomainFromPassword.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetDomainFromPassword.restype = ctypes.c_char_p
        self.hcl_library.UpdatePasswordName.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdatePasswordLogin.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdatePasswordPassword.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.UpdatePasswordDomain.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        # RSAPrivateKey functions
        self.hcl_library.GetOwnerFromPrivateKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetOwnerFromPrivateKey.restype = ctypes.c_char_p
        self.hcl_library.SetPrivateKeyOwner.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.DecryptMessageWithPrivateKey.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.DecryptMessageWithPrivateKey.restype = ctypes.c_void_p
        self.hcl_library.ExtractKeyFromPrivateKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.ExtractKeyFromPrivateKey.restype = ctypes.c_void_p
        # RSAPublicKey functions
        self.hcl_library.GetOwnerFromPublicKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetOwnerFromPublicKey.restype = ctypes.c_char_p
        self.hcl_library.SetPublicKeyOwner.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.EncryptMessageWithPublicKey.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.EncryptMessageWithPublicKey.restype = ctypes.c_void_p
        self.hcl_library.ExtractKeyFromPublicKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.ExtractKeyFromPublicKey.restype = ctypes.c_void_p
        # SymmetricKey functions
        self.hcl_library.CreateSymmetricKey.argtypes = []
        self.hcl_library.CreateSymmetricKey.restype = ctypes.c_void_p
        self.hcl_library.GetOwnerFromSymmetricKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetOwnerFromSymmetricKey.restype = ctypes.c_char_p
        self.hcl_library.SetSymmetricKeyOwner.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        self.hcl_library.GetKeyFromSymmetricKey.argtypes = [ctypes.c_void_p]
        self.hcl_library.GetKeyFromSymmetricKey.restype = ctypes.c_char_p
        self.hcl_library.SetSymmetricKeyKey.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        # RSAKey functions
        self.hcl_library.DeleteRSAKey.argtypes = [ctypes.c_void_p]

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

    def deserialize_secret(self, key, serialized_content):
        return self.hcl_library.DeserializeSecret(self.encode_string(key.key), self.encode_string(serialized_content))

    def deserialize_secret_asymmetric(self, key, serialized_content):
        rsa_key = self.hcl_library.ExtractKeyFromPrivateKey(key)
        secret = self.hcl_library.DeserializeSecretAsymmetric(rsa_key, self.encode_string(serialized_content))
        self.hcl_library.DeleteRSAKey(rsa_key)
        return secret

    def correct_secret_decryption(self, secret):
        return self.hcl_library.CorrectSecretDecryption(secret)

    def get_secret_type_name(self, secret):
        return self.decode_hcl_string(self.hcl_library.GetSecretTypeName(secret))
