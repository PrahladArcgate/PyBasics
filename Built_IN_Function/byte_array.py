# The bytearray() method returns a bytearray object which is an array of the given bytes.

prime_numbers = [2, 3, 5, 7]

# convert list to bytearray
byte_array = bytearray(prime_numbers)
print(byte_array)

# Output: bytearray(b'\x02\x03\x05\x07')