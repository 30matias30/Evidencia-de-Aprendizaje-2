Algoritmo Iterativa_4
	TE = 5
	Para i<-1 Hasta TE Con Paso 1 Hacer
		Escribir 'Ingrese la nota del alumno ' i
		Leer a
		b = b + a
	FinPara
	p = b / TE
	Si p > 8 Entonces
		Escribir 'El rendimineto del curso ha sido ELEVADO.'
		Escribir 'Promedio de ' p
	SiNo
		Si p >= 6 Entonces
			Escribir 'El rendimineto del curso ha sido ACEPTABLE.'
			Escribir 'Promedio de ' p
		SiNo
			Escribir 'El rendimineto del curso ha sido BAJO.'
			Escribir 'Promedio de ' p
		FinSi
	FinSi
FinAlgoritmo
