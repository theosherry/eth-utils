from typing import Union


from .conversions import to_bytes


def keccak(
    primitive: Union[bytes, int, bool] = None, hexstr: str = None, text: str = None
) -> bytes:
    raise NotImplementedError('Removed to avoid circular reference. Use eth-hash directly'.)
