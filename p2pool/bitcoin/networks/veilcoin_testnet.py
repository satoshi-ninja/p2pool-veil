import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX='a8d1a7c4'.decode('hex')
P2P_PORT=58811
ADDRESS_VERSION=111
SEGWIT_ADDRESS_VERSION=196
RPC_PORT=58813
RPC_CHECK=lambda bitcoind: True
SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000
POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('lyra2re3_hash').getPoWHash(data))
BLOCK_PERIOD=60 # s
SYMBOL='VEILTEST'
CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Vertcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Vertcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.vertcoin'), 'vertcoin.conf')
BLOCK_EXPLORER_URL_PREFIX='http://test.vtc.sovereignshare.com/exp/#/vtctest/'
ADDRESS_EXPLORER_URL_PREFIX='http://test.vtc.sovereignshare.com/exp/#/vtctest/address/'
TX_EXPLORER_URL_PREFIX='http://test.vtc.sovereignshare.com/exp/#/vtctest/tx/'
SANE_TARGET_RANGE=(2**256//1000000000000000000 - 1, 2**256//100000 - 1)
DUMB_SCRYPT_DIFF=256
DUST_THRESHOLD=0.03e8
HUMAN_READABLE_PART = 'tveil'
