# ----------------------------------------------------------------------------------
# BitBox02 plugin
#

import traceback
import sys

from electrum.keystore import Hardware_KeyStore

from ..hw_wallet import HW_PluginBase

class BitBox02Keystore(Hardware_Keystore)
    def get_derivation(self):
        return self.derivation

    def get_client(self, force_pair=True):
        return self.plugin.get_client(self, force_pair)

    def sign_transaction(self):
        print("just put this here for now")



class BitBox02Plugin(HW_PluginBase):
    BitBox02_Product_Key = 'BitBox02'
    device = BitBox02_Product_Key

    firmware_URL = 'https://github.com/digitalbitbox/bitbox02-firmware'
    libraries_URL = 'https://github.com/digitalbitbox/bitbox02-firmware/tree/master/py/bitbox02'
    #minimum_firmware = (1, 5, 2)
    keystore_class = BitBox02Keystore
    #minimum_library = (0, 11, 0)
    #maximum_library = (0, 12)
    SUPPORTED_XTYPES = ('standard', 'p2wpkh-p2sh', 'p2wpkh', 'p2wsh-p2sh', 'p2wsh')
    DEVICE_IDS = (BITBOX_PRODUCT_KEY,)

    def __init__(self, parent, config, name):
        HW_PluginBase.__init__(self, parent, config, name)

        self.libraries_available = self.check_libraries_available()
        if not self.libraries_available:
            return

        self.device_manager().register_devices(self.DEVICE_IDS)





