#Task -  Convert the following integer back into a message
#BASE - 10
#import required module
from Crypto.Util.number import *
cipher = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

#From base10 to bytes
print(long_to_bytes(cipher))

#From bytes to base10
#print(bytes_to_long(b"crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"))
#flag = b"crypto{3nc0d1n6_4ll_7h3_w4y_d0wn}"
