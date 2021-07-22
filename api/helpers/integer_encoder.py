import string

from hashids import Hashids

from api.exceptions.decode_exception import DecodeException


# Note: The salt here should ideally be read from a config or environment file that 
# is not committed to a code repository. 
hashid_generator = Hashids(min_length=4, salt='eradicate-the-payday-poverty-cycle')

def encode_number(number_to_encode:int) -> string:
    return hashid_generator.encode(number_to_encode)

def decode_hash(hash:string) -> int:
    decoded_hash = hashid_generator.decode(hash)
    
    if decoded_hash:
        return decoded_hash[0]
    else:
        raise DecodeException()