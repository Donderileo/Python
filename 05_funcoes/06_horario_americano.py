def horario(hh):
	if (hh > 24) or (hh < 0):
		print("Formato invalido")
		return (-1)

	if (hh > 12):
		hh = hh - 12
	return hh

replay = 'S' 

while(replay == 'S') or (replay == 's'):
	hh = int(input("Insira as horas: "))
	mn = int(input("Insira os minutos: "))
	moment = 'x'
	aux = hh
	hh = horario(hh)
	if(aux == hh):
		moment = 'A'
	else:
		moment = 'P'
	if(hh > 0):
		print("0%d:%2d %c.M"%(hh,mn,moment))
	
	replay = input("Deseja fazer mais uma conversão?(S/N): ")
