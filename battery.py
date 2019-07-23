import psutil
import time

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = int(battery.percent)
if plugged==False: plugged="Not Plugged In"
else: plugged="Plugged In"

print('\007')
if( plugged=="Plugged In" and percent > 95 ):
    print("----------------WARNING------------------------")
    print("----------------WARNING------------------------")
    
    print("BATTERY CHARGED TO 95 % : PLEASE REMOVE CHARGER")
elif(plugged=="Not Plugged In" and percent < 20):
   
    print("-------------------WARNING----------------")
    print("-------------------WARNING----------------")
    print("BATTERY PERCENTAGE LESS THAN 20 % : PLEASE PLUG IN CHARGER!")




print("press Enter to exit the script")
input()



