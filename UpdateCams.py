# a simple XBMC addon written to show webcam images
import urllib
import xbmc
import os

#define the storage directory
dirPath = "/storage/pictures/webcams"


#clean the directory of old images
fileList = os.listdir(dirPath)
for fileName in fileList:
 os.remove(dirPath+"/"+fileName)

#create a dictionary of the webcam images to be retrieved of the structure {"webpage":"name to be saved as"}
images={"http://images.drivebc.ca/bchighwaycam/pub/cameras/17.jpg":"1 stanleypark causeway.jpg",\
	"http://images.drivebc.ca/bchighwaycam/pub/cameras/179.jpg":"2 alicelake.jpg",\
	"http://images.drivebc.ca/bchighwaycam/pub/cameras/4.jpg":"3 garibaldi.jpg",\
	"http://images.drivebc.ca/bchighwaycam/pub/cameras/178.jpg":"4 functionjunction.jpg",\
	"http://www.whistlerolympicpark.com/webcams/netcam-s.jpg":"5 olympicpark.jpg",\
	"http://www.whistlerolympicpark.com/webcams/netcam-n.jpg":"6 olympicpark.jpg",\
	"http://www.whistlerolympicpark.com/webcams/ski-jump-whistlerheliskiing.jpg":"7 olympicpark.jpg",\
	"http://www.whistler.com/images/webcam/olympic_plaza/olympic_plaza.jpg":"8 olympicplaza.jpg",\
	"http://www.flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn31/Latest-gfacn31_cldwx_000.png":"9 GFA 00.jpg",\
	"http://www.flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn31/Latest-gfacn31_cldwx_006.png":"10 GFA 06.jpg",\
	"http://www.flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn31/Latest-gfacn31_cldwx_012.png":"11 GFA 12.jpg",\
	"http://www.jericho.ca/webcam/images/webcam.jpg":"12 jericho.jpg",\
	"http://www.jerichowind.com/east/fullday.gif":"/storage/pictures/webcams/14 jericho wind.jpg",\
	"http://windisgood.com/Webcams/pareilcam.jpg":"/storage/pictures/webcams/15 parksville.jpg",\
	"http://old.sailflow.com/cgi-bin/mapperv2.jpg?regionID=133&regionProductID=29&date=-1&websiteID=4&tid=453&hid=58487471&rid=446212248":"16 sailflow.jpg"}


#Retrieve the latest web images	and save them to the webcam directory
for i,j in images.items():
	try:
		urllib.urlretrieve(i,dirPath+"/"+j)
	except:
		pass

#Start a slideshow of the webcam directory using XBMC's builtin function
xbmc.executebuiltin("SlideShow("+dirPath+")")
