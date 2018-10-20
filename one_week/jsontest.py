#!/usr/bin/env python3

import json

class student(object):
    def __init__(self, _user_id, _name, _pass, _study_time):
        self._user_id = _user_id
        self._name = _name
        self._pass = _pass
        self._study_time = _study_time

    def to_dict(self):
        return {'user_id':self._user_id, 'name':self._name, 'pass':self._pass, 'study_time':self._study_time}

if __name__ == '__main__':
    student1 = student(1000, 'Shiyan', 10, 50)
    student2 = student(2000, 'Lou', 15, 171)
    studentinfo = [student1.__dict__, student2.__dict__]
    #studentinfo = [student1.to_dict(), student2.to_dict()]
    '''
    studentinfo = [{
                     'user_id':1000,
                     'name': 'Shiyan',
                     'pass': 10,
                     'study_time':50,
                  },
                  {
                     'user_id':2000,
                     'name': 'Lou',
                     'pass': 15,
                     'study_time':171,
                  }]
    '''
    with open('/tmp/jsontest.json', 'w') as f:
        json.dump(studentinfo, f)
