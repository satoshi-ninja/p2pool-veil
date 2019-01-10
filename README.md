# Requirements:

## Generic:
* Veil >= 1.0.0.6 --> https://github.com/Veil-Project/veil/releases
* Python >=2.6
* Twisted >=10.0.0

## Linux:
* Install the following required packages: 
```sh
sudo apt-get install python-rrdtool python-pygame python-scipy python-twisted python-twisted-web python-pil python-setuptools`
```

## Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

# Running P2Pool:
To use P2Pool, you must be running your own local veild. For standard configurations, using P2Pool should be as simple as:
```sh
    cd x16rt_hash
    git submodule init
    git submodule update
    sudo python setup.py install
    python test.py
    cd ../
    python run_p2pool.py --net veil (--testnet) -a <your mining address here> <rpcuser> <rpcpassword>
```
Then run your miner program, connecting to 127.0.0.1 on port 58817 (mainnet) or port 58815 (testnet) with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your router. Forward port 58816 (mainnet) or 58814 (testnet) to the host running P2Pool.

Run for additional options.
```
    python run_p2pool.py --help
```

# Official P2Pool wiki:
* https://en.bitcoin.it/wiki/P2Pool

# Alternate web frontend:
* https://github.com/hardcpp/P2PoolExtendedFrontEnd

# License:
* [Available here](COPYING)


