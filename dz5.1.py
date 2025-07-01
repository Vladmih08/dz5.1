#---------------------------------------------------------------------------#
import string
import keyword
#---------------------------------------------------------------------------#
a = input()
rezultat = "True"
#---------------------------------------------------------------------------#
if a[0].isdigit() or a in keyword.kwlist or '__' in a:
    rezultat = "False"
for simvol in a:
    if simvol in string.punctuation and simvol != '_' or simvol.isupper():
        rezultat = "False"
        break
#---------------------------------------------------------------------------#
print(rezultat)
#---------------------------------------------------------------------------#