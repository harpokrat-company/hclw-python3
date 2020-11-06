#!/usr/bin/env python3

from hclw.ASecret import ASecret


class RSAPrivateKey(ASecret):
    @property
    def owner(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetOwnerFromPrivateKey(self.hcl_secret))

    @owner.setter
    def owner(self, owner):
        self.hcl_library.SetPrivateKeyOwner(self.hcl_secret, self.wrapper.encode_string(owner))

    def decrypt_message(self, message):
        return self.wrapper.decode_hcl_string(
            self.hcl_library.DecryptMessageWithPrivateKey(self.hcl_secret, self.wrapper.encode_string(message)))
