y=str(input("Twój miesiąc urodzenia to: \n"))
z=int(input("Twój dzień urodzenia to: \n"))
if(((y=="Styczeń" or y=="Styczen" or y=="styczeń" or y=="styczen") and 19>=z>0) or ((y=="Grudzień" or y=="Grudzien" or y=="grudzień" or y=="grudzien") and 31>=z>=22)):
       print("Jesteś Koziorożcem!!!")
elif(((y=="Styczeń" or y=="Styczen" or y=="styczeń" or y=="styczen") and 31>=z>=20) or ((y=="Luty" or y=="luty") and 18>=z>0)):
       print("Jesteś Wodnikiem!!!")
elif(((y=="Luty" or y=="luty") and 19<=z<=29) or ((y=="Marzec" or y=="marzec") and 20>=z>0)):
       print("Jesteś Rybami!!!")
elif(((y=="Marzec" or y=="marzec") and 31>=z>=21) or ((y=="Kwiecień" or y=="Kwiecien" or y=="kwiecień" or y=="kwiecien") and 19>=z>0)):
       print("Jesteś Baranem!!!")
elif(((y=="Maj" or y=="maj") and 20>=z>0) or ((y=="Kwiecień" or y=="Kwiecien" or y=="kwiecień" or y=="kwiecien") and 30>=z>=20)):
       print("Jesteś Bykiem!!!")
elif(((y=="Czerwiec" or y=="czerwiec") and 20>=z>0) or ((y=="Maj" or y=="maj") and 31>=z>=21)):
       print("Jesteś Bliźniętami!!!")
elif(((y=="Czerwiec" or y=="czerwiec") and 30>=z>=21) or ((y=="Lipiec" or y=="lipiec") and 22>=z>0)):
       print("Jesteś Rakiem!!!")
elif(((y=="Lipiec" or y=="lipiec") and 31>=z>=23) or ((y=="Sierpień" or y=="Sierpien" or y=="sierpień" or y=="sierpien") and 22>=z>0)):
       print("Jesteś Lwem!!!")
elif(((y=="Sierpień" or y=="Sierpien" or y=="sierpień" or y=="sierpien") and 31>=z>=23) or ((y=="Wrzesień" or y=="Wrzesien" or y=="wrzesień" or y=="wrzesien") and 22>=z>0)):
       print("Jesteś Panną!!!")
elif(((y=="Wrzesień" or y=="Wrzesien" or y=="wrzesień" or y=="wrzesien") and 30>=z>=23) or ((y=="Październik" or y=="Pazdziernik" or y=="październik" or y=="pazdziernik") and 22>=z>0)):
       print("Jesteś Wagą!!!")
elif(((y=="Październik" or y=="Pazdziernik" or y=="październik" or y=="pazdziernik") and 31>=z>=23) or ((y=="Listopad" or y=="listopad") and 21>=z>0)):
       print("Jesteś Skorpionem!!!")
elif(((y=="Grudzień" or y=="Grudzien" or y=="grudzień" or y=="grudzien") and 21>=z>0) or ((y=="Listopad" or y=="listopad") and 30>=z>=22)):
       print("Jesteś Strzelcem!!!")
else:
       print("BŁĄD")