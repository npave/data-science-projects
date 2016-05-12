# Linear regression

from math import exp, log

def least_squares(x,y):
	n 		= len(x)
	sxi		= sum(x)
	syi		= sum(y)
	sxi2	= sum(xi**2 for xi in x)
	sxiyi	= sum(xi*yi for xi,yi in zip(x,y))
	detA	= sxi*sxi - n*sxi2
	detm	= syi*sxi - n*sxiyi
	detb	= sxi*sxiyi - sxi2*syi

	return (float(detm)/detA, float(detb)/detA)
	
def least_squares_exp(x,y):
	logy	= [log(yi) for yi in y]
	b,loga	= least_squares(x,logy)
	return (exp(loga),b)

