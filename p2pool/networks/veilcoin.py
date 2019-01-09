from p2pool.bitcoin import networks

PARENT=networks.nets['veilcoin']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='A06A81C827CAB984'.decode('hex')
PREFIX='A06A81C827CAB985'.decode('hex')
P2P_PORT=58816
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=58817
BOOTSTRAP_ADDRS='explorer.veil-project.com veil.pool-address.com'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-veil'
VERSION_CHECK=lambda v: True
#SOFTFORKS_REQUIRED = set(['bip65', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 17
MINIMUM_PROTOCOL_VERSION = 70000
NEW_MINIMUM_PROTOCOL_VERSION = 70020
