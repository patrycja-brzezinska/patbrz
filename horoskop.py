y=str(input("Twój miesiąc urodzenia to: \n")).lower()
z=int(input("Twój dzień urodzenia to: \n"))
if(((y=="styczeń" or y=="styczen") and 19>=z>0) or ((y=="grudzień" or y=="grudzien") and 31>=z>=22)):
       print("Jesteś Koziorożcem!!!")
elif(((y=="styczeń" or y=="styczen") and 31>=z>=20) or (y=="luty" and 18>=z>0)):
       print("Jesteś Wodnikiem!!!")
elif((y=="luty" and 19<=z<=29) or (y=="marzec" and 20>=z>0)):
       print("Jesteś Rybami!!!")
elif((y=="marzec" and 31>=z>=21) or (y=="kwiecień" or y=="kwiecien") and 19>=z>0)):
       print("Jesteś Baranem!!!")
elif((y=="maj" and 20>=z>0) or ((y=="kwiecień" or y=="kwiecien") and 30>=z>=20)):
       print("Jesteś Bykiem!!!")
elif((y=="czerwiec" and 20>=z>0) or (y=="maj" and 31>=z>=21)):
       print("Jesteś Bliźniętami!!!")
elif((y=="czerwiec" and 30>=z>=21) or (y=="lipiec" and 22>=z>0)):
       print("Jesteś Rakiem!!!")
elif((y=="lipiec" and 31>=z>=23) or ((y=="sierpień" or y=="sierpien") and 22>=z>0)):
       print("Jesteś Lwem!!!")
elif(((y=="sierpień" or y=="sierpien") and 31>=z>=23) or ((y=="wrzesień" or y=="wrzesien") and 22>=z>0)):
       print("Jesteś Panną!!!")
elif(((y=="wrzesień" or y=="wrzesien") and 30>=z>=23) or ((y=="październik" or y=="pazdziernik") and 22>=z>0)):
       print("Jesteś Wagą!!!")
elif(((y=="październik" or y=="pazdziernik") and 31>=z>=23) or (y=="listopad" and 21>=z>0)):
       print("Jesteś Skorpionem!!!")
elif(((y=="grudzień" or y=="grudzien") and 21>=z>0) or (y=="listopad" and 30>=z>=22)):
       print("Jesteś Strzelcem!!!")
else:
       print("BŁĄD")
