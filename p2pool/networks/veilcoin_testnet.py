from p2pool.bitcoin import networks

PARENT=networks.nets['veilcoin_testnet']
SHARE_PERIOD=15 # seconds
CHAIN_LENGTH=24*60*60//10 # shares
REAL_CHAIN_LENGTH=24*60*60//10 # shares
TARGET_LOOKBEHIND=200 # shares
SPREAD=12 # blocks
IDENTIFIER='A06A81C827CAB973'.decode('hex')
PREFIX='A06A81C827CAB974'.decode('hex')
P2P_PORT=58814
MIN_TARGET=4
MAX_TARGET=2**256//2**20 - 1
PERSIST=False
WORKER_PORT=58815
BOOTSTRAP_ADDRS='veil.pool-address.com veil.pool-address2.com'.split(' ')
ANNOUNCE_CHANNEL='#p2pool-veil-testnet'
VERSION_CHECK=lambda v: True
SOFTFORKS_REQUIRED = set(['nversionbips', 'csv', 'segwit'])
SEGWIT_ACTIVATION_VERSION = 16
