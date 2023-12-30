
import my_secure
my_secure.secure_name('김철수')
my_secure.secure_no('991216-1234567')
my_secure.secure_phone('010-1234-5678')

print()

from my_secure import secure_name as f1, secure_no as f2, secure_phone as f3
f1('김철수')
f2('991216-1234567')
f3('010-1234-5678')
