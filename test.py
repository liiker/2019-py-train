import time


# class ClassRoom:
#     students = []
#     pcs = []

#     def add_studnet(self, student):
#         self.students.append(student)

#     def add_pc(self, pc):
#         self.pcs.append(pc)


# class Student:
#     name = None
#     age = None
#     grade = None

#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade


# class PC:
#     cpu = ''
#     brand = ''
#     ram = ''


# class_room = ClassRoom()
# s1 = Student('adam', 20, '201801')
# s2 = Student('adam1', 22, '201801')

# class_room.add_studnet(s1)

# print(class_room.students[0].name)

class Parking(object):
    cars = []
    orders = []
    max_count = 10

    price = {
        'A': 2,
        'B': 3
    }

    def car_in(self, car):
        self.cars.append(car)
        self.orders.append(Order('0x00001', car))

    def car_out(self, car):
        self.__charge(car)

    def __charge(self, car):
        for o in self.orders:
            if o.car == car:
                o.out_time = time.time()
                ll = o.out_time - o.in_time
                ll = ll / 60 / 60 + 2
                o.fee = self.price.get(car.m_type) * ll
                o.is_pay = True
                return o

        return None


class Order:
    is_pay = False
    car = None
    in_time = ''
    out_time = ''
    fee = 0.0
    code = ''

    def __init__(self, code, car):
        self.code = code
        self.car = car
        self.in_time = time.time()

    def __str__(self):
        return "order : %s , paystatus %s" % (self.code, self.is_pay)


class Car(object):
    number = ''
    m_type = ''

    def __init__(self, number, type):
        self.number = number
        self.m_type = type


pk = Parking()
car = Car('宁A12345', 'A')

pk.car_in(car)

# print(pk.cars[0])
# print(pk.orders[0])

pk.car_out(car)
print(pk.orders[0])
