w=200
h=100
f=open("ray.ppm","w")
f.write("P3\n200 100\n255\n")
for j in range(0,h+1):
	for i in range(0,w):
		string=""
		r=int ((float(i)/float(w))*255*0.7)
		g=int ((float(h-j+1)/float(h))*255*0.7)
		b=int (0.9*255)

		string+=str(r)+" "+str(g)+" "+str(b)+"\n"
		f.write(string)
f.close()