lista_goala = []
dict_gol = {}

# declaram si initializam un dict
note_elevi = {'Gigel': 10, 'Costel': 9, 'Ana': 10}

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dictul
print(note_elevi)

# aflam nota
print(note_elevi['Gigel'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# stergere valori
note_elevi.pop('Gigel')
print(note_elevi)
note_elevi.get('Gigel' + 'nu mai avem acest elev')
print(note_elevi)