from electrum.i18n import _

fullname = 'BitBox02'
description = _('Provides support for BitBox02 hardware wallet from Shift Cryptosecurity')
#requires = [('ckcc-protocol', 'github.com/Coldcard/ckcc-protocol')]
registers_keystore = ('hardware', 'BitBox02', _("BitBox02 Wallet"))
available_for = ['qt', 'cmdline']
