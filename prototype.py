# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

import copy
class Address :
    
    def __init__(self,street_address,town,city):
        self.street_address = street_address 
        self.city = city
        self.town = town
        
    def __str__(self):
        return f'{self.street_address}, {self.town} ,{self.city}'

class Employee :
    
    def __init__(self,name,address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f'{ self.name}, {self.address}'


class EmployeePizzaCompany:
    
    manager_employee = Employee('',Address('123 west side ','','New york'))
    
    cook_employee = Employee('',Address('123 west side ','','New york'))
    
    
    @staticmethod
    def __new_employee(proto, name, town):
        result = copy.deepcopy(proto)
        result.name = name
        result.address.town = town
        return result
    
    
    @staticmethod
    def new_manager_employee(name, town):
        return EmployeePizzaCompany.__new_employee(
            EmployeePizzaCompany.manager_employee, name, town
        )

    @staticmethod
    def new_cook_employee(name, town):
        return EmployeePizzaCompany.__new_employee(
            EmployeePizzaCompany.cook_employee, name, town
        )
        

if __name__ == '__main__':
    # john = EmployeePizzaCompany.new_manager_employee('john','Buffalo')
    # rickka = EmployeePizzaCompany.new_cook_employee('rickka','Utica')
    # bass = EmployeePizzaCompany.new_cook_employee('bass','Binghamton')
    # print(john)
    # print(rickka)
    # print(bass)
    
    john = EmployeePizzaCompany.new_manager_employee('john','Buffalo')
    print(john)
    
    # john = Employee('Bass' , Address(''))
    # john = Employee('Bass' , Address('1234 west side ', 'buffalo' , 'New york'))
    # champ = Employee('Champ' , Address('1234 west side ' , 'Utica' , 'New york'))
    