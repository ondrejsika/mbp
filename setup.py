from setuptools import setup, find_packages


setup(
    name='mbp',
    version='0.0.0',
    description='BIP44 (Trezor) payment processor.',
    url='https://github.com/ondrejsika/mbp',
    author='Ondrej Sika',
    author_email='ondrej@ondrejsika.com',
    packages=find_packages(),
    install_requires=[
        'Django==1.6.11',
        'Pillow==3.1.1',
        'South==1.0.2',
        'bip32utils==0.3-1',
        'blockchain==1.2.1',
        'django-debug-toolbar==1.3.0',
        'ecdsa==0.13',
        'gunicorn==19.4.5',
        'psycopg2==2.6.1',
        'qrcode==5.2.2',
     ],
)
