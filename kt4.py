class User:
    count =0
    def __init__(self,name,log,passwd,grade):
        
        self.name = name
        self._log = log
        self._passwd = passwd
        self._grade = grade
        type(self).count += 1

    @property
    def log(self):
        return self._log
    @log.setter
    def log(self,value):
        return print("Невозможно изменить логин!")
    
    @property
    def passwd(self):
        return '*' * len(self._passwd)
    @passwd.setter
    def passwd(self,value):
        self._passwd = value

    @property
    def grade(self):
        return "Неизвестное свойство grade"
    @grade.setter
    def grade(self,value):
        return print("Неизвестное свойство grade")
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade == other._grade
    
    def __bt__ (self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade > other._grade
    
    def __lt__(self, other):
        if not isinstance(other, User):
            return NotImplemented
        return self._grade < other._grade

    def show_info(self):
         print(f'имя: {self.name}, логин: {self.log}')

class SuperUser(User):
    count =0
    def __init__(self, name, log, passwd, role, grade):
        super().__init__(name, log, passwd, grade)
        self.role = role
        
    def show_info(self):
        return super().show_info()



user1 = User('Paul McCartney', 'paul', '1234', 3)
user2 = User('George Harrison', 'george', '5678', 2)
user3 = User('Richard Starkey', 'ringo', '8523', 3)
admin = SuperUser('John Lennon', 'john', '0000', 'admin', 5)

user1.show_info()
admin.show_info()

users = User.count
admins = SuperUser.count

print(f'Всего обычных пользователей: {users}')
print(f'Всего супер-пользователей: {admins}')

print(user1 < user2)
print(admin > user3)
print(user1 == user3)

user3.name = 'Ringo Star'
user1.passwd = 'Pa$$w0rd'

print(user3.name)
print(user1.passwd)
print(user2.log)

user2.log = 'geo'

print(user1.grade)
admin.grade = 10