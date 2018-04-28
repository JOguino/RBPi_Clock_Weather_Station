# function to control ambient light
def setPixelArray(icon):
	# Color Grids
	sun = (255,255,0)
	clo = (0,169,255)
	bro = (0,0,255)
	rai = (200,0,255)
	mis = (104, 104, 104)
	sno = (0, 255, 255)
	thu = (50,255,50)
	red = (255, 0, 0)

	clear = [
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun 
		]

	few = [
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		sun, sun, sun, sun, sun, sun, sun, sun,
		clo, clo, clo, clo, clo, clo, clo, clo,
		clo, clo, clo, clo, clo, clo, clo, clo,
		clo, clo, clo, clo, clo, clo, clo, clo,	
		clo, clo, clo, clo, clo, clo, clo, clo
		]

	scattered = [
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo
		]

	broken = [
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro,
		bro, bro, bro, bro, bro, bro, bro, bro
		]

	shower = [
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai
		]

	rain = [
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		clo, clo, clo, clo, clo, clo, clo, clo, 
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai
		]

	mist = [
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis
		]

	snow = [
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		mis, mis, mis, mis, mis, mis, mis, mis,
		sno, sno, sno, sno, sno, sno, sno, sno,
		sno, sno, sno, sno, sno, sno, sno, sno,
		sno, sno, sno, sno, sno, sno, sno, sno,
		sno, sno, sno, sno, sno, sno, sno, sno
		]

	thunderstorm = [
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		rai, rai, rai, rai, rai, rai, rai, rai,
		red, red, red, red, red, red, red, red,
		red, red, red, red, red, red, red, red,
		thu, thu, thu, thu, thu, thu, thu, thu,
		thu, thu, thu, thu, thu, thu, thu, thu,
		thu, thu, thu, thu, thu, thu, thu, thu
		]

	if (icon=='01d')|(icon=='01n'):
		return  clear
	elif (icon=='02d')|(icon=='02n'):
		return  few
	elif (icon=='03d')|(icon=='03n'):
		return  scattered
	elif (icon=='04d')|(icon=='04n'):
		return  broken
	elif (icon=='09d')|(icon=='09n'):
		return  shower
	elif (icon=='10d')|(icon=='10n'):
		return  rain
	elif (icon=='11d')|(icon=='11n'):
		return  thunderstorm
	elif (icon=='13d')|(icon=='13n'):
		return  snow
	else:
		return  mist