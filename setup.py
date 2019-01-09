from setuptools import setup

setup(name='p2pool-veil',
      version='1.0.0',
      description='p2pool for Veil',
      url='http://github.com/satoshi-ninja/p2pool-veil',
      license='GPLv3',
      author = 'Satoshi Ninja',
      author_email = 'satoshi.ninja@protonmail.com',
      packages=['p2pool','p2pool/bitcoin','p2pool/bitcoin/networks','p2pool/util','p2pool/networks', 
                'nattraverso', 'nattraverso/pynupnp'],
      install_requires=[
          'twisted',
          'argparse',
          'pyOpenSSL'
      ],
      scripts=['run_p2pool.py'],
      include_package_data=True,
      zip_safe=False)
