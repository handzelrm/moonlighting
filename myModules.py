# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 11:30:54 2016

@author: Rober
"""
import re

class narcotic(object):
    """Class for creating a narcotic object
    
    Attributes:
        name: Medication name
        route: Route of administration
        dose: numeric dose
        units: units of dose
    """    
    
    def __init__(self,name,route,dose,units,timing):
        self.name = name
        self.route = route
        self.dose = dose
        self.units = units
        self.timing = timing
        self.morphine_eq = self.morphine_eq()              

    def morphine_eq(self):
        #morphine
        if self.name == 'MORPHINE':
            if self.route == 'ORAL':
                return unit_conversion(self.dose,self.units)
            elif self.route == 'IT':
                return 0
            elif self.route == 'IV':
                return 3*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Morphine route not found')
        #Oxymorphone
        elif self.name == 'OXYMORPHONE':
            if self.route == 'ORAL':
                return 3*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Oxymorphone route not found')
        #Hydromorphone        
        elif self.name == 'HYDROMORPHONE':
            if self.route == 'ORAL':
                return 3*unit_conversion(self.dose,self.units)
            elif self.route == 'IT':
                return 0
            elif self.route == 'IV':
                return 20*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Hydromorphone route not found')
        #Fentanyl
        elif self.name == 'FENTANYL':
            if self.route == 'IV':
                return 300*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Fentanyl route not found')
        #Oxycodone
        elif self.name == 'OXYCODONE':
            if self.route == 'ORAL':
                return 1.5*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Oxycodone route not found')
        #Percocet
        elif self.name == 'ACETAMINOPHEN_OXYCODONE':
            if self.route == 'ORAL':
                return 1.5*unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Percocet route not found')
        #Norco
        elif self.name == 'ACETAMINOPHEN_HYDROCODONE':
            if self.route == 'ORAL':
                return unit_conversion(self.dose,self.units)
            else:
                raise TypeError('Norco route not found')
        #Medication Error
        else:
            print(self.name)
            raise TypeError('Medication name not found')
            
def unit_conversion(dose,units):
    if units == 'mg' or units == 'mL': 
        return dose
    elif units == 'mcg':
        return dose/1000
    elif units == 'tab':
        return dose*5
    else:
        raise TypeError('Units not found')                 
            
            
class File(object):
    """Creates file object
    
    Attributes:
        path: path of file
        file: file name
        extension: file extension
    
    Methods:
        full_name(self): returns full path/file.extension
    """
    
    sheet = None
    
    
    def __init__(self,path,name,extension):
        self.path = path
        self.name = name.replace('\\','/')
        self.extension = extension
            
    def __repr__(self):
        return "File('{}', '{}', '{}')".format(self.path,self.name,self.extension)
    
    def __str__(self):
        return self.fullname
    
    def add_sheet(self,sheet):
        self.sheet = sheet
        
    @property
    def fullname(self):
        if self.extension.find('.') == -1:
            return '{}{}.{}'.format(self.path,self.name,self.extension)
        else:
            return '{}{}{}'.format(self.path,self.name,self.extension)
    
    @classmethod
    def from_fullstring(cls, fullstring):
        fullstring = fullstring.replace('\\','/')
        regex = re.search(r'(.+/)(.+)(\..+)',fullstring)
        path = regex.group(1)
        name = regex.group(2)
        extension = regex.group(3)
        return cls(path,name,extension) 
 
            
class Call(object):
    """Class for call schedule. It calls on Day class to first create
    a Day object and then used this object to create a call object.
    
    Attributes:
        name: Name of the call
        sun: day object
        mon: day object
        etc
    """        
    
    def __init__(self,name,start,end):
        self.name = name
        self.sun = Day(start,end)
        self.mon = Day(start,end)
        self.tue = Day(start,end)
        self.wed = Day(start,end)
        self.thu = Day(start,end)
        self.fri = Day(start,end)
        self.sat = Day(start,end)
        
    def weekday(self,weekday):
        if weekday == 'Sun':
            return self.sun
        elif weekday == 'Mon':
            return self.mon
        elif weekday == 'Tue':
            return self.tue
        elif weekday == 'Wed':
            return self.wed
        elif weekday == 'Thu':
            return self.thu
        elif weekday == 'Fri':
            return self.fri
        elif weekday == 'Sat':
            return self.sat
        else:
            raise AttributeError('Issue with start_time')

class Day(object):
    """Class for call schedule
    
    Attributes:
        start: start time
        end: end time
        
    Methods:
        updateCall(self,start,end): updates a datetime for a Day object
    """  
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def updateCall(self,start,end):
        """updates call time"""
        self.start = start
        self.end = end 

        
class Staff(object):
    """Creates an abstract base class
    
    Attributes:
        first_name: first name
        last_name: last name
        postition: position ie resident
        upmc_email: upmc email
    """

    gmail = None
    year = None
    
    
    def __init__(self,first_name,last_name,upmc_email):
        self.first_name = first_name
        self.last_name = last_name
        self.upmc_email = upmc_email
    
    def __repr__(self):
        return "Staff('{}', '{}', '{}')".format(self.first_name,self.last_name,self.upmc_email)
    
    def __str__(self):
        return '{} {}'.format(self.first_name,self.last_name)
        
    @staticmethod
    def find_lastname(object_list,lname):
        for staff in object_list:
            if staff.last_name == lname:
                return staff
        
    
class Resident(Staff):
    """Creates an abstract base class
    
    Attributes:
        first_name: first name
        last_name: last name
        postition: position ie resident
        upmc_email: upmc email
    """
    
    
    
    def __init__(self,first_name,last_name,upmc_email,year,daysoff=None,number_of_calls=None): 
        super().__init__(first_name,last_name,upmc_email)
        self.position = 'Resident'
        self.year = year
        self.daysoff = []
        
    def __repr__(self):
        return "Staff('{}', '{}', '{}' {})".format(self.first_name,self.last_name,self.upmc_email,self.year)

    def add_dayoff(self,date):
        self.daysoff.append(date)
        
    def number_of_calls(self,number_of_calls):
        self.number_of_calls = number_of_calls
        

class Resident_Call(object):
    """Creates an abstract base class
    
    Attributes:
        
    """    
    
    def __init__(self,name,daysoff=None,number_of_calls=None,calls=None): 
        self.name = name
        self.daysoff = []
        
    def __repr__(self):
        return '{}'.format(self.name)
    
    def __str__(self):
        return '{}'.format(self.name)
        
    def add_dayoff(self,date):
        self.daysoff.append(date)
        
    def number_of_calls(self,number_of_calls):
        self.number_of_calls = number_of_calls
        
    def assign_call(self,date):
        self.calls.append(date)
        
class Service_Call(object):
    
    def __init__(self,name,uncovered_days=None,covered_days=None):
        self.name = name
        self.uncovered_days = []
        self.covered_days = []
    
    def __repr__(self):
        return '{}'.format(self.name)
    
    def __str__(self):
        return '{}'.format(self.name)    
        
    def add_uncovered(self,date):
        self.uncovered_days.append(date)
        
    def rm_uncovered(self,date):
        self.uncovered_days.remove(date)
        
    def add_covered(self,date):
        self.covered_days.append(date)
        
    def rm_covered(self,date):
        self.covered_days.remove(date)
        





