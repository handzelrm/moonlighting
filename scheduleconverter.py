import pandas as pd
import datetime
import argparse

class Resident():
    def __init__(self,name_first,name_last,email_work):
        self.name_first = name_first
        self.name_last = name_last
        self.email_work = email_work

class Service():
    def __init__(self,start=datetime.time(18,0),end=datetime.time(6,0)):
        # self.name = name
        self.start = start
        self.end = end
        self.mon = {'start':self.start,'end':self.end}
        self.tue = {'start':self.start,'end':self.end}
        self.wed = {'start':self.start,'end':self.end}
        self.thu = {'start':self.start,'end':self.end}
        self.fri = {'start':self.start,'end':self.end}
        self.sat = {'start':self.start,'end':self.end}
        self.sun = {'start':self.start,'end':self.end}

class GenerateIcals():
    def __init__(self,send=False):
        self.df = pd.read_excel('./February 2018 Moonlighting Final.xlsm')
        self.load_residents()
        self.load_services()
        self.test()

    def load_residents(self):
        self.Griepentrog = Resident('John', 'Griepentrog','griepentrogje@upmc.edu')
        self.Handzel = Resident('Robert', 'Handzel','handzelrm@upmc.edu')
        self.Okolo = Resident('Frances','Okolo','okolofc@upmc.edu')
        self.Siow = Resident('Shaun','Siow','siowv@upmc.edu')
        self.Tam = Resident('Vernissia','Tam','tamvw@upmc.edu')
        self.Vanderwindt = Resident('Dirk','Van Der Windt','vanderwindtd@upmc.edu')
        self.Yeh = Resident('Andrew','Yeh','yeha@upmc.edu')
        self.Cyr = Resident('Anthony','Cyr','cyrar@upmc.edu')
        self.Dadashzadeh = Resident('Esmaeel','Dadashzadeh','dadashzadeher@upmc.edu')
        self.Gallagher = Resident('James','Gallagher','gallagherjw@upmc.edu')
        self.Huckaby = Resident('Lauren','Huckaby','huckabylv@upmc.edu')
        self.Kulkarni = Resident('Shreyus','Kulkarni','kulkarniss@upmc.edu')
        self.Myers = Resident('Sara','Myers','myerssp@upmc.edu')
        self.Nicholson = Resident('Kristina','Nicholson','nicholsonkj@upmc.edu')
        self.Egro = Resident('Francesco','Egro','egrofm@upmc.edu')
        self.Yecies = Resident('Todd','Yecies','yeciest@upmc.edu')
        self.Beidas = Resident('Omar', 'Beidas', 'beidaso@upmc.edu')
        self.Hugar = Resident('Hugar', '_', '_')

    def load_services(self):
        self.Trauma = Service(datetime.time(18,0),datetime.time(7,30))
        self.CT = Service()
        self.CT.fri['end'] = datetime.time(7,0)
        self.CT.sat = {'start':datetime.time(13,0),'end':datetime.time(7,0)}
        self.CT.sun['start'] = datetime.time(13,0)
        self.CHP_Sr = Service()
        self.CHP_Jr = Service()
        self.SHY = Service()

    def test(self):
        for col in self.df.columns:
            try:
                current_match = self.__getattribute__(col)
                if Resident.__instancecheck__(current_match):
                    
            except AttributeError:
                pass



def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument('file',help='Path to excel schedule', type=str)
    parser.add_argument('-s','--send', help='Sends out emails', action='store_true')
    args = parser.parse_args()
    GenerateIcals(args.send)




if __name__ == '__main__':
    main()
