#!/usr/bin/env python3

class UserData:
    def __init__(self, ID, name):
        self.ID = ID
        self.Name = name

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.ID,self.Name)

class NewUser(UserData):
    group = 'shiyanlou-louplus'
    @property
    def name(self):
        return self.Name
    @name.setter
    def name(self, value):
        if len(value) > 3:
            self.Name = value
        else:
            print('ERROR')

    def __repr__(self):
        return '{}\' id is {}'.format(self.Name, self.ID)
    @classmethod
    def get_group(cls):
        return cls.group
    @staticmethod
    def format_userdata(id, name):
        return '{0}\'s is {1}'.format(name,id)

if __name__ == '__main__':
    """
    user1 = NewUser(101, 'Jack')
    user1.name = 'Lou'
    user1.name = 'Jackie'
    user2 = NewUser(102, 'Louplus')
    print(user1.name)
    print(user2.name)
    """
    print(NewUser.get_group())
    print(NewUser.format_userdata(109, 'Lucy'))
