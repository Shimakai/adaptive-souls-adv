#setup 
si_no = ["si", "no"]
direzioni = ["sinistra", "destra", "avanti", "indietro"]
#introduzione
nome =input("Benvenuto nel sistema RAGNAROK, un mondo privo di alcuna legge terrena ove avvengono scontri tra due fazioni ...... e ...... Il tuo obbiettivo sarà lasciare segno nella storia facendo si che chiunque possa rimembrare le tue gesta, perciò scrivi il nome col quale vorrai essere ricordato:")
print("Mhhh,"+ nome + " quindi? \n Ottimo, che le tue gesta possano essere tramandate per l'eternità")
#si_inizia_boiiiiiiiiiiiii
risposta = ""
while risposta not in si_no:
    risposta = input("Sei pronto ad entrare in azione? \n Si, No\n")
    if risposta == "si":
        print()
