
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
    web_page_data=''
    r=requests.get(url_website)
    content=r.content
    soup=BeautifulSoup(content,'html.parser')
    web_page_data_t=soup.find_all('tbody')
    content=str(web_page_data_t)
    soup=BeautifulSoup(content,'html.parser')
    web_page_data=soup.find_all('tr')
    return web_page_data


def fetchVaccineDoses(web_page_data):
    vaccine_doses_dict = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    d=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    v=[]
    k=[]
    for i in range(1,max(d)+1):
        vaccine_doses_dict[str(i)]='Dose {}'.format(i)
    return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
    age_group_dict = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    d=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    age=[i.get_text() for i in soup.find_all('td',class_='age')]
    temp=[]
    for i,j in zip(d,age):
        if str(i)==str(dose):
            temp.append(j)
    temp=list(set([int(i.split('+')[0]) for i in temp]))
    temp.sort()
    for i,j in enumerate(temp):
        age_group_dict[str(i+1)]=str(j)+'+'
    return age_group_dict


def fetchStates(web_page_data, age_group, dose):
    states_dict = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    d=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    sn=[i.get_text() for i in soup.find_all('td',class_='state_name')]
    a=[i.get_text() for i in soup.find_all('td',class_='age')]
    fsn=[]
    for i,j,k in zip(d,a,sn):
        if str(i)==str(dose):
            if j==age_group:
                fsn.append(k)
    fsn=sorted(set(fsn))
    k=[]
    for i,j in enumerate(fsn):
        states_dict[str(i+1)]=j
    return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
    districts_dict = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    dos=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    sn=[i.get_text() for i in soup.find_all('td',class_='state_name')]
    a=[i.get_text() for i in soup.find_all('td',class_='age')]
    dis=[i.get_text() for i in soup.find_all('td',class_='district_name')]
    f_dis=[]
    for i,j,k,l in zip(dos,a,sn,dis):
        if str(dose)==str(i):
            if age_group==j:
                if state==k:
                    f_dis.append(l)
    f_dis=sorted(f_dis) 
    for i,j  in enumerate(f_dis):
        districts_dict[str(i+1)]=j
    return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
    hospital_vaccine_names_dict = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    dos=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    sn=[i.get_text() for i in soup.find_all('td',class_='state_name')]
    a=[i.get_text() for i in soup.find_all('td',class_='age')]
    dis=[i.get_text() for i in soup.find_all('td',class_='district_name')]
    h=[i.get_text() for i in soup.find_all('td',class_="hospital_name")]
    v=[i.get_text() for i in soup.find_all('td',class_="vaccine_name")]    

    f_h=[]
    for i,j,k,l,m,n in zip(dos,a,sn,dis,h,v):
        if str(i)==str(dose):
            if j==age_group:
                if k==state:
                    if l==district:
                        f_h.append([m,n])
    for i,j in enumerate(f_h):
        hospital_vaccine_names_dict[str(i+1)]={j[0]:j[1]}
    return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
    vaccine_slots = {}
    content=str(web_page_data)
    soup=BeautifulSoup(content,'html.parser')
    dos=[int(i.get_text()) for i in soup.find_all('td',class_='dose_num')]
    sn=[i.get_text() for i in soup.find_all('td',class_='state_name')]
    a=[i.get_text() for i in soup.find_all('td',class_='age')]
    dis=[i.get_text() for i in soup.find_all('td',class_='district_name')]
    h=[i.get_text() for i in soup.find_all('td',class_="hospital_name")]

    s1=[i.get_text() for i in soup.find_all('td',class_="may_15")]
    s2=[i.get_text() for i in soup.find_all('td',class_="may_16")]
    s3=[i.get_text() for i in soup.find_all('td',class_="may_17")]
    s4=[i.get_text() for i in soup.find_all('td',class_="may_18")]
    s5=[i.get_text() for i in soup.find_all('td',class_="may_19")]
    s6=[i.get_text() for i in soup.find_all('td',class_="may_20")]
    s7=[i.get_text() for i in soup.find_all('td',class_="may_21")]
    fs=[]
    for z,(i,j,k,l,m) in enumerate(zip(dos,a,sn,dis,h)):
        if str(i)==str(dose):
            if j==age_group:
                if k==state:
                    if l==district:
                        if m==hospital_name:
                            ind=z
    fs.append(['May 15',s1[ind]])
    fs.append(['May 16',s2[ind]])
    fs.append(['May 17',s3[ind]])
    fs.append(['May 18',s4[ind]])
    fs.append(['May 19',s5[ind]])
    fs.append(['May 20',s6[ind]])
    fs.append(['May 21',s7[ind]])
    for i,j in enumerate(fs):
        vaccine_slots[str(i+1)]={j[0]:j[1]}
    return vaccine_slots


def openConnection():
    client_socket = None
    client_addr = None
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1',24680))
    s.listen(1)
    client_socket,client_addr=s.accept()
    print('Client is connected at:  {}'.format(client_addr))
    return client_socket, client_addr
def dose_f(client_conn, client_addr,web_page_data):
    m='\n>>> Select the Dose of Vaccination:\n'+str(fetchVaccineDoses(web_page_data))+'\n\n'
    client_conn.send(m.encode('utf-8'))
    dose=client_conn.recv(1024).decode()
    d=fetchVaccineDoses(web_page_data)
    return dose,d
def age_f(client_conn, client_addr,web_page_data,dose):
    d=fetchAgeGroup(web_page_data, dose)
    m='\n\n>>> Select the Age Group:\n'+str(d)+'\n\n'
    client_conn.send(m.encode('utf-8'))
    age_group_k=str(client_conn.recv(1024).decode())
    return age_group_k,d

def state_f(client_conn, client_addr,web_page_data,age_group,dose):
    d=fetchStates(web_page_data, age_group, dose)
    m='\n\n>>> Select the State:\n'+str(d)+'\n\n'
    client_conn.send(m.encode('utf-8'))
    state_k=str(client_conn.recv(1024).decode())
    return state_k,d
def district_f(client_conn, client_addr,web_page_data,age_group,dose,state):
    d=fetchDistricts(web_page_data, state, age_group, dose)
    m='\n\n>>> Select the District:\n'+str(d)+'\n\n'
    client_conn.send(m.encode('utf-8'))
    district_k=str(client_conn.recv(1024).decode())
    return district_k,d

def hospital_f(client_conn, client_addr,web_page_data, district, state, age_group, dose):
    d=fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose)
    m='\n>>> Select the Vaccination Center Name:\n'+str(d)+'\n\n'
    client_conn.send(m.encode('utf-8'))
    hospital_name_k=str(client_conn.recv(1024).decode())
    return hospital_name_k,d

def slot_f(client_conn, client_addr,web_page_data, hospital_name, district, state, age_group, dose):
    d=fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose)
    m='\n\n>>> Select one of the available slots to schedule the Appointment:\n'+str(d)+'\n\n'
    client_conn.send(m.encode('utf-8'))
    key=str(client_conn.recv(1024).decode())
    return key,d
    
def dose_selection_f(client_conn, client_addr, web_page_data,count):
    while count!=3:
        message=''
        f=0
        dose,d=dose_f(client_conn, client_addr,web_page_data)
        if dose=='q' or dose=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if dose=='b' or dose=='B':
                continue
    
        if str(dose)==str(1):
            m='\n<<< Dose selected: '+dose
            client_conn.send(m.encode('utf-8'))
            print('Dose selected: '+dose)
            break
        if(str(dose)==str(2)):
            m='\n<<< Dose selected: '+dose
            client_conn.send(m.encode('utf-8'))
            print('Dose selected: '+dose)
            m='\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021'
            client_conn.send(m.encode('utf-8'))
            while True:
                error=0
                date=client_conn.recv(1024).decode()
                if date=='q' or date=='Q':
                    m='\n<<< See ya! Visit again :)'
                    client_conn.send(m.encode('utf-8'))
                    print('Client wants to quit!\nSaying Bye to client and closing the connection!')
                    exit()
                if date=='b' or date=='B':
                    f=1
                    break
                valid=True
                try:
                    d,m,y=date.split('/')
                    datetime.datetime(int(y),int(m),int(d))
                except ValueError:
                    valid=False
                if valid:
                    a=datetime.datetime.strptime(date,"%d/%m/%Y")
                    now=datetime.datetime.now()
                    diff=(now-a).days//7
                    if diff>=0:
                        m='\n<<< Date of First Vaccination Dose provided: %s'%date
                        client_conn.send(m.encode('utf-8'))
                        m='\n<<< Number of weeks from today: {}'.format(diff)
                        client_conn.send(m.encode())
                        if diff>=4 and diff<=8:
                            m='\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.'
                            client_conn.send(m.encode('utf-8'))
                            message='inner break'
                            error=0
                            break
                        if diff>8:
                            m='\n<<< You have been late in scheduling your 2nd Vaccination Dose by '+str(diff-8)+' weeks.\n'
                            client_conn.send(m.encode('utf-8'))
                            message='inner break'
                            error=0
                            break
                        if diff<4:
                            m='\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after '+str(4-diff)+' weeks.\n<<< See ya! Visit again :)'
                            client_conn.send(m.encode('utf-8'))
                            stopCommunication(client_conn)
                            exit()
                    else:
                        m='<<< Invalid Date provided of First Vaccination Dose: '+date+'\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021'
                        client_conn.send(m.encode('utf-8'))
                        continue
                    break

                else:
                    m='<<< Invalid Date provided of First Vaccination Dose: '+date+'\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021'
                    client_conn.send(m.encode('utf-8'))
                    continue
                
        if f==1:
            continue
        if message=='inner break':
            break
        if dose not in d.values():
            m='<<< Invalid input provided {} time(s)! Try again.'.format(count+1)
            print('Invalid input detected {} time(s)! Try again.'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
            if count>=3:
                print('Notifying the client and closing the connection!')
                m='\n<<< See ya! Visit again :)'
                client_conn.send(m.encode('utf-8'))
                exit()
    return dose,count
def age_selection_f(client_conn, client_addr, web_page_data,dose,count):
    while count!=3:
        age_group=''
        age_group_k,d=age_f(client_conn, client_addr,web_page_data,dose)
        if age_group_k=='q' or age_group_k=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if age_group_k=='b' or age_group_k=='B':
            dose,count=dose_selection_f(client_conn, client_addr, web_page_data,count)
            continue
        if str(age_group_k) not in d.keys():
            m='<<< Invalid input provided {} time(s)! Try again.'.format(count+1)
            print('Invalid input detected {} time(s)!'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
        else:
            age_group=d[age_group_k]
            m='\n<<< Selected Age Group: '+age_group
            client_conn.send(m.encode('utf-8'))
            print('Age Group selected:  '+age_group)
            break
    if count>=3:
        print('Notifying the client and closing the connection!')
        m='\n<<< See ya! Visit again :)'
        client_conn.send(m.encode('utf-8'))
        exit()

    return age_group,dose,count
def state_selection_f(client_conn, client_addr, web_page_data,dose,age_group,count):
    while count!=3:
        state_k,d=state_f(client_conn, client_addr,web_page_data,age_group,dose)
        if  state_k=='q' or state_k=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if state_k=='b' or state_k=='B':
            age_group,dose,count=age_selection_f(client_conn, client_addr, web_page_data,dose,count)
            continue
        if state_k in d.keys():
            state=d[state_k]
            m='\n<<< Selected State: '+state
            client_conn.send(m.encode('utf-8'))
            print('State selected:  '+state)
            break
        else:
            m='<<< Invalid input provided {} time(s)! Try again.'.format(count+1)
            print('Invalid input detected {} time(s)!'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
            if count>=3:
                print('Notifying the client and closing the connection!')
                m='\n<<< See ya! Visit again :)'
                client_conn.send(m.encode('utf-8'))
                exit()
    return state,age_group,dose,count

def district_selection_f(client_conn, client_addr,web_page_data,age_group,dose,state,count):
    while count!=3:
        district_k,d=district_f(client_conn, client_addr,web_page_data,age_group,dose,state)
        if district_k=='q' or district_k=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if district_k=='b' or district_k=='B':
            state,age_group,dose,count=state_selection_f(client_conn, client_addr, web_page_data,dose,age_group,count)
            continue
        if district_k in d.keys():
            district=d[district_k]
            m='\n<<< Selected District: '+district+'\n'
            client_conn.send(m.encode('utf-8'))
            print('District selected:  '+district)
            break
        else:
            m='<<< Invalid input provided {} time(s)! Try again.'.format(count+1)
            print('Invalid input detected {} time(s)!'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
            if count>=3:
                print('Notifying the client and closing the connection!')
                m='\n<<< See ya! Visit again :)'
                client_conn.send(m.encode('utf-8'))
                exit()
    return district,state,age_group,dose,count

def hospital_selection_f(client_conn, client_addr,web_page_data, district, state, age_group, dose,count):
    while count!=3:
        hospital_k,d=hospital_f(client_conn, client_addr,web_page_data, district, state, age_group, dose)
        if hospital_k=='q' or hospital_k=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if hospital_k=='b' or hospital_k=='B':
            district,state,age_group,dose,count=district_selection_f(client_conn, client_addr,web_page_data,age_group,dose,state,count)
            continue
        if hospital_k in d.keys():
            hospital_name=str(list(d[hospital_k].keys())[0])
            m='\n<<< Selected Vaccination Center: '+hospital_name
            client_conn.send(m.encode('utf-8'))
            print('Hospital selected:  '+hospital_name)
            break
        else:
            m='<<< Invalid input provided {} time(s)! Try again.\n'.format(count+1)
            print('Invalid input detected {} time(s)!'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
            if count>=3:
                print('Notifying the client and closing the connection!')
                m='<<< See ya! Visit again :)'
                client_conn.send(m.encode('utf-8'))
                exit()
    return hospital_name,district,state,age_group,dose,count

def slot_selection_f(client_conn, client_addr,web_page_data, hospital_name, district, state, age_group, dose,count):
    
    while count!=3:
        key,d=slot_f(client_conn, client_addr,web_page_data, hospital_name, district, state, age_group, dose)
        if key=='q' or key=='Q':
            m='\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            print('Client wants to quit!\nSaying Bye to client and closing the connection!')
            exit()
        if key=='b' or key=='B':
            hospital_name,district,state,age_group,dose,count=hospital_selection_f(client_conn, client_addr,web_page_data, district, state, age_group, dose,count)
            continue
        if key in d.keys():
            vaccine_slots=str(list(d[key].keys())[0])
            c=str(list(d[key].values())[0])
            m='\n<<< Selected Vaccination Appointment Date: '+vaccine_slots
            client_conn.send(m.encode('utf-8'))
            m='\n<<< Available Slots on the selected Date: '+c
            client_conn.send(m.encode('utf-8'))
            print('Vaccination Date selected:  '+vaccine_slots)
            break
        else:
            m='<<< Invalid input provided {} time(s)! Try again.'.format(count+1)
            print('Invalid input detected {} time(s)!'.format(count+1))
            client_conn.send(m.encode('utf-8'))
            count=count+1
            if count>=3:
                print('Notifying the client and closing the connection!')
                m='<<< See ya! Visit again :)'
                client_conn.send(m.encode('utf-8'))
                exit()
    return vaccine_slots,c,hospital_name,district,state,age_group,dose,count



def startCommunication(client_conn, client_addr, web_page_data):
    m="============================\n# Welcome to CoWIN ChatBot #\n============================\n\n\nSchedule an Appointment for Vaccination:\n"
    client_conn.send(m.encode('utf-8'))
    count=0
    dose,count=dose_selection_f(client_conn, client_addr, web_page_data,count)
    
    age_group,dose,count=age_selection_f(client_conn, client_addr, web_page_data,dose,count)    

    state,age_group,dose,count=state_selection_f(client_conn, client_addr, web_page_data,dose,age_group,count)


    district,state,age_group,dose,count=district_selection_f(client_conn, client_addr,web_page_data,age_group,dose,state,count)

    hospital_name,district,state,age_group,dose,count=hospital_selection_f(client_conn, client_addr,web_page_data, district, state, age_group, dose,count)
    
    vaccine_slots,c,hospital_name,district,state,age_group,dose,count=slot_selection_f(client_conn, client_addr,web_page_data, hospital_name, district, state, age_group, dose,count)
    while True:
        if int(c)>0:
            print('Available Slots on that date:  '+c)
            m='<<< Your appointment is scheduled.\n<<< See ya! Visit again :)'
            client_conn.send(m.encode('utf-8'))
            break
        if int(c)==0:
            m='\n<<< Selected Appointment Date has no available slots, select another date!'
            client_conn.send(m.encode('utf-8'))
            vaccine_slots,c,hospital_name,district,state,age_group,dose,count=slot_selection_f(client_conn, client_addr,web_page_data, hospital_name, district, state, age_group, dose,count)
    stopCommunication(client_conn)


def stopCommunication(client_conn):
    client_conn.close()
    quit()
    exit()
	

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################



##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
