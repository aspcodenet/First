from datetime import datetime, timedelta


#   02-28-2021     28-02-2021
datumStr = input("Mata in ett datum:") # "2021-02-28"
datum = datetime.strptime(datumStr,"%Y-%m-%d")

nu = datetime.now()
forfalloDag = nu + timedelta(30)
veckodag = forfalloDag.weekday()
if veckodag == 5:
    forfalloDag = forfalloDag - timedelta(1) #fredagen innan - 29
elif veckodag == 6:
    forfalloDag = forfalloDag + timedelta(1) #måndagen innan - 31

formattedDate = forfalloDag.strftime("%Y-%m-%d")    
print(f"Betala senast: {formattedDate}")


nu = datetime.now()
jul = datetime(2021,12,24,15,0,0)
diff = jul - nu
#print(f"{diff.days} dagar, {diff.}")
print(diff.days)

