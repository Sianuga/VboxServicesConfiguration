import subprocess
import virtualbox 
import time


# Wybór konfiguracji usługi
def configure_service(service_name, session, session2):
    if service_name == "DNS":
        # Logika konfiguracji usługi DNS
        print("Konfiguracja usługi DNS")
        return True
    elif service_name == "DHCP":
        # Logika konfiguracji usługi DHCP
        print("Konfiguracja usługi DHCP")
        return True
    elif service_name == "NFS":
        # Logika konfiguracji usługi NFS
        print("Konfiguracja usługi NFS")
        return True
    elif service_name == "SAMBA":
        # Logika konfiguracji usługi SAMBA
        print("Konfiguracja usługi SAMBA")
        return True
    elif service_name == "FTP":
        # Logika konfiguracji usługi FTP
        print("Konfiguracja usługi FTP")
        return True
    elif service_name == "WWW":
        # Logika konfiguracji usługi WWW
        print("Konfiguracja usługi WWW")
        create_www_server(session, session2)  
        return True  
    elif service_name == "FINISH":
        print("Zakończono skrypt")
        return False
    else:
        print("Nieprawidłowa usługa")
        return True



def create_www_server(session, session2):
    wantHTML = input("Do you want to create HTML configuration? (Y/N): ")
    folderName = input("Give folder name: ")
    port = input("Give port number (default: 80): ")
    if wantHTML == "Y":
     
        session2.console.keyboard.put_keys("sudo apt update"+ 
                                      "; sudo apt install links"+
                                        "; sudo apt install apache2"+
                                        f"; sudo mkdir -p /var/www/{folderName}/html"+
                                        f"; sudo touch /var/www/{folderName}/html/index.html"+
                                        f"; sudo echo -e '<html>\n<body>\n<p>HELLO WORLD</p>\n</body>\n</html>' | sudo tee /var/www/{folderName}/html/index.html"+
                                        f"; sudo chown -R $USER:$USER /var/www/{folderName}/html"+
                                        f"; sudo chmod -R 755 /var/www/{folderName}"+
                                        "; sudo nano /etc/apache2/sites-available/000-default.conf"+
                                        "; sudo nano /etc/apache2/apache2.conf"+
                                        "; sudo service restart apache2"+
                                        "; links 10.1.2.102"+
                                      f'\n')
    else:
        print("PHP")
        


def main():
    print("Welcome to the script configuring your VMs! The setup is in progress")
    print("DO NOT START CONFIGURING UNTIL THE VMs ARE UP AND RUNNING")
    vbox = virtualbox.VirtualBox()
    session = virtualbox.Session()
    session2 = virtualbox.Session()
    machine = vbox.find_machine("vm1")
    machine2 = vbox.find_machine("vm2")
    progress = machine.launch_vm_process(session, "gui", [])
    time.sleep(2)
    progress2 = machine2.launch_vm_process(session2, "gui", [])
    progress.wait_for_completion()
    progress2.wait_for_completion()

    while True:
        toConfigure = input("What do you want to configure? (DNS, DHCP, NFS, SAMBA, FTP, WWW, FINISH): ")
        if not configure_service(toConfigure, session, session2):
            break
    
    print("Program finished successfully, turning off VMs")

    session.console.power_down()
    session2.console.power_down()



main()