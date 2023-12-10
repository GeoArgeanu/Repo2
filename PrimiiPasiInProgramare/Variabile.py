# variabila = zona din memorie calc care tine date
# variabila = cutiuta in care punem valori

# am declarat si initializat variabila
marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem pune spatiu in numele variabilei
# o variabila incepe cu litera mica
# loosely typed - nu trebuie specificat tipul de date

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'XC 60 facelift'

print(f'Am cumparat o masina marca : {marca_masina}')
print(f'Este modelul : {model_masina}')

nume = 'Geo'
prenume = 'Argeanu'
varsta = '34'
print(nume + ' ' + prenume)
print(f'{nume} {prenume} are varsta de {varsta}')