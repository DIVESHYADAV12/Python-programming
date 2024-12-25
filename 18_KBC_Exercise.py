print("........NAMASKAR DEVIYO AUR SAJJANO MAI AMITABH BAACHAN ")
print("AUR AAPKA SWAAGAT HAI KAUN BANEGA CAROREPATI ME .......")
print("")
name=str(input("Aapka Subh Naam : "))
print("")
# Quetions of the game
que=["1.Who is the current president of india?","2.Which is the largest country in the world according to area?",
"3.which countary has the largest population in the world?"]
# Otions of Each questions
opt=["  A.Nirmala Sitaraman   B.Narendra Modi   C.Draupadi Murmu   D.Bahubali",
"   A.Russia   B.China   C.India   D.U.S.A",
"   A.Japan   B.Bangladesh   C.China   D.India"]
i=0
while(i<len(que)):
    if(i==0):
        print("Pehla Sawal 10 Laakh Rupye K Lie Aapki computer Screen pe ye rha...")
        print("")
        print(que[i])
        print("")
        print(opt[i])
        print("")
        x=str(input(" Aapna Option Chuniye : "))
        print("")
        match x.lower():
            case 'c':
                print("Mubarak ho aap jeete chuke hai 10 Lakh Rupyeee....🥳")
                print("")
                y=str(input("Kya aap aage khelna chahenge ya 10 laakh ghar le jana chahenge >>>\n\n1.Aage khelne k lie likhe \'YES\'. \n2.Game chor kar jaane k lie likhe \'NO\' \n\n"))
                match y.lower():
                    case 'yes':
                        print("")
                    case 'no':
                        print("")
                        print("Aapka safar yhi tak tha...")
                        print("")
                        print("Ammount credited : 1000000")
                        break
            case _:
                print("Afsos Aaj aap yaha se koi Dhanrahi lekar nhi jayenge.....😔")
                break
                
    
    if(i==1):
        print("\n")
        print("Dusra Sawal 1 crore Rupye K Lie Aapki computer Screen pe ye rha...")
        print("")
        print(que[i])
        print("")
        print(opt[i])
        print("")
        x=str(input(" Aapna Option Chuniye : "))
        print("")
        match x.lower():
            case 'a':
                print("Mubarak ho aap jeete chuke hai 1 crore Rupyeeee....🥳")
                print("")
                y=str(input("Kya aap aage khelna chahenge ya 10 laakh ghar le jana chahenge >>>\n\n1.Aage khelne k lie likhe \'YES\'. \n2.Game chor kar jaane k lie likhe \'NO\' \n\n "))
                match y.lower():
                    case 'yes':
                        print("")
                    case 'no':
                        print("")
                        print("Aapka safar yhi tak tha...")
                        print("")
                        print("Ammount credited : 10000000")
                        break
            case _:
                print(" Afsos Aaj aap yaha se keval 10  Lakh rupye lekar jayenge.....😔")
                print(name,"ji ye gye 10 lakh seedhe aapke account me")
                print("")
                print("Ammount credited : 1000000")
                break

    if(i==2):
        print("\n")
        print("Teesra Sawal 7 crore Rupye K Lie Aapki computer Screen pe ye rha...")
        print("")
        print(que[i])
        print("")
        print(opt[i])
        print("")
        x=str(input(" Aapna Option Chuniye : "))
        print("")
        match x.lower():
            case 'd':
                print(" 7 crorreeeeeeeee!!!!!!!!!!")
                print("")
                print(name,"ji 7 crore seedha aapke bank account me.....!!!!!!!!")
                print("")
                print("Ammount credited : 70000000")
            case _:
                print(" Afsos Aaj aap yaha se keval 1 crore le kar jayenge.....😔")
                print("")
                print("Ammount credited : 10000000")
    i=i+1                      
    