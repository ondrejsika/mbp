# MBP - My Bitcoin Payments

BIP44 ([Trezor](http://bitcointrezor.com)) payment processor.

- author: Ondrej Sika <ondrej@ondrejsika.com>
- license: [MIT](https://ondrejsika.com/license/mit.txt)

Tips are welcome to address [__1DhDxyquETrhKk3m6TkHreegr3yFmf8FkB__](https://blockchain.info/address/1DhDxyquETrhKk3m6TkHreegr3yFmf8FkB)

## Installation

Setup base project

    git clone git@github.com:ondrejsika/mbp.git
    cd mbp
    cp setting_local--template.py settings_local.py
    # edit settings_local.py
    vim settings_local.py
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


### Settings

- `DATABASE_*` - configurate DB connection
- `ORIGIN` - site origin like `https://mbp.sikaapp.cz` in production, `http://localhost:8000` in development
- `DEFAULT_XPUB` - default xpub used for new profiles, if custom xpubs are disabled
- `DEBUG_TOOLBAR_PATCH_SETTINGS` - must be `False` if site run in gunicorn

## Live version

Live:

- <https://mbp.sikaapp.cz>

Demo:

- <https://mbp-demo.sikaapp.cz>
- user: __demo__
- password: __demo__
