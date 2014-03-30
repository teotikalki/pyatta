#!../bin/python

import sys
sys.path.append('../')
from ExecFormat import ExecutorFormator
from ConfigOpt import config_opt
from RoutingService import routingservice
IOV="interfaces openvpn vtun"
class openvpn(config_opt):
    exe = ExecutorFormator()    
    RS = routingservice()

    def shared_keygen():
        # run generate openvpn key <filename>
        pass
    #@staticmethod
    def openvpn_config(self,iface_num,suffix=[]):
        openvpn_params=[IOV+iface_num]
        openvpn_params.extend(suffix)
        self.set(openvpn_params)
    
    def set_interface_vpn(self,iface_num):
        self.openvpn_config(iface_num)        

    def set_endpoint_local_vaddr(self,iface_num,local_vaddr):
        suffix=["local-address",local_vaddr]
        self.openvpn_config(iface_num,suffix)

    def set_vpn_mode(self,iface_num,mode):
        suffix=["mode",mode]
        self.openvpn_config(iface_num,suffix)

    def set_endpoint_remote_vaddr(self,iface_num,remote_vaddr):
        suffix=["remote-address",remote_vaddr]
        self.openvpn_config(iface_num,suffix)

    def define_remote_host(self,iface_num,remote_host):
        suffix=["remote-host",remote_host]
        self.openvpn_config(iface_num,suffix)

    def sharedkey_file_path(self,iface_num,path):
        suffix=["shared-secret-key-file",path]
        self.openvpn_config(iface_num,suffix)

    def set_access_route_vpn(self,iface_num,dst_subnet):
        self.RS.set_interface_route(dst_subnet,"vtun"+iface_num)

    def set_tls_role(self,iface_num,role):
        suffix=["tls role",role]
        self.openvpn_config(iface_num,suffix)
    
    def define_files(self,iface_num,typefile,abspath):
        suffix=["tls",typefile+"-file",abspath]
        self.openvpn_config(iface_num,suffix)

    def del_vpn_iface(self,iface_num):
        openvpn_params=[IOV+iface_num]
        self.delete(openvpn_params)
        self.exe.commit()
        self.exe.save()

    def set_server_range_addr(self,iface_num,subnet):
        suffix=["server subnet",subnet+"/24"]
        self.openvpn_config(iface_num,suffix)

    def push_root_subnet(self,iface_num,subnet): 
        suffix=["server push-route",subnet+"/24"]
        self.openvpn_config(iface_num,suffix)

    def push_root_nameserver(self,iface_num,nameserver):
        suffix=["server name-server",nameserver]
        self.openvpn_config(iface_num,suffix)

obj=openvpn()
obj.set_interface_vpn("0")
obj.set_vpn_mode("0","server")
obj.set_server_range_addr("0","10.1.1.0")
obj.push_root_subnet("0","172.168.1.0")
obj.define_files("0","ca-cert","/config/auth/ca.crt")
obj.define_files("0","cert","/config/auth/vyos-server.crt")
#obj.define_files("0","crl","/config/auth/01.pem")
obj.define_files("0","dh","/config/auth/dh1024.pem")
obj.define_files("0","key","/config/auth/vyos-server.key")
obj.exe.commit()
obj.exe.save()

#obj.set_endpoint_local_vaddr("0","192.168.100.1")
#obj.set_endpoint_remote_vaddr("0","192.168.100.2")
#obj.define_remote_host("0","172.168.1.22")
#obj.sharedkey_file_path("0","/config/auth/zomta3key")
#obj.set_access_route_vpn("0","192.168.1.0")
#obj.del_vpn_iface("0")