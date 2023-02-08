import math
def round_to_even(n):
    # round off to the nearest integer
    rounded = round(n)
    # if the rounded number is odd, add 1
    if rounded % 2 != 0:
        rounded += 1
    return rounded
    
#CREDITS
print("\033[33mCredits:\n        Syed Shahid \033[0m")
print("")

#Input Data

b1 = int(input("Enter the width of thinner plate in mm "))
print("")

t1 = int(input("Enter the thickness of thinner plate in mm "))
print("")

b2 = int(input("Enter the width of thicker plate in mm "))
print("")

t2 = int(input("Enter the thickness of thicker plate in mm "))
print("")

P = int(input("Enter the value of axial load in Service Condition in KN =  "))
print("")

fu = int(input("Enter fu value of plate in N/mm**2 "))
print("")

print ("The Ultimate strength of plate (fu) = ",fu," N/mm*2")
print("")

fy =  int(input("Enter fy value of plate in N/mm**2 "))
print("")

print ("The Yield strength of plate (fy) = ",fy,"N/mm**2")
print("")

C = float(input("Enter the grade or class of bolts "))
print ("\033[31m Bolts used are of", C ,"Grade \033[0m")
print("")

γₘₗ = 1.25
γₘb = 1.25
γₘₒ = 1.1
γₘf = 1.1

#Printing the fub values of bolts
fub = int(C) * 100 
print("fub = ", fub , "N/mm**2") 
print("")

#Printing the fyb values of bolts
fyb = int(C) * int(str(C).split(".")[1]) * 10
print("fyb = ", fyb , " N/mm**2") 
print("")

# printing the type of joint
print("\033[31m NOTE :\033[0m")
print("      \033[31m1.For Lap Joint or Single Cover Butt Joint nₙ =1\n      2.For Double Cover Butt Joint nₙ = 2\033[0m")
print("")

nₙ = int(input("Enter the number of shearing planes: "))

if nₙ == 1:
    print("\033[31m The joint is a Lap joint or Single Cover Butt Joint.\033[0m")
elif nₙ == 2:
    print("\033[31m The joint is a Double Cover Butt joint.\033[0m")
else:
    print("The number of shearing planes is not valid.")
    print("")
    
# If Shearing planes are also in shunk region
    
print("If shunk region is also in shear then put nₛ = 1 else nₛ = 0 ") 
nₛ = int(input(" Enter the value of ns "))
print("")

#Diameter of Bol
if t1 <1:
    d=int(input("Enter Diameter of Bolt in mm "))
else:
    d=int(round_to_even(6.04*math.sqrt(t1)))
    print("The Diameter of Bolt is ", round_to_even(d), "mm")
  
    

if 12 <= d <= 14:
    dₒ = d + 1
    print("Diameter of Hole dₒ =", dₒ)
elif 16 <= d <= 24:
    dₒ = d + 2
    print("Diameter of Hole dₒ =", dₒ)
elif d > 24:
    dₒ = d + 3
    print("Diameter of Hole dₒ =", dₒ)
else:
    print("d is not in the expected range.")
print("")
    
# Strength of One Bolt (B)
if C == 4.6:    
        print("Strength of One Bolt B is least of vdsb and vdpb")
        print("")
        Aₙb = 0.78* math.pi/4 * d**2
        Aₙb = round(Aₙb, 2)
        print("")
        print("Aₙb = 0.78*π/4 * d**2 ")
        print("")
        print("The Value of Aₙb is = ",Aₙb, "mm**2")
        print("")

        Aₛb = math.pi/4 *d**2
        Aₛb = round(Aₛb,2)
        print ("Aₛb = π/4*d**2 ")
        print("")
        print ("The Value of Aₛb is = ",Aₛb, "mm**2")
        print("")

        vdsb = fub/math.sqrt(3)*(nₙ* Aₙb + nₛ * Aₛb)/γₘb
        vdsb = round(vdsb/1000, 2)
        print("vdsb = fub/√3 *(nₙ* Aₙb + nₛ * Aₛb)/γₘb")
        print("")
        print("\033[31m Shearing Strength of Bolt : vdsb = ", vdsb, "KN\033[0m")
        print("")

        e = 1.5* dₒ
        print ("Minimum Edge distance (e)= 1.5 * dₒ ")
        print("")
        e = round_to_even(e)
        print ("The Edge distance = ",e, "mm")
        print("")

        p = 2.5 * d
        print ("Minimum Pitch distance (p) = 2.5 * d")
        print("")
        p = round_to_even(p)
        print("The Pitch Distance = ",p, "mm")
        print("")

        a= e/(3*dₒ)
        b= p/(3*dₒ)-0.25
        c= fub/fu
        D= 1.0
    
        Kb = min(a, b ,c, D)
        Kb = round (Kb,2)
        print ("The value of Kb = ",Kb)
        print("")
        print(" Now Bearing strength of one bolt: ")
        print("")

        vdpb = 2.5*Kb*d*t1*fub/γₘb
        vdpb = round(vdpb/1000, 2)
    
        print ("vdpb = 2.5*Kb*d*t1*fub/γₘb")
        print("")
        print (" \033[31m The Bearing Strength of One Bolt vdpb = ",vdpb, " KN\033[0m ")
        print("")

        B = min(vdsb,vdpb)
        print(" \033[31m Strength of One Bolt (B)= ",B, "KN\033[0m]")
        print("")
    
else:
        print("\033[31m Strength of One Bolt B = vdsf  \033[0m ")
        print("")
        μf = 0.55
        ne = nₙ
        Kh =1
        Aₙb = 0.78* math.pi/4 * d**2
        Aₙb = round(Aₙb, 2)
        print("Aₙb = 0.78*π/4 * d**2 ")
        print("")
        print("The Value of Aₙb is = ",Aₙb, "mm**2")
        print("")
        Fo = Aₙb * 0.7*fub
        vdsf = μf*ne*Kh*Fo/γₘf
        vdsf = round(vdsf/1000,2)
        print(" vdsf = μf*ne*Kh*Fo/γₘf ")
        print ("\033[31m Shear capacity for friction type bolts is = ", vdsf, "KN \033[0m")
        B= vdsf
        print("")
        print("\033[31mThe Strength of one Bolt B= ", B,"KN \033[0m")
        print("")

# Number of Bolts
N =1.5*P/B
N = round_to_even(N)
print("Number of Bolts required (N) = 1.5*P/B= ",N)
print("")
print("\033[31m Hence",N,"number of bolts are required \033[0m")

# Strength of joint
if C==4.6:
    print("Strength of joint Pd = least of Ps,Pb,Pt")
    print("")
    Ps= vdsb* N
    print ("\033[31m Ps=vdsb* N = ", Ps, "KN \033[0m")
    print("")
    Pb= vdpb * N
    Pb= round(Pb, 2)
    print("\033[31m Pb=vdpb*N = ",Pb, "KN \033[0m")
    print("")
    
else:
    print("\033[31mbStrength of joint Pd = least of Pf and Pt \033[0m")
    print("")
    Pf= vdsf*N
    print("Pf=vdsf*N = ",Pf, "KN")
    print("")

print("\033[31m Pt is least of Tdg and Tdn\033[0m")
Ag = b1*t1
print("")
print ("Yield Strength of plate if given by: ")
print("")
Tdg = Ag * fy /γₘₒ 
Tdg = round(Tdg/1000, 2)
print("Tdg = Ag * fy /γₘₒ = ", Tdg, "KN")
print("")
print("\033[31m Yield Strength of plate Tdg= ", Tdg, "KN \033[0m ")

print ("")
print("Rupture Strength of plate (Tdn)is given by:")
print("")

print ("Tdn = 0.9*An*fu/γₘₗ ")
print("")

n_n = int(input("\033[31m Number of Horizont lines of bolts \033[0m "))
print("")
An= (b1-n_n*dₒ)*t1
print("")
print("An= (b1-(n_n*)*dₒ)*t1 = ", An,"mm**2")
Tdn = 0.9*An*fu/γₘₗ
Tdn = round (Tdn/1000,2)
print("")

print ("\033[31m Tdn = 0.9*An*fu/γₘₗ = ", Tdn, "KN \033[0m ")
print("")

Pt= min(Tdg,Tdn)
print(" \033[31m Since Pt is least of Tdg and Tdn hence \033[0m ")
print ("\033[31m Pt= ",Pt, "KN\033[0m ")
print("")



#Strength of plate
print("Yield Strength of Plate = Tdg")
Tdg = Tdg
print("")
if C==4.6:
    print("\033[31m Strength of Joint is least of Ps,Pb,Pt \033[0m")
    Pd = min(Ps,Pb,Pt)
    print("")
    
    print("\033[31m Strength of Joint Pd = ", Pd, "KN \033[0m ")
    print("")
else:
    print(" Strength of Joint is least of Pf and Pt ")
    print("")
    Pd = min(Pf,Pt)
    print("\033[31m Strength of Joint Pd = ",Pd, "KN \033[0m ")
    print("")
    
#Efficiency of Joint
η = Pd/Tdg*100
η = round(η, 2)
print("Efficiency of joint η = Pd/Tdg*100 = ", η, "%")
print("")

print( "\033[31m Hence Efficiency of Joint = ",η,"% \033[0m")
print("")
print("")
print("")
print("{:>30}".format("\033[33mCredits:\n        Syed Shahid \033[0m"))
