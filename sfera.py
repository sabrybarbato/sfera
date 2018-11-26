import math

def volume(r)
  v=(4.0/3.0*math.pi)*r**3
   return v




r= input ("inserisci il raggio della sfera:")
r=int(r)
sf=volume(r)
print(sf)