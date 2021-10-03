#import configparser
from freepybox.freepybox import Freepybox

#config = configparser.ConfigParser()
#config.sections()
#config.read('example.ini')

fbx = Freepybox()
fbx.open('mafreebox.freebox.fr', port=443)
fbx_config = fbx.lan.get_hosts_list()

for device in fbx_config:
    if device["active"] == True:
        for ips in device["l3connectivities"]:
            if ips["active"] == True and ips["af"] == "ipv4" and ips["reachable"] == True:
                ip_addr = ips["addr"]
                continue
        # if i want alternates names (mdns, etc.)
        # names = []
        # if "names" in device:
        #     for name in device["names"]:
        #         names.append(name["name"])
        #     names = set(names)
        #     names = ", ".join(list(names))
        # else:
        names = device["primary_name"]
        print(names, ip_addr, device["l2ident"]["id"], device["vendor_name"], device["host_type"])
