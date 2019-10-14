import time, os
from functools import partial

from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QPushButton, QLabel, QVBoxLayout, QWidget, QGridLayout
from PyQt5.QtWidgets import QFileDialog

from electrum.i18n import _
from electrum.plugin import hook
from electrum.wallet import Standard_Wallet
from electrum.gui.qt.util import WindowModalDialog, CloseButton, get_parent_main_window, Buttons
from electrum.transaction import Transaction

from .bitbox02 import BitBox02Plugin
from ..hw_wallet.qt import QtHandlerBase, QtPluginBase
from ..hw_wallet.plugin import only_hook_if_libraries_available

from binascii import a2b_hex
from base64 import b64encode, b64decode

CC_DEBUG = False

class Plugin(BitBox02Plugin, QtPluginBase):
    icon_unpaired = "coldcard_unpaired.png"
    icon_paired = "coldcard.png"

    def create_handler(self, window):
        return BitBox02_Handler(window)

    @only_hook_if_libraries_available
    @hook
    def receive_menu(self, menu, addrs, wallet):
        # Context menu on each address in the Addresses Tab, right click...
        if len(addrs) != 1:
            return
        for keystore in wallet.get_keystores():
            if type(keystore) == self.keystore_class:
                def show_address(keystore=keystore):
                    keystore.thread.add(partial(self.show_address, wallet, addrs[0], keystore=keystore))
                device_name = "{} ({})".format(self.device, keystore.label)
                menu.addAction(_("Show on {}").format(device_name), show_address)

class BitBox02_Handler(QtHandlerBase):
    setup_signal = pyqtSignal()
    #auth_signal = pyqtSignal(object)

    def __init__(self, win):
        super(BitBox02_Handler, self).__init__(win, 'Coldcard')
        self.setup_signal.connect(self.setup_dialog)
        #self.auth_signal.connect(self.auth_dialog)


