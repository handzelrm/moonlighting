from icalendar import Calendar, Event #used to create icalendar files
import re
import datetime #used to create datetime objects
import pytz
import calendar #used to get how many days in month
import win32com.client as win32 #used to use local outlook program to send email
import myModules
import pandas as pd
import numpy as np
import pickle
import os

def find_path(file):
    if os.path.isfile('C:/Users/Rober/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/call/'+file):
        path = 'C:/Users/Rober/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/call/'
    elif os.path.isfile('I:/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/call/'+file):
        path =  'I:/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/call/'
    elif os.path.isfile('I:/Google Drive/GitHub/moonlighting/'+file):
        path = 'I:/Google Drive/GitHub/moonlighting/'
    elif os.path.isfile('C:/Users/Rober/Google Drive/GitHub/moonlighting/'+file):
        path = 'C:/Users/Rober/Google Drive/GitHub/moonlighting/'
    else:
        print('Error - no file found in any directories')
        path = None
    return path

#function defines values, loads schedule data, and pickles all of it
def pickle_data(path,file):
    # path_desktop = 'I:/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/'
    # path_laptop = 'C:/Users/Rober/Google Drive/Python/WinPython-64bit-3.4.4.3Qt5/settings/.spyder-py3/'

    if not os.path.isdir(path+'pickles/'):
        os.makedirs(path+'pickles/')

    df = pd.read_excel(path+file,sheetname='Master')
    pd.to_pickle(df,path+'pickles/'+'call_schedule.pickle')

    #creates objects for each service
    trauma = myModules.Call('Trauma',datetime.time(18,30),datetime.time(7,30))
    ct = myModules.Call('CT',datetime.time(18,0),datetime.time(6,0))
    ct.fri = myModules.Day(datetime.time(18,0),datetime.time(7,0))
    ct.sat = myModules.Day(datetime.time(13,0),datetime.time(7,0))
    ct.sun = myModules.Day(datetime.time(13,0),datetime.time(6,0))
    chp_sr = myModules.Call('CHP Sr.',datetime.time(18,0),datetime.time(6,0))
    chp_jr = myModules.Call('CHP Jr.',datetime.time(18,0),datetime.time(6,0))
    shy = myModules.Call('SHY',datetime.time(18,0),datetime.time(6,0))
    transplant = myModules.Call('Transplant',datetime.time(18,0),datetime.time(6,0))
    six_fg = myModules.Call('6FG',datetime.time(16,0),datetime.time(6,0))
    vasc = myModules.Call('VASC',datetime.time(18,00),datetime.time(14,00))

    #creates dictionary of all service objects
    callTimes = {'Trauma':trauma,'CT':ct, 'CHP Sr.':chp_sr, 'CHP Jr.':chp_jr,
                 'SHY':shy, 'Transplant':transplant, '6FG':six_fg, 'VASC':vasc}

    with open(path+'pickles/'+'callTimes.pickle','wb') as f:
        pickle.dump(callTimes,f)

    #creates resident objects
    griepentrog = myModules.Resident('John', 'Griepentrog','griepentrogje@upmc.edu',4)
    handzel = myModules.Resident('Robert', 'Handzel','handzelrm@upmc.edu',4)
    okolo = myModules.Resident('Frances','Okolo','okolofc@upmc.edu',4)
    siow = myModules.Resident('Shaun','Siow','siowv@upmc.edu',4)
    tam = myModules.Resident('Vernissia','Tam','tamvw@upmc.edu',4)
    vanderwindt = myModules.Resident('Dirk','Van Der Windt','vanderwindtd@upmc.edu',5)
    yeh = myModules.Resident('Andrew','Yeh','yeha@upmc.edu',5)
    dyer = myModules.Resident('Mitchell','Dyer','dyermr@upmc.edu',5)
    cyr = myModules.Resident('Anthony','Cyr','cyrar@upmc.edu',4)
    dadashzadeh = myModules.Resident('Esmaeel','Dadashzadeh','dadashzadeher@upmc.edu',4)
    gallagher = myModules.Resident('James','Gallagher','gallagherjw@upmc.edu',4)
    huckaby = myModules.Resident('Lauren','Huckaby','huckabylv@upmc.edu',4)
    kulkarni = myModules.Resident('Shreyus','Kulkarni','kulkarniss@upmc.edu',4)
    myers = myModules.Resident('Sara','Myers','myerssp@upmc.edu',4)
    nicholson = myModules.Resident('Kristina','Nicholson','nicholsonkj@upmc.edu',4)
    egro = myModules.Resident('Francesco','Egro','egrofm@upmc.edu',4)
    yecies = myModules.Resident('Todd','Yecies','yeciest@upmc.edu',4)
    beidas = myModules.Resident('Omar', 'Beidas', 'beidaso@upmc.edu',4)
    hugar = myModules.Resident('Hugar', '_', '_', 5)

    # berkey = myModules.Resident('Sara','Berkey','berkeyse@upmc.edu',5)
    # cunningham = myModules.Resident('Kellie','Cunningham','cunninghamke@upmc.edu',6)

    # goswami = myModules.Resident('Julie','Goswami','goswamij@upmc.edu',5)
    # kirk = myModules.Resident('Katherine','Hill (Kirk)','kirkka@upmc.edu',4)
    # kowalsky = myModules.Resident('Stacy','Kowalsky','kowalskysj@upmc.edu',5)
    # leeper = myModules.Resident('Christine','Leeper','leepercm@upmc.edu',6)
    # lewis = myModules.Resident('Anthony','Lewis','lewisaj@upmc.edu',6)
    # torres = myModules.Resident('Crisanto','Torres','torrescm@upmc.edu',5)
    # uy = myModules.Resident('Jamie','Uy','uyjt@upmc.edu',4)
    # chen = myModules.Resident('Wendy','Chen','chenw2@upmc.edu',4)
    # schusterman = myModules.Resident('Ash','Schusterman','schustermanma@upmc.edu',4)
    # browning = myModules.Resident('Jeff','Browning','browningjd@upmc.edu',4)
    # theisen = myModules.Resident('Katie', 'Theisen','theisenkm@upmc.edu',4)
    # shaffiey = myModules.Resident('Shahab','Shaffiey','shaffieysa@upmc.edu',7)
    # mcdonald = myModules.Resident('KerryAnn','McDonald','stewartkc@upmc.edu',7)


    residents = [dyer,griepentrog,handzel,okolo,siow,tam,vanderwindt,yeh,cyr,dadashzadeh,gallagher,huckaby,kulkarni,myers,nicholson,egro,yecies,beidas,hugar]

    #kirk,kowalsky,leeper,lewis,berkey,cunningham,goswami,torres,uy,chen,schusterman,browning,theisen,shaffiey,mcdonald,

    with open(path+'pickles/'+'residents.pickle','wb') as f:
        pickle.dump(residents,f)

    #may be able to replace with a fxn at some point but works for now
    month = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
    with open(path+'pickles/'+'month.pickle','wb') as f:
        pickle.dump(month,f)

    services = ['Trauma','SHY','CHP Sr.', 'CHP Jr.','CT','6FG','VASC']
    with open(path+'pickles/'+'services.pickle','wb') as f:
        pickle.dump(services,f)

"""
createCalendar is a function which takes inputs of a calendar object, the event name
the start time and the end time and will add that event to the calendar object. This
can be called multiple times to add more events to a calendar object before it is
saved as a file.
    Last modified 10/28
"""
def createCalendar(cal,eventName,datetimeStart,datetimeEnd):
    if not cal.has_key('version'): #checks to see if it is a new file and needs these lines.
        cal.add('prodid', '-//My calendar product//mxm.dk//') #standard lines
        cal.add('version', '2.0') #standard lines
    event = Event() #creates a new event object
    event.add('summary', eventName) #adds the summary or title to the new event
    event.add('dtstart', datetimeStart) #adds start time
    event.add('dtend', datetimeEnd) #adds end time
    cal.add_component(event) #adds event to the calendar object
    return cal #returns the object
    #year, month, day, hour, min, sec, microsec


def resident_ical(path, file, send=False):
    #loads call schedule as pandas df
    df = pd.read_pickle(path+'pickles/'+'call_schedule.pickle')

    #loads call times from pickle
    with open(path+'pickles/'+'callTimes.pickle','rb') as f:
        callTimes = pickle.load(f)

    #loads residents list of objects from pickle
    with open(path+'pickles/'+'residents.pickle','rb') as f:
        residents = pickle.load(f)

    #loads services dictionary from pickle
    with open(path+'pickles/'+'services.pickle','rb') as f:
        services = pickle.load(f)

    #loads month dictionary from pickle
    with open(path+'pickles/'+'month.pickle','rb') as f:
        month = pickle.load(f)

    regex = re.search(r'(\w+) (\d+) .*Moonlighting',file)
    month_str = regex.group(1)
    month = month[month_str]
    year = int(regex.group(2))

    if not os.path.isdir(path+'resident icals/'):
        os.makedirs(path+'resident icals/')
    if not os.path.isdir(path+'resident icals/'+month_str+'/'):
        os.makedirs(path+'resident icals/'+month_str+'/')

    res_lastname_list = ['Date'] #need date in each df below
    #loops through each resident
    for res in residents:
        #checks to see if resident is on the schedule
        if res.last_name in df.columns:
            res_lastname_list.append(res.last_name) #adds them to inclusion list
    df = df[res_lastname_list] #removes all residents not on schedule
    #loops through residents
    for res in df.columns:
        if res != 'Date':
            cal = Calendar() #creates calendar file
            df_res = df[['Date',res]][df[res].isin(services)] #defines resident specific df. removes any rows that do not have a service listed in the cell
            #loops through each row
            for row in df_res.iterrows():
                curDay = int(row[1].values[0]) #gest current integer of day value
                curService = row[1].values[1] #gets the value of the resident assigned that call

                curDate = datetime.date(month=month,day=curDay,year=year) #creates datetime date obect
                weekday = curDate.strftime("%a") #returns abbreviated day of week

                callStart = datetime.datetime(year=year, month=month, day=curDay, hour=callTimes[curService].weekday(weekday).start.hour, minute=callTimes[curService].weekday(weekday).start.minute,second=0,tzinfo=pytz.timezone('US/Eastern')) #datetime object that adds a day to get correct day/month/year based on calendar. it then edits the hour/min values
                callEnd = callStart + datetime.timedelta(days=1)
                callEnd = callEnd.replace(hour=callTimes[curService].weekday(weekday).end.hour,minute=callTimes[curService].weekday(weekday).end.minute,tzinfo=pytz.timezone('US/Eastern'))

                cal = createCalendar(cal,curService,callStart,callEnd) #updates the cal file

            with open(path+'resident icals/'+month_str+'/'+'{}_{}_Call.ics'.format(month_str,res),'wb') as f:
                f.write(cal.to_ical())

            curResident = myModules.Staff.find_lastname(residents,res) #will be used in sendoutlookemail)

            if send:
                print(curResident.upmc_email)
                sendOutlookEmail(curResident.upmc_email, month_str+' iCalendar File', 'Hi,\n\nAttached is your iCalendar file for the month of {}. The iCal file can simply be dragged into your Outlook calendar or uploaded to Google Calendar via the Calendar Settings -> Import calendar. Please let me know if there are any problems. You can always access the most up to date schedule and files at:\nhttps://github.com/handzelrm/moonlighting\n\nThanks,\nRob'.format(month_str), path+'resident icals/'+month_str+'/'+month_str+'_'+res+'_Call.ics')
                # return
            else:
                print('\n'+curResident.upmc_email+'\n'+month_str+' iCalendar File', '\nHi,\n\nAttached is your iCalendar file for the month of {}. The iCal file can simply be dragged into your Outlook calendar or uploaded to Google Calendar via the Calendar Settings -> Import calendar. Please let me know if there are any problems. You can always access the most up to date schedule and files at:\nhttps://github.com/handzelrm/moonlighting\n\nThanks,\nRob'.format(month_str))


"""
sendOutlookEmail takes inputs who to send it to, subject, body, attachment and will
send an email as such using a local outlook application
"""
def sendOutlookEmail(to,subject,body,ical_attachment):
    outlook = win32.Dispatch('Outlook.Application') #creates outlook applicatoin object
    mail = outlook.CreateItem(0) #creates outlook item mail
    mail.To = to #adds who to send it to
    mail.Subject = subject #adds subject
    mail.Body = body #adds body
    # mail.Attachments.Add(excel_attachment)
    mail.Attachments.Add(ical_attachment) #adds attachment
    mail.Send() #sends message

def service_ical(path,file):
    df = pd.read_pickle(path+'call_schedule.pickle')

    #loads call times from pickle
    with open(path+'callTimes.pickle','rb') as f:
        callTimes = pickle.load(f)

    #loads services dictionary from pickle
    with open(path+'services.pickle','rb') as f:
        services = pickle.load(f)

    #loads month dictionary from pickle
    with open(path+'month.pickle','rb') as f:
        month = pickle.load(f)

    regex = re.search(r'(\w+) (\d+) Moonlighting',file)
    month_str = regex.group(1)
    month = month[month_str]
    year = int(regex.group(2))

    if not os.path.isdir(path+'service icals/'):
        os.makedirs(path+'service icals/')
    if not os.path.isdir(path+'service icals/'+month_str+'/'):
        os.makedirs(path+'service icals/'+month_str+'/')

    #loops through the services
    for service in services:
        df_service = df[['Date',service]] #new df with just Date (just numbered day of month) and service column)
        df_service = df_service[df_service[service]!='NEEDS COVERAGE'] #removes days that are not covered, but need coverage
        df_service = df_service[pd.notnull(df_service[service])] #removes days that are not covered, not needed

        cal = Calendar() #creates a new ical calendar object

        #loops through each row
        for row in df_service.iterrows():
            curDay = int(row[1].values[0]) #gest current integer of day value
            curRes = row[1].values[1] #gets the value of the resident assigned that call

            curDate = datetime.date(month=month,day=curDay,year=year) #creates datetime date obect
            weekday = curDate.strftime("%a") #returns abbreviated day of week

            callStart = datetime.datetime(year=year, month=month, day=curDay, hour=callTimes[service].weekday(weekday).start.hour, minute=callTimes[service].weekday(weekday).start.minute,second=0,tzinfo=pytz.timezone('US/Eastern')) #datetime object that adds a day to get correct day/month/year based on calendar. it then edits the hour/min values
            callEnd = callStart + datetime.timedelta(days=1)
            callEnd = callEnd.replace(hour=callTimes[service].weekday(weekday).end.hour,minute=callTimes[service].weekday(weekday).end.minute,tzinfo=pytz.timezone('US/Eastern'))

            cal = createCalendar(cal,curRes,callStart,callEnd) #updates the cal fi

        with open(path+'service icals/'+month_str+'/'+'{}{}_Call.ics'.format(month_str,service),'wb') as f:
            f.write(cal.to_ical())

# def run(file,send=False):
#     path = find_path(file)
#     print(path)
#     pickle_data(path=path, file=file)
#     resident_ical(path=path, file=file, send=send)



def main():
    file = 'April 2018 Moonlighting Final.xlsm'
    path=find_path(file)
    print(path)
    pickle_data(path=path, file=file)
    resident_ical(path=path, file=file, send=False)

    # service_ical(path=path, file=file)


if __name__ == '__main__':
    main()
