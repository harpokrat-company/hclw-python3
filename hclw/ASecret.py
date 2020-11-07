#!/usr/bin/env python3

from hclw.HCLW import HCLW


class ASecret:
    def __init__(self, wrapper: HCLW, secret):
        self.wrapper = wrapper
        self.hcl_secret = secret
        self.symmetric = True

    def __del__(self):
        self.hcl_library.DeleteSecret(self.hcl_secret)

    def initialize_asymmetric(self):
        self.symmetric = False
        self.hcl_library.SecretInitializeAsymmetricCipher(self.hcl_secret)

    def initialize_symmetric(self):
        self.symmetric = True
        self.hcl_library.SecretInitializeSymmetricCipher(self.hcl_secret)

    def serialize(self, key):
        if self.symmetric:
            return self.wrapper.decode_hcl_string(
                self.hcl_library.SerializeSecret(self.hcl_secret, self.wrapper.encode_string(key.key)))
        else:
            rsa_key = self.hcl_library.ExtractKeyFromPublicKey(key)
            serialized = self.hcl_library.SerializeSecretAsymmetric(self.hcl_secret, rsa_key)
            self.hcl_library.DeleteRSAKey(rsa_key)
            return serialized

    @property
    def hcl_library(self):
        return self.wrapper.hcl_library

    @property
    def correct_decryption(self):
        return self.hcl_library.CorrectSecretDecryption(self.hcl_secret)
