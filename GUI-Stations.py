from tkinter import *
import requests
import xmltodict

root = Tk()
root.geometry('500x500+500+100')

#api ophalen
def clicked():
    auth_details = ('elinenube@hotmail.com', 'Q6WIq746GOtqim5Wr0iM7ePzk7xRdxCf0cgVwxDRSeQarmve66Q5Kg')
    gekozenStation = entry.get()
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + gekozenStation
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        tekst =  'Om ' + str(vertrektijd) + ' vertrekt een trein naar ' + str(eindbestemming)
        print(tekst)
#invoer
voerStationIn = Label(master=root,
                      text='Kies een station* waar je wilt vertrekken.\n* Het een Nederlands NS-station zijn')
voerStationIn.pack(pady=20)

entry = Entry(master=root,
                width=50)
entry.pack(pady=10)

button = Button(master=root,
                text='Klik hier om uw keuze te bevestigen.',
                command=clicked)
button.pack()

#uitvoer
vertrektijd1 = Label(master=root)
vertrektijd1.pack(pady=20)

root.mainloop()