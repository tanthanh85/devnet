from ncclient import manager
from connection_info import *



with manager.connect(**R1) as m1:
    reply = m1.get_config('running')
    print(reply)



# try:
#     with manager.connect(**R2) as m2:
#         print(m2)
# except:
#     print('Something went wrong')