import pyfiglet
import webbrowser
import os
from colorama import Fore, Back, Style
#laget av kamil p


text2 = pyfiglet.print_figlet(text="snatcher",
 font="rowancap" ,colors="red")

print(text2)

print(Fore.BLUE + "laget av kamil p")  #fore lar deg farge teksten eller bakgrunnen. 
print(Fore.GREEN + "Select Mode:")
print("1: phishing page")
print("2: work in p")
print("3: work in p")

select1 = float(input("selection: "))
if select1 == 1:
    print(Fore.GREEN + "selected mode: 1 ")
    print("select type")
    print("1: login page")
    print("2: custom template")
    selection2 = float(input("selection: "))
    if selection2 == 1:
        webbrowser.open(f"index52.html")
    if selection2 == 2:
        input2 = input("enter file name: ")
        print("file location c/" + input2)
        f = open(input2 + ".html", "w")     #"w" betyr write, altså det lager en ny fil
                                            #"r" betyr read, altså det åpner en ny fil som du gir navnet og dir på.
                                            #her tok jeg input + ".html" som lar deg bruke variabel som over står som
                                            # velg navn som da brukes som input 2 + ".html" extention og åpner i browser altså ms edge. 
    else:
        print("syntax error")
else:
    print("work in progress.")  #work in progress for other methods prep, change to if, elif or else later.
    


  
        
        
