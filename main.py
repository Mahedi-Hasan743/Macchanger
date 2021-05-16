
import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change is mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="To change mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Kindly put a valid interface, or type -- help for more info")
    elif not options.new_mac:
        parser.error("kindly put a valid mac , or type --help for more info")
    return options


def change_mac(interface, new_mac):
    print("changing mac for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])



def search_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("could not find the mac address")




options = get_arguments()


current_mac =str(search_current_mac(options.interface))
print("current Mac = " + str(current_mac))

change_mac(options.interface,options.new_mac)

current_mac = search_current_mac(options.interface)


if current_mac == options.new_mac:
    print("mac address was successfully change to " + current_mac)
else:
    print('mac address did not get changed.')


