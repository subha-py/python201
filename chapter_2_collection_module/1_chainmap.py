from collections import ChainMap

car_parts = dict(hood=500, engine=5000, front_door=750)
car_options = {'A/C': 1000, 'Turbo': 2500, 'rollbar': 300}
car_accessories = dict(cover=100, hood_ornament=150, seat_cover=99)
car_pricing = ChainMap(car_parts, car_options, car_accessories)
print(car_pricing['hood'])
