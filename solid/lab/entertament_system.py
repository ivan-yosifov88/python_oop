class HdmiConnectable:
    def connect_to_device_via_hdmi_cable(self, device):
        pass


class RcaConnectable:
    def connect_to_device_via_rca_cable(self, device):
        pass


class EthernetConnectable:
    def connect_to_device_via_ethernet_cable(self, device):
        pass


class PowerOutlet:
    def connect_device_to_power_outlet(self, device): pass


class Television(HdmiConnectable, RcaConnectable, PowerOutlet):
   pass


class DvdPlayer(HdmiConnectable, PowerOutlet):
   pass


class GameConsole(HdmiConnectable, EthernetConnectable, PowerOutlet):
    pass


class Router(EthernetConnectable, PowerOutlet):
    pass

