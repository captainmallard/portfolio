'''

Diffie-Hellman Key Distribution
AUTHOR: Philip de Castro, 2017

'''
'''
x := exponent
y := base
p := modulus
'''
def keys(x, y, p):
    return y**x%p

def public_power(shared_base, shared_modulus, secret_power):
    #   values of shared base/modulus agreed upon ahead of time
    #   secret power chosen at random.
    #   The result of this function is shared in order to compute the encryption key.
    return keys(secret_power, shared_base, shared_modulus)

def encryption_key(public_power, secret_power, shared_modulus):
    #   compute the encryption key.
    return public_power**secret_power%shared_modulus

print public_power(7, 11, 3)
print encryption_key(4,3,11)