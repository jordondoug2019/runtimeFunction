#Write a Python function that calculates the uptime percentage of a service based on the total number of hours 
#and the number of hours the service was down. The function should take 2 parameters(total hours and down hours, 
#inputted when the function is run). 
#Lastly, the function should return the uptime percentage rounded to two decimal places. 

#take 2 numbers
    #Uptime and Downtime
#return uptime rounded to a percentage

def runtime(tHours, dHours):
    uptime= (tHours-dHours)/tHours*100
    print(round(uptime,2))
    return round(uptime,2)

runtime(3600,500)