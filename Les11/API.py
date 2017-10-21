import requests
import xmltodict

auth_details = ('elinenube@hotmail.com', 'Q6WIq746GOtqim5Wr0iM7ePzk7xRdxCf0cgVwxDRSeQarmve66Q5Kg')
gekozenStation = input('Kies een station:')
api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + gekozenStation
response = requests.get(api_url, auth=auth_details)

vertrekXML = xmltodict.parse(response.text)

print('Dit zijn de vertrekkende treinen:')
for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
    eindbestemming = vertrek['EindBestemming']
    vertrektijd = vertrek['VertrekTijd']    # 2016-09-27T18:36:00+0200
    vertrektijd = vertrektijd[11:16]        # 18:36

    print('Om ' + str(vertrektijd) + ' vertrekt een trein naar ' + str(eindbestemming))