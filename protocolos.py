OSPF = 110
RIP = 120
EIGRP = 90
BGP = 20

protocolo = input("Ingrese protocolo: ").upper()

if protocolo == "OSPF":
    print(f"{protocolo} = {OSPF}")
elif protocolo == "RIP":
    print(f"{protocolo} = {RIP}")
elif protocolo == "EIGRP":
    print(f"{protocolo} = {EIGRP}")
elif protocolo == "BGP":
    print(f"{protocolo} = {BGP}")
else:
    print("Protocolo no reconocido")
