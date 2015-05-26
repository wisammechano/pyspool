"""
File related methods
"""
import hashlib
import pybitcointools


class File(object):

    """Docstring for File. """

    def __init__(self, filename, testnet=False, **kwargs):
        self.testnet = testnet
        # prefix of the addresses to distinguish between mainnet and testnet
        self._magicbyte = 111 if testnet else 0
        self.file_hash, self.file_hash_metadata = self._calculate_hash(filename, **kwargs)

    @classmethod
    def from_hash(cls, hash):
        cls.hash = hash
        return cls

    def _calculate_hash(self, filename, **kwargs):
        # hash to address
        with open(filename, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if kwargs:
            data = str([unicode(value) for value in kwargs.itervalues()] + [file_hash])
        else:
            data = file_hash
        address_piece_with_metadata = unicode(pybitcointools.bin_to_b58check(pybitcointools.bin_hash160(data),
                                                                             magicbyte=self._magicbyte))
        address_piece = unicode(pybitcointools.bin_to_b58check(pybitcointools.bin_hash160(file_hash),
                                                               magicbyte=self._magicbyte))
        return address_piece, address_piece_with_metadata