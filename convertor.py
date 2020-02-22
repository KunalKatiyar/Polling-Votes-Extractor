import csv,json
import pandas as pd
import numpy as np
import os
import time

first={'COOCHBEHAR (SC)': ['Mathabhanga', 'Cooch Behar Uttar', 'Cooch BeharDakshin', 'Sitalkuchi', 'Sitai', 'Dinhata', 'Natabari'],
 'ALIPURDUARS (ST)': ['Tufanganj', 'Kumargram', 'Kalchini', 'Alipurduars', 'Falakata', 'Madarihat', 'Nagrakata'],
  'JALPAIGURI (SC)': ['Mekliganj', 'Dhupguri', 'Maynaguri', 'Jalpaiguri', 'Rajganj', 'Dabgram-Fulbari', 'Mal'],
   'DARJEELING': ['Kalimpong', 'Darjeeling', 'Kurseong', 'Matigara-Naxalbari', 'Siliguri', 'Phansidewa', 'Chopra'],
    'RAIGANJ': ['Islampur', 'Goalpokhar', 'Chakulia', 'Karandighi', 'Hemtabad', 'Kaliaganj', 'Raiganj'],
     'BALURGHAT': ['Itahar', 'Kushmandi', 'Kumarganj', 'Balurghat', 'Tapan', 'Gangarampur', 'Harirampur'],
      'MALDAHAUTTAR': ['Habibpur', 'Gazole', 'Chanchal', 'Harischandrapur', 'Malatipur', 'Ratua', 'Maldaha'],
       'MALDAHADAKSHIN': ['Manikchak', 'Englishbazar', 'Mothabari', 'Sujapur', 'Baisnabnagar', 'Farakka', 'Samserganj'],
        'JANGIPUR': ['Suti', 'Jangipur', 'RaghunathGanj', 'Sagardighi', 'Lalgola', 'Nabagram', 'Khargram'],
          'BAHARAMPUR': ['Burwan', 'Kandi', 'Bharatpur', 'Rejinagar', 'Beldanga', 'Baharampur', 'Naoda'],
           'MURSHIDABAD': ['Bhagabangola', 'Raninagar', 'Murshidabad', 'Hariharpara', 'Domkal', 'Jalangi', 'Karimpur'],
           	'KRISHNANAGAR': ['Tehatta', 'Palashipara', 'Kaliganj', 'Nakashipara', 'Chapra', 'Krishnanagar Uttar', 'KrishnanagarDakshin'],
           	 'RANAGHAT (SC)': ['Nabadwip', 'Santipur', 'Ranaghat UttarPaschim', 'Krishnaganj', 'Ranaghat UttarPurba', 'Ranaghat Dakshin', 'Chakdaha'],
           	 'BANGAON (SC)': ['Kalyani', 'Haringhata', 'Bagda', 'Bangaon Uttar', 'Bangaon Dakshin', 'Gaighata', 'Swarupnagar'],
	   	        'BARRACKPUR': ['Amdanga', 'Bijpur', 'Naihati', 'Bhatpara', 'Jagatdal', 'Noapara', 'Barrackpur'],
	   	        'DUM DUM': ['Khardaha', 'Dum Dum Uttar', 'Panihati', 'Kamarhati', 'Baranagar', 'Dum Dum', 'Rajarhat Gopalpur'],
               'BARASAT': ['Habra', 'Ashoknagar', 'Rajarhat NewTown', 'Bidhannagar', 'Madhyamgram', 'Barasat', 'Deganga'],
                'BASIRHAT': ['Baduria', 'Haroa', 'Minakhan', 'Sandeshkhali', 'Basirhat Dakshin', 'Basirhat Uttar', 'Hingalganj'],
                 'JAYNAGAR (SC)': ['Gosaba', 'Basanti', 'Kultali', 'Joynagar', 'Canning Paschim', 'Canning Purba', 'Magrahat Purba'],
                  'MATHURAPUR(SC)': ['Patharpratima', 'Kakdwip', 'Sagar', 'Kulpi', 'Raidighi', 'Mandirbazar', 'Magrahat Paschim'],
                   'DIAMONDHARBOUR': ['Diamond Harbour', 'Falta', 'Satgachhia', 'Bishnupur', 'Maheshtala', 'Budge Budge', 'Metiaburuz'],
                    'JADAVPUR': ['Baruipur Purba', 'Baruipur Paschim', 'Sonarpur Dakshin', 'Bhangar', 'Jadavpur', 'Sonarpur Uttar', 'Tollyganj'],
                     'KOLKATADAKSHIN': ['Kasba', 'Behala Purba', 'Behala Paschim', 'Kolkata Port', 'Bhabanipur', 'Rashbehari', 'Ballygunge'],
                      'KOLKATA UTTAR': ['Chowrangee', 'Entally', 'Beleghata', 'Jorasanko', 'Shyampukur', 'Maniktola', 'Kashipur-Belgachhia'],
                      'HOWRAH': ['Bally', 'Howrah Uttar', 'Howrah Madhya', 'Shibpur', 'Howrah Dakshin', 'Sankrail', 'Panchla'],
           	          'ULUBERIA': ['Uluberia Purba', 'Uluberia Uttar', 'Uluberia Dakshin', 'Shyampur', 'Bagnan', 'Amta', 'Udaynarayanpur'],
           	           'SREERAMPUR': ['Jagatballavpur', 'Domjur', 'Uttarpara', 'Sreerampur', 'Champdani', 'Chanditala', 'Jangipara'],
           	            'HOOGHLY': ['Singur', 'Chandannagar', 'Chunchura', 'Balagarh', 'Pandua', 'Saptagram', 'Dhanekhali'],
           	             'ARAMBAG (SC)': ['Haripal', 'Tarakeswar', 'Pursurah', 'Arambag', 'Goghat', 'Khanakul', 'Chandrakona'],
           	              'TAMLUK': ['Tamluk', 'Panskura Purba', 'Moyna', 'Nandakumar', 'Mahishadal', 'Haldia', 'Nandigram'],
           	               'KANTHI': ['Chandipur', 'Patashpur', 'Kanthi Uttar', 'Bhagabanpur', 'Khejuri', 'Kanthi Dakshin', 'Ramnagar'],
           	                'GHATAL': ['Panskura Paschim', 'Sabang', 'Pingla', 'Debra', 'Daspur', 'Ghatal', 'Keshpur'],
           	                 'JHARGRAM (ST)': ['Garbeta', 'Salboni', 'Nayagram', 'Gopiballavpur', 'Jhargram', 'Binpur', 'Bandwan'],
           	                  'MEDINIPUR': ['Egra', 'Dantan', 'Keshiary', 'Kharagpur Sadar', 'Narayangarh', 'Kharagpur', 'Medinipur'],
           	                   'PURULIA': ['Balarampur', 'Baghmundi', 'Joypur', 'Purulia', 'Manbazar', 'Kashipur', 'Para'],
           	                    'BANKURA': ['Raghunathpur', 'Saltora', 'Chhatna', 'Ranibandh', 'Raipur', 'Taldangra', 'Bankura'],
           	                     'BISHNUPUR (SC)': ['Barjora', 'Onda', 'Bishnupur', 'Katulpur', 'Indus', 'Sonamukhi', 'Khandaghosh'],
           	  'BARDHAMANPURBA (SC)': ['Raina', 'Jamalpur', 'Kalna', 'Memari', 'PurbasthaliDakshin', 'Purbasthali Uttar', 'Katwa'],
           	   'BARDHAMAN-DURGAPUR': ['Burdwan Dakshin', 'Monteswar', 'Burdwan Uttar', 'Bhatar', 'Galsi', 'Durgapur Purba', 'Durgapur Paschim'],
           	    'ASANSOL': ['Pandabeswar', 'Raniganj', 'Jamuria', 'Asnsol Dakshin', 'Asansol Uttar', 'Kulti', 'Barabani'],
           	     'BOLPUR (SC)': ['Ketugram', 'Mongalkote', 'Ausgram', 'Bolpur', 'Nanoor', 'Labhpur', 'Mayureswar'],
           	      'BIRBHUM': ['Dubrajpur', 'Suri', 'Sainthia', 'Rampurhat', 'Hansan', 'Nalhati', 'Murarai']}
for spider in range(1,43):
	try:		
		ini_d = "give/the/directory/to/the/input/folder" #dont run the code from the input directory
		colunm_row = []
		candidates = []
		finRow = []
		print('=============================================')
		ex = str(spider)
		if len(ex) == 4:
			ex = ex[1:]
			temp_d = ini_d + ex
			file= str(ex)
		elif len(ex) == 5:
			ex = ex[2:]
			temp_d = ini_d + ex
			file= str(ex)
		else:
			temp_d = ini_d + ex
			file= str(ex)
		filename=temp_d+".csv"
		# filename = 'C:/Users/dell/Desktop/Dont know/dynamic/zzz/'+filename
		df = pd.read_csv(filename)
		for name in list(df.columns.values):
			name = name.replace('\n','').replace('  ', ' ')
			colunm_row.append(name)
		colunm_row.insert(1,'vote_Other')
		colunm_row.insert(1,'Votes_Female')
		colunm_row.insert(1,'Votes_male')
		colunm_row.insert(1,'Elec_total')
		colunm_row.insert(1,'Elec_other')
		colunm_row.insert(1,'Elec_Female')
		colunm_row.insert(1,'Elec_male')
		colunm_row.insert(0,'ac_name')
		colunm_row.insert(0,'ac_id')
		colunm_row.insert(0,'pc_name')
		colunm_row.insert(0,'pc_id')
		numOfCandi = input("For "+str(spider)+": ")
		numOfCandi = int(numOfCandi,10)
		for c in range(12,12 + int(numOfCandi)):
			candidates.append(colunm_row[c])
			colunm_row[c] = 'Candidate ' + str(c-11)
		xount = 1
		ids = []
		pc_id = spider
		ac_name = []
		for vv,ii in zip(list(df[df.columns.values[0]]),range(0,len(list(df[df.columns.values[0]])) - 1)):
			vv = str(vv)
			if(vv == '1'):
				rows = []
				i = xount - 1
				xount += 1
				ids.insert(len(ids),ii)
				# print(first[str(list(first)[spider - 1])][i-(spider-1)*7])
				ac_name.insert(len(ac_name),first[str(list(first)[int(pc_id) - 1])][i])
				print('Code running for ' + filename)
			else:
				i =0
		ids.insert(7,len(df))
		for aot in range(0,7):
			for x in list(df[ids[aot]:ids[(aot+1)]].values):
				x = list(x)
				x.insert(1,'')
				x.insert(1,'')
				x.insert(1,'')
				x.insert(1,'')
				x.insert(1,'')
				x.insert(1,'')
				x.insert(1,'')
				x.insert(0,ac_name[aot])
				x.insert(0,str(aot+1))
				x.insert(0,str(list(first)[int(pc_id) - 1]))
				x.insert(0,str(pc_id))
				rows.append(x)



		for person,h in zip(candidates,range(0,int(numOfCandi)+1)):
			smRow = []
			smRow.append(str(pc_id))
			smRow.append(str(list(first)[int(pc_id) - 1]))	
			smRow.append(person)
			smRow.append(h+1)
			finRow.append(smRow)

		with open((str(spider) + 'candi.csv'),'w', encoding='utf-8') as cFile:
			wri = csv.writer(cFile)
			wri.writerow(['pc_id','pc_name','candidate name','candidate number'])
			wri.writerows(finRow)
		cFile.close()

		with open((str(spider) + '.csv'), 'w', encoding='utf-8') as csvFile:
		    writer = csv.writer(csvFile)
		    writer.writerow(colunm_row)
		    writer.writerows(rows)
		csvFile.close()
	except FileNotFoundError:
		print(str(spider) + 'th file not found')

