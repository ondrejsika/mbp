# MBP - My Bitcoin Payments

BIP44 ([Trezor](http://bitcointrezor.com)) payment processor.

- author: Ondrej Sika <ondrej@ondrejsika.com>
- license: [MIT](https://ondrejsika.com/license/mit.txt)

Tips are welcome to address [__1DhDxyquETrhKk3m6TkHreegr3yFmf8FkB__](https://blockchain.info/address/1DhDxyquETrhKk3m6TkHreegr3yFmf8FkB)

## Installation

Setup base project

    git clone git@github.com:ondrejsika/mbp.git
    cd mbp
    virtualenv .env
    source .env/bin/activate
    pip install -e .
    ./manage.py syncdb
    ./manage.py migrate
    ./manage.py createsuperuser
    ./manage.py collectstatic

Run in gunicorn

    gunicorn wsgi -b 0.0.0.0:9999

Setup cron job

    # add to your crontab
    */12 * * * * cd /home/projects/mbp && .env/bin/python manage.py confirm_transactions


## Live version

__<http://mbp.sikaapp.cz>__

