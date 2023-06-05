import string

import random

def passwd( size=8, chars=string.ascii_letters + string.digits + string.punctuation ):
    return ''.join( random.choice(chars) for _ in range(size) )
print(passwd(int(input( "how many caracters in your password?" ))))
