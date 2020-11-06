#!/usr/bin/env python3

from hclw.HCLW import HCLW
from hclw.ASecret import ASecret


class SymmetricKey(ASecret):
    def __init__(self, wrapper: HCLW, secret=None):
        ASecret.__init__(self, wrapper, secret=(secret if secret is not None else wrapper.hcl_library.CreateSymmetricKey()))

    @property
    def owner(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetOwnerFromSymmetricKey(self.hcl_secret))

    @owner.setter
    def owner(self, owner):
        self.hcl_library.SetSymmetricKeyOwner(self.hcl_secret, self.wrapper.encode_string(owner))

    @property
    def key(self):
        return self.wrapper.decode_char_array(self.hcl_library.GetKeyFromSymmetricKey(self.hcl_secret))

    @key.setter
    def key(self, key):
        self.hcl_library.SetSymmetricKeyKey(self.hcl_secret, self.wrapper.encode_string(key))
