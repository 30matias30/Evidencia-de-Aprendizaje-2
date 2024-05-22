Algoritmo Despensa
	LECHE = 1000; D = 0.10; D2 = 0.15; DJ = 0.10
	Mnt_min = 12
	Mnt_max = 24
	J = 'y'
	Escribir 'Bienvenido a la LECHERIA, cuántas leches va a llevar?'
	Escribir 'Cantidad: '
	Leer cL
	pB = cL * LECHE
	Si cL > Mnt_min y cL <= Mnt_max Entonces
		desc = pB * D 
	SiNo
		Si cL > Mnt_max Entonces
			desc = pB * D2
		SiNo
			Escribir 'La cantidad no llega al monto de mayorista'
			desc = 0
		FinSi
	FinSi
	Escribir 'Eres JUBILADO? (y/n)'
	Leer rJ
	Si rJ = J Entonces
		descJ = pb * DJ
		pF = pB - desc - descJ
	SiNo
		pF = pB - desc
	FinSi
	Escribir 'El precio final de tu compra lactea es de :'
	Escribir '$ ' pF '.'
FinAlgoritmo
