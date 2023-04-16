import os, sys
try:
    import fade
except IndexError:
    os.system("pip install fade")
    import fade
try:
    from colorama import Fore
except IndexError:
    os.system("pip install Fore")
    os.system("pip install colorama")
    from colorama import Fore
try:
    from pystyle import *
except IndexError:
    os.system("pip install pystyle")
    from pystyle import *
gui="""
    ╔════════════════════ ═══════╗ ╔════════════════════════╗
    ║╔╗ ╔═╗╔╗╔╔╗╔╔═╗╔═╗ ║ ║ [https://discord.gg/Zf7JuYeWAd]║
    ║╠╩╗║╣ ║║║║║║║╣ ╔═╝ ║ ║                                ║
    ║╚═╝╚═╝╝╚╝╝╚╝╚═╝╚═╝ ║ ║  [Project bennez#2060]         ║ 
    ╚═══════════════════════════╝ ╚════════════════════════╝
    ╔═══════════════════════════════════════════════════╗
    ║           [bennez#2060 Serial Checker]            ║
    ║       [!] https://discord.gg/Zf7JuYeWAd [!]       ║
    ╚═══════════════════════════════════════════════════╝
"""
os.system("@mode con cols=90 lines=56")
os.system("title oxycontin Serial Checker ^| Press any key to refresh")
faded_gui=fade.pinkred(gui)
while(True):
    os.system("cls")
    print(faded_gui)
    Write.Print("[</>] Baseboard\n", Colors.rainbow, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] Mac\n", Colors.rainbow, interval=0.001)
    os.system("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
    Write.Print("[</>] CPU\n", Colors.rainbow, interval=0.001)
    os.system("wmic cpu get processorid")
    Write.Print("[</>] GPU\n", Colors.rainbow, interval=0.001)
    os.system("wmic PATH Win32_VideoController GET Description,PNPDeviceID")
    Write.Print("[</>] DISK DRIVE\n", Colors.rainbow, interval=0.001)
    os.system("wmic diskdrive get serialnumber")
    Write.Print("[</>] MotherBoard\n", Colors.rainbow, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] RAM\n", Colors.rainbow, interval=0.001)
    os.system("wmic memorychip get serialnumber")
    Write.Print("[</>] Bios\n", Colors.rainbow, interval=0.001)
    os.system("wmic bios get serialnumber")
    Write.Print("[</>] smBios\n", Colors.rainbow, interval=0.001)
    os.system("wmic csproduct get uuid")





    os.system("pause >nul")
