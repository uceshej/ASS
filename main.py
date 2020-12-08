def main(a,b,c):
	
	x=float(a)
	y=float(b)
	z=float(c)
	if x+y+z!=180:
	    typ='error'
	elif x==y and y==z:
	    typ='eq'
	elif x==y or x==z or y==z:
	    typ='is'
	else:
	    typ='sca'
	return typ

print(main(60,60,60))
print(main(70,70,40))
print(main(56,84,40))
print(main(46,79,76))

if __name__=='__main__':

        main(1,2,3)
