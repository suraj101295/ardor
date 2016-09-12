import os
import sys
from urllib2 import urlopen,URLError,Request
import requests
import json
import math
import datetime

#Change according to local system
os.chdir("/home/sandra/spark2.0.0")
os.curdir

# Configure the environment. Set this up to the directory where
# Spark is installed
if 'SPARK_HOME' not in os.environ:
    os.environ['SPARK_HOME'] = '/home/sandra/spark2.0.0'

# Create a variable for our root path
SPARK_HOME = os.environ['SPARK_HOME']

#Add the following paths to the system path. Please check your installation
#to make sure that these zip files actually exist. The names might change
#as versions change.
sys.path.insert(0,os.path.join(SPARK_HOME,"python"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","pyspark.zip"))
sys.path.insert(0,os.path.join(SPARK_HOME,"python","lib","py4j-0.9-src.zip"))

#Initiate Spark context. Once this is done all other applications can run
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark import SQLContext
import itertools


# Optionally configure Spark Settings
conf=SparkConf()
conf.set("spark.executor.memory", "1g")
conf.set("spark.cores.max", "2")
conf.setAppName("Commute")

## Initialize SparkContext. Run only once. Otherwise you get multiple 
#Context Error.
sc = SparkContext('local', conf=conf)
sqlContext = SQLContext(sc)

traffic = sqlContext.read.json("db.json")
traffic.show()
traffic.registerTempTable("signal")
sqlContext.sql("SELECT * FROM signal WHERE Index>0 AND Index<23").show()
sqlContext.sql("SELECT * FROM signal WHERE Index>22 AND Index<38").show()
sqlContext.sql("SELECT * FROM signal WHERE Index>39 AND Index<48").show()

query=[]

query1="SELECT * FROM signal WHERE Signal_Name='Graphite India Junction'"
query.append(query1)
query2="SELECT * FROM signal WHERE Signal_Name='Kundenahalli Gate Junction'"
query.append(query2)
query3="SELECT * FROM signal WHERE Signal_Name='Marathahalli Bridge'"
query.append(query3)
query4="SELECT * FROM signal WHERE Signal_Name='HAL Main Gate'"
query.append(query4)
query5="SELECT * FROM signal WHERE Signal_Name='Manipal Hospital Junction'"
query.append(query5)
query6="SELECT * FROM signal WHERE Signal_Name='Diamond District'"
query.append(query6)
query7="SELECT * FROM signal WHERE Signal_Name='Domlur Water Tank Junction'"
query.append(query7)
query8="SELECT * FROM signal WHERE Signal_Name='Trinity Circle Junction'"
query.append(query8)
query9="SELECT * FROM signal WHERE Signal_Name='Mayo Hall'"
query.append(query9)
query10="SELECT * FROM signal WHERE Signal_Name='Richmond Circle Junction'"
query.append(query10)
query11="SELECT * FROM signal WHERE Signal_Name='Johnson Market Junction'"
query.append(query11)
query12="SELECT * FROM signal WHERE Signal_Name='Adugodi Junction'"
query.append(query12)
query13="SELECT * FROM signal WHERE Signal_Name='Forum Mall'"
query.append(query13)
query14="SELECT * FROM signal WHERE Signal_Name='Koramangala Water Tank Junction'"
query.append(query14)
query15="SELECT * FROM signal WHERE Signal_Name='Madiwala Police Station'"
query.append(query15)
query16="SELECT * FROM signal WHERE Signal_Name='Ayappa Temple Junction'"
query.append(query16)
query17="SELECT * FROM signal WHERE Signal_Name='Silk Board Junction'"
query.append(query17)
query18="SELECT * FROM signal WHERE Signal_Name='Bommanahalli Junction'"
query.append(query18)
query19="SELECT * FROM signal WHERE Signal_Name='Garvebavipalya Junction'"
query.append(query19)
query20="SELECT * FROM signal WHERE Signal_Name='Koodlu Junction'"
query.append(query20)
query21="SELECT * FROM signal WHERE Signal_Name='Electronic City - Phase 2'"
query.append(query21)
query22="SELECT * FROM signal WHERE Signal_Name='Wipro Junction'"
query.append(query22)
query23="SELECT * FROM signal WHERE Signal_Name='Silk Board Junction R2'"
query.append(query23)
query24="SELECT * FROM signal WHERE Signal_Name='HSR Main Junction'"
query.append(query24)
query25="SELECT * FROM signal WHERE Signal_Name='Agara Junction'"
query.append(query25)
query26="SELECT * FROM signal WHERE Signal_Name='Iblur Junction'"
query.append(query26)
query27="SELECT * FROM signal WHERE Signal_Name='Sarjapur Checkpoint Junction'"
query.append(query27)
query28="SELECT * FROM signal WHERE Signal_Name='Devara Beesana Halli Junction'"
query.append(query28)
query29="SELECT * FROM signal WHERE Signal_Name='Kadu beesanahalli Junction'"
query.append(query29)
query30="SELECT * FROM signal WHERE Signal_Name='Marathalli Bridge Junction'"
query.append(query30)
query31="SELECT * FROM signal WHERE Signal_Name='Doddanakundi Junction'"
query.append(query31)
query32="SELECT * FROM signal WHERE Signal_Name='Tin Factory'"
query.append(query32)
query33="SELECT * FROM signal WHERE Signal_Name='Ramamurthy Nagar Junction'"
query.append(query33)
query34="SELECT * FROM signal WHERE Signal_Name='Kalyan Nagar'"
query.append(query34)
query35="SELECT * FROM signal WHERE Signal_Name='Hennur Road'"
query.append(query35)
query36="SELECT * FROM signal WHERE Signal_Name='Veeranna Palaya'"
query.append(query36)
query37="SELECT * FROM signal WHERE Signal_Name='Hebbal'"
query.append(query37)
query38="SELECT * FROM signal WHERE Signal_Name='KR Market Junction'"
query.append(query38)
query39="SELECT * FROM signal WHERE Signal_Name='Shankar Mutt Road Junction'"
query.append(query39)
query40="SELECT * FROM signal WHERE Signal_Name='National College'"
query.append(query40)
query41="SELECT * FROM signal WHERE Signal_Name='Dewan Madhav Rao Junction'"
query.append(query41)
query42="SELECT * FROM signal WHERE Signal_Name='South End Circle'"
query.append(query42)
query43="SELECT * FROM signal WHERE Signal_Name='Aurobindo Circle'"
query.append(query43)
query44="SELECT * FROM signal WHERE Signal_Name='Yediyur Maternity Hospital Junction'"
query.append(query44)
query45="SELECT * FROM signal WHERE Signal_Name='Banashankari Bus Stand Junction'"
query.append(query45)
query46="SELECT * FROM signal WHERE Signal_Name='Ilyas Nagar'"
query.append(query46)
query47="SELECT * FROM signal WHERE Signal_Name='Konakunte Junction'"
query.append(query47)



################################

source=raw_input("Enter source:")

if(source=="Graphite India Junction"):
	src=sqlContext.sql(query1).collect()
elif(source=="Kundenahalli Gate Junction"):
	src=sqlContext.sql(query2).collect()
elif(source=="Marathahalli Bridge"):
	src=sqlContext.sql(query3).collect()
elif(source=="HAL Main Gate"):
	src=sqlContext.sql(query4).collect()
elif(source=="Manipal Hospital Junction"):
	src=sqlContext.sql(query5).collect()
elif(source=="Diamond District"):
	src=sqlContext.sql(query6).collect()
elif(source=="Domlur Water Tank Junction"):
	src=sqlContext.sql(query7).collect()
elif(source=="Trinity Circle Junction"):
	src=sqlContext.sql(query8).collect()
elif(source=="Mayo Hall"):
	src=sqlContext.sql(query9).collect()
elif(source=="Richmond Circle Junction"):
	src=sqlContext.sql(query10).collect()
elif(source=="Johnson Market Junction"):
	src=sqlContext.sql(query11).collect()
elif(source=="Adugodi Junction"):
	src=sqlContext.sql(query12).collect()
elif(source=="Forum Mall"):
	src=sqlContext.sql(query13).collect()
elif(source=="Kormangala Water Tank Junction"):
	src=sqlContext.sql(query14).collect()
elif(source=="Madiwala Police Station"):
	src=sqlContext.sql(query15).collect()
elif(source=="Ayappa Temple Junction"):
	src=sqlContext.sql(query16).collect()
elif(source=="Silk Board Junction"):
	src=sqlContext.sql(query17).collect()
elif(source=="Bommanahalli Junction"):
	src=sqlContext.sql(query18).collect()
elif(source=="Garvebavipalya Junction"):
	src=sqlContext.sql(query19).collect()
elif(source=="Koodlu Junction"):
	src=sqlContext.sql(query20).collect()
elif(source=="Electronic City - Phase 2"):
	src=sqlContext.sql(query21).collect()
elif(source=="Wipro Junction"):
	src=sqlContext.sql(query22).collect()
elif(source=="Silk Board Junction R2"):
	src=sqlContext.sql(query23).collect()
elif(source=="HSR Main Junction"):
	src=sqlContext.sql(query24).collect()
elif(source=="Agara Junction"):
	src=sqlContext.sql(query25).collect()
elif(source=="Iblur Junction"):
	src=sqlContext.sql(query26).collect()
elif(source=="Sarjapur Checkpoint Junction"):
	src=sqlContext.sql(query27).collect()
elif(source=="Devara Beesana Halli Junction"):
	src=sqlContext.sql(query28).collect()
elif(source=="Kadu beesanahalli Junction"):
	src=sqlContext.sql(query29).collect()
elif(source=="Marathalli Bridge Junction"):
	src=sqlContext.sql(query30).collect()
elif(source=="Doddanakundi Junction"):
	src=sqlContext.sql(query31).collect()
elif(source=="Tin Factory"):
	src=sqlContext.sql(query32).collect()
elif(source=="Ramamurthy Nagar Junction"):
	src=sqlContext.sql(query33).collect()
elif(source=="Kalyan Nagar"):
	src=sqlContext.sql(query34).collect()
elif(source=="Hennur Road"):
	src=sqlContext.sql(query35).collect()
elif(source=="Veeranna Palaya"):
	src=sqlContext.sql(query36).collect()
elif(source=="Hebbal"):
	src=sqlContext.sql(query37).collect()
elif(source=="KR Market Junction"):
	src=sqlContext.sql(query38).collect()
elif(source=="Shankar Mutt Road Junction"):
	src=sqlContext.sql(query39).collect()
elif(source=="National College"):
	src=sqlContext.sql(query40).collect()
elif(source=="Dewan Madhav Rao Junction"):
	src=sqlContext.sql(query41).collect()
elif(source=="South End Circle"):
	src=sqlContext.sql(query42).collect()
elif(source=="Aurobindo Circle"):
	src=sqlContext.sql(query43).collect()
elif(source=="Yediyur Maternity Hospital Junction"):
	src=sqlContext.sql(query44).collect()
elif(source=="Banashankari Bus Stand Junction"):
	src=sqlContext.sql(query45).collect()
elif(source=="Ilyas Nagar"):
	src=sqlContext.sql(query46).collect()
elif(source=="Konakunte Junction"):
	src=sqlContext.sql(query47).collect()


srcd = {}
for ele in src:
	d = str(ele)
	d = d.strip("Row")
	d = d.strip(")")
	d = d.strip("(")
	d = d.replace("=",":")
        d = d.split(",")

d[0]=d[0].strip("Distance:")
d[0]=d[0].strip("'")
d[1]=d[1].strip(" Index:")
d[1]=d[1].strip("'")
d[2]=d[2].strip(" Police_Station:u")
d[2]=d[2].strip("'")
d[3]=d[3].strip(" Signal_Name:u")
d[3]=d[3].strip("'")
d[4]=d[4].strip(" Signal_Time:u")
d[4]=d[4].strip("'")



srcd["Distance"]=float(d[0])
srcd["Index"]=int(d[1])
srcd["Police Station"]=d[2]
srcd["Signal Name"]=d[3]
srcd["Signal Time"]=float(d[4])

#print srcd	

indexs=srcd["Index"]

######################

destination=raw_input("Enter destination:")

if(destination=="Graphite India Junction"):
	dst=sqlContext.sql(query1).collect()
elif(destination=="Kundenahalli Gate Junction"):
	dst=sqlContext.sql(query2).collect()
elif(destination=="Marathahalli Bridge"):
	dst=sqlContext.sql(query3).collect()
elif(destination=="HAL Main Gate"):
	dst=sqlContext.sql(query4).collect()
elif(destination=="Manipal Hospital Junction"):
	dst=sqlContext.sql(query5).collect()
elif(destination=="Diamond District"):
	dst=sqlContext.sql(query6).collect()
elif(destination=="Domlur Water Tank Junction"):
	dst=sqlContext.sql(query7).collect()
elif(destination=="Trinity Circle Junction"):
	dst=sqlContext.sql(query8).collect()
elif(destination=="Mayo Hall"):
	dst=sqlContext.sql(query9).collect()
elif(destination=="Richmond Circle Junction"):
	dst=sqlContext.sql(query10).collect()
elif(destination=="Johnson Market Junction"):
	dst=sqlContext.sql(query11).collect()
elif(destination=="Adugodi Junction"):
	dst=sqlContext.sql(query12).collect()
elif(destination=="Forum Mall"):
	dst=sqlContext.sql(query13).collect()
elif(destination=="Kormangala Water Tank Junction"):
	dst=sqlContext.sql(query14).collect()
elif(destination=="Madiwala Police Station"):
	dst=sqlContext.sql(query15).collect()
elif(destination=="Ayappa Temple Junction"):
	dst=sqlContext.sql(query16).collect()
elif(destination=="Silk Board Junction"):
	dst=sqlContext.sql(query17).collect()
elif(destination=="Bommanahalli Junction"):
	dst=sqlContext.sql(query18).collect()
elif(destination=="Garvebavipalya Junction"):
	dst=sqlContext.sql(query19).collect()
elif(destination=="Koodlu Junction"):
	dst=sqlContext.sql(query20).collect()
elif(destination=="Electronic City - Phase 2"):
	dst=sqlContext.sql(query21).collect()
elif(destination=="Wipro Junction"):
	dst=sqlContext.sql(query22).collect()
elif(destination=="Silk Board Junction R2"):
	dst=sqlContext.sql(query23).collect()
elif(destination=="HSR Main Junction"):
	dst=sqlContext.sql(query24).collect()
elif(destination=="Agara Junction"):
	dst=sqlContext.sql(query25).collect()
elif(destination=="Iblur Junction"):
	dst=sqlContext.sql(query26).collect()
elif(destination=="Sarjapur Checkpoint Junction"):
	dst=sqlContext.sql(query27).collect()
elif(destination=="Devara Beesana Halli Junction"):
	dst=sqlContext.sql(query28).collect()
elif(destination=="Kadu beesanahalli Junction"):
	dst=sqlContext.sql(query29).collect()
elif(destination=="Marathalli Bridge Junction"):
	dst=sqlContext.sql(query30).collect()
elif(destination=="Doddanakundi Junction"):
	dst=sqlContext.sql(query31).collect()
elif(destination=="Tin Factory"):
	dst=sqlContext.sql(query32).collect()
elif(destination=="Ramamurthy Nagar Junction"):
	dst=sqlContext.sql(query33).collect()
elif(destination=="Kalyan Nagar"):
	dst=sqlContext.sql(query34).collect()
elif(destination=="Hennur Road"):
	dst=sqlContext.sql(query35).collect()
elif(destination=="Veeranna Palaya"):
	dst=sqlContext.sql(query36).collect()
elif(destination=="Hebbal"):
	dst=sqlContext.sql(query37).collect()
elif(destination=="KR Market Junction"):
	dst=sqlContext.sql(query38).collect()
elif(destination=="Shankar Mutt Road Junction"):
	dst=sqlContext.sql(query39).collect()
elif(destination=="National College"):
	dst=sqlContext.sql(query40).collect()
elif(destination=="Dewan Madhav Rao Junction"):
	dst=sqlContext.sql(query41).collect()
elif(destination=="South End Circle"):
	dst=sqlContext.sql(query42).collect()
elif(destination=="Aurobindo Circle"):
	dst=sqlContext.sql(query43).collect()
elif(destination=="Yediyur Maternity Hospital Junction"):
	dst=sqlContext.sql(query44).collect()
elif(destination=="Banashankari Bus Stand Junction"):
	dst=sqlContext.sql(query45).collect()
elif(destination=="Ilyas Nagar"):
	dst=sqlContext.sql(query46).collect()
elif(destination=="Konakunte Junction"):
	dst=sqlContext.sql(query47).collect()


desd = {}
for ele in dst:
	d = str(ele)
	d = d.strip("Row")
	d = d.strip(")")
	d = d.strip("(")
	d = d.replace("=",":")
        d = d.split(",")

d[0]=d[0].strip("Distance:")
d[0]=d[0].strip("'")
d[1]=d[1].strip(" Index:")
d[1]=d[1].strip("'")
d[2]=d[2].strip(" Police_Station:u")
d[2]=d[2].strip("'")
d[3]=d[3].strip(" Signal_Name:u")
d[3]=d[3].strip("'")
d[4]=d[4].strip(" Signal_Time:u")
d[4]=d[4].strip("'")


desd["Distance"]=float(d[0])
desd["Index"]=int(d[1])
desd["Police Station"]=d[2]
desd["Signal Name"]=d[3]
desd["Signal Time"]=float(d[4])

#print desd

indexd=desd["Index"]

###########

master=[]
master.append(srcd)

#print "Master dict: "

if(indexd-indexs > 0):
	down=1
	#print("Top to down")
	for x in range(indexs+1,indexd):
		dummy=sqlContext.sql(query[x-1]).collect()
		dummyd={}
		for ele in dummy:
			d = str(ele)
			d = d.strip("Row")
			d = d.strip(")")
			d = d.strip("(")
			d = d.replace("=",":")
       			d = d.split(",")

		d[0]=d[0].strip("Distance:")
		d[0]=d[0].strip("'")
		d[1]=d[1].strip(" Index:")
		d[1]=d[1].strip("'")
		d[2]=d[2].strip(" Police_Station:u")
		d[2]=d[2].strip("'")
		d[3]=d[3].strip(" Signal_Name:u")
		d[3]=d[3].strip("'")
		d[4]=d[4].strip(" Signal_Time:u")
		d[4]=d[4].strip("'")


		dummyd["Distance"]=float(d[0])
		dummyd["Index"]=int(d[1])
		dummyd["Police Station"]=d[2]
		dummyd["Signal Name"]=d[3]
		dummyd["Signal Time"]=float(d[4])

		master.append(dummyd)
	
	
else:
	down=0
	#print("Down to up")
	for x in range(2,indexs-indexd+1):
		dummy=sqlContext.sql(query[indexs-(x)]).collect()
		dummyd={}
		for ele in dummy:
			d = str(ele)
			d = d.strip("Row")
			d = d.strip(")")
			d = d.strip("(")
			d = d.replace("=",":")
       			d = d.split(",")

		d[0]=d[0].strip("Distance:")
		d[0]=d[0].strip("'")
		d[1]=d[1].strip(" Index:")
		d[1]=d[1].strip("'")
		d[2]=d[2].strip(" Police_Station:u")
		d[2]=d[2].strip("'")
		d[3]=d[3].strip(" Signal_Name:u")
		d[3]=d[3].strip("'")
		d[4]=d[4].strip(" Signal_Time:u")
		d[4]=d[4].strip("'")


		dummyd["Distance"]=float(d[0])
		dummyd["Index"]=int(d[1])
		dummyd["Police Station"]=d[2]
		dummyd["Signal Name"]=d[3]
		dummyd["Signal Time"]=float(d[4])

		master.append(dummyd)
	
		
master.append(desd)
Dist=[]
Sig_Name=[]
Sig_Time=[]
#for ele in master:
#	print ele
x=len(master)
#print "Length of master list: ",x
if(indexd-indexs > 0):
	for y in range(0,x-1):
	 	disc = master[y]["Distance"]
		SN = master[y]["Signal Name"]
		ST = master[y]["Signal Time"]
		Dist.append(disc)
		Sig_Name.append(SN)
		Sig_Time.append(ST)
else:
	for y in range(1,x):
		disc = master[y]["Distance"]
		Dist.append(disc)
		SN = master[y]["Signal Name"]
		Sig_Name.append(SN)
		ST = master[y]["Signal Time"]
		Sig_Time.append(ST)

print("List of names of signals enroute\n")
print Sig_Name
#print("List of distances between signals enroute\n")
#print Dist
#print("List of traffic light cycles for all signals enroute\n")
#print Sig_Time

################
#print("Enter the starting time of your journey in hh:mm:ss")
#Time_str = raw_input()
Time_str  = str(datetime.datetime.now().time())
################

#to convert given time to seconds
def get_sec(Time_str):
    
    
    h, m, s = Time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(float(s))

Time_Start = get_sec(Time_str)

#print "Start time of journey in seconds from 00:00:00 is\t",Time_Start
## Time_Start - time of start of journey converted to seconds

##to get approximate time of travel from source to destination
def get_Time_Approx(start,finish):
	apiurl = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="

	source = start
	source = source.replace(" ","+")
	rsource = source+"+bangalore+india"

	dest = finish
	dest = dest.replace(" ","+")
	rdest = "&destinations="+dest+"+bangalore+india"


	traffic = "&departure_time=now&traffic_model"
	key = "&key=AIzaSyBk_8AZa8WsndiFSSuZ09oA3x4C5x7rdes"

	response = urlopen(apiurl+rsource+rdest+traffic+key)

	#gives link to the json file
	#print apiurl+rsource+rdest+traffic+key

	body = response.read()
	obj = json.loads(body)


	time = obj['rows'][0]['elements'][0]['duration']['value']
	distance = obj['rows'][0]['elements'][0]['distance']['value']
	traffic_time = obj['rows'][0]['elements'][0]['duration_in_traffic']['value']

	#print "time = ",time
	#print "distance = ",distance 
	return traffic_time
							
##to get Distance to be travelled from source to destination
def get_Total_Distance(start,finish):
	apiurl = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="

	source = start
	source = source.replace(" ","+")
	rsource = source+"+bangalore+india"

	dest = finish
	dest = dest.replace(" ","+")
	rdest = "&destinations="+dest+"+bangalore+india"


	traffic = "&departure_time=now&traffic_model"
	key = "&key=AIzaSyBk_8AZa8WsndiFSSuZ09oA3x4C5x7rdes"

	response = urlopen(apiurl+rsource+rdest+traffic+key)

	#gives link to the json file
	#print apiurl+rsource+rdest+traffic+key

	body = response.read()
	obj = json.loads(body)


	time = obj['rows'][0]['elements'][0]['duration']['value']
	distance = obj['rows'][0]['elements'][0]['distance']['value']
	traffic_time = obj['rows'][0]['elements'][0]['duration_in_traffic']['value']

	#print "time = ",time
	#print "distance = ",distance 
	return distance
				





#i to access signal name, j to access between signals, k to access the distances in Dist , D is value of k for a single iteration, p for Sig_Time, Time_Cycle is value of p for a single iteration

##### THE MAIN FUNCTION ##########
print "Your Journey Is From ",source, "to" ,destination, "where:\n"
s = get_Total_Distance(source,destination)
Travel_Distance = s/1000 
print "Approximate Distance to be covered is: ", Travel_Distance,"km\n" 

for i in range(0,len(master)):
	T1 = master[i]["Signal Name"]
	if i > len(master)-2:
		break
	else:
		T2 = master[i+1]["Signal Name"]
		#print T1
		#print T2
	Time_Approx = get_Time_Approx(T1,T2)
	Time_in_minutes = Time_Approx/60
	print "From ",T1," To ",T2,"\nTime = ",Time_in_minutes," minutes"
	for k in Dist:
		D = k
		for p in Sig_Time:
			Time_Cycle = p
		Time_Total = Time_Start + Time_Approx ## total time for red light to change starting from 00:00:00
		Cycles_Elapsed = Time_Total/Time_Cycle ## no. of total cycles finished when next node enroute is reached
	#print Cycles_Elapsed
	Cycle_Fraction = Cycles_Elapsed - int(Cycles_Elapsed)
	#print Cycle_Fraction
	Ongoing_Cycle = Cycle_Fraction * master[i]["Signal Time"]
	x = int(Ongoing_Cycle)# int value of ongoing cycle saved in x
	if x > (0.6 * master[i]["Signal Time"]):
		Time_Fraction = master[i]["Signal Time"] - x #Time_Fraction is to be added to the time by which distance is to be divided
		Average_Speed = D/(Time_Fraction + Time_Approx + 120)
	else:
		Average_Speed = D/(Time_Approx +120)
	AVERAGE_SPEED = (Average_Speed * 3600)+25	
	print "Average speed = ",AVERAGE_SPEED," km/hr\n\n"
	javsp=[]
	javsp.append(AVERAGE_SPEED)
a=0
for z in javsp:
	a = a + z
Journey_speed = a/len(javsp)
print"\n\nAverage Speed to be maintained throughout the journey is: ",Journey_speed,"km/hr\n"
