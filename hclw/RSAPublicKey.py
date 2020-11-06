#!/usr/bin/env python3

from hclw.ASecret import ASecret


class RSAPublicKey(ASecret):
    @property
    def owner(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetOwnerFromPublicKey(self.hcl_secret))

    @owner.setter
    def owner(self, owner):
        self.hcl_library.SetPublicKeyOwner(self.hcl_secret, self.wrapper.encode_string(owner))

    def encrypt_message(self, message):
        return self.wrapper.decode_hcl_string(
            self.hcl_library.EncryptMessageWithPublicKey(self.hcl_secret, self.wrapper.encode_string(message)))
