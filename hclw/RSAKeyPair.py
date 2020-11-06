#!/usr/bin/env python3

from hclw.HCLW import HCLW
from hclw.RSAPrivateKey import RSAPrivateKey
from hclw.RSAPublicKey import RSAPublicKey


class RSAKeyPair:
    def __init__(self, wrapper: HCLW, bits):
        self.wrapper = wrapper
        self.hcl_rsa_key_pair = self.wrapper.hcl_library.GenerateRSAKeyPair(bits)

    def __del__(self):
        self.hcl_library.DeleteRSAKeyPair(self.hcl_rsa_key_pair)

    @property
    def hcl_library(self):
        return self.wrapper.hcl_library

    def create_private_key(self):
        return RSAPrivateKey(self.wrapper, self.hcl_library.GetPrivateKeyFromRSAKeyPair(self.hcl_rsa_key_pair))

    def create_public_key(self):
        return RSAPublicKey(self.wrapper, self.hcl_library.GetPublicKeyFromRSAKeyPair(self.hcl_rsa_key_pair))
