from collections import namedtuple

# programmers use it like a struct
Parts = namedtuple('Parts', 'id_num desc cost amount')
auto_parts = Parts(id_num=1234, cost=1200.00, amount=10, desc='Ford Engine')
print(auto_parts.id_num)