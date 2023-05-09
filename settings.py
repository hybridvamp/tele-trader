# Bot token provided by BotFather

# TOKEN_TEST = "852053528:AAHL_ryUUJ1JOhenzmI0WDiayAnxxqGFmyU"
from sqlalchemy import create_engine


# PUBLIC_KEY = "953b0c668c9d75c2d3da984f62a00fd269dc66c6da701250a0d7e14b52449183"
# PRIVATE_KEY = "c68f21F77B13FE4D6617EfcD0287c036da7A3aB1A5f3e870fb179E940F5839Dd"
# Merchant_ID = "c4baf6ef23be73a2da7fa0531b2df323"
# IPN_secret = "coinpaymentspeaks"
# ADMIN_ID = 1053579181

DEBUG = True

if DEBUG == False:
    print("\033[1;35;40m Running in production mode")
    TOKEN = "852053528:AAEOdgDErcNtHbbK2E-80uSFmF5tsCeJdSc"  # FCX trading bot
    URL = 'https://8828-richardokoni-teletrader-1q4ifr00tyi.ws-eu96b.gitpod.io/'
    try:
        import os
        DATABASE_URL = os.environ['DATABASE_URL']
    except KeyError:
        # DATABASE_URL="postgres://oilzaezgbpfuad:0c38dcf0bdd1cad9456aff15f7b6ae3cb076e5911dcbb5bf266afd5a3710e608@ec2-184-72-236-57.compute-1.amazonaws.com:5432/d3u443uoa0b5os"
        # DATABASE_URL = "postgres://jiuyexwrlknkee:183e46190d220e36b4401f4d6d86549ba7107653bb62ddadec6bccecd02c366a@ec2-54-246-89-234.eu-west-1.compute.amazonaws.com:5432/daprusoucv4h82"
        # DATABASE_URL = 'mysql://o0o1vr0hworagxo8ehdp:pscale_pw_TNVjf1YgB4OMXcwseOUYAwahFNGhWm8TU2ehfwcjgml@aws.connect.psdb.cloud/testdb?sslaccept=strict'
        DATABASE_URL = "postgres://default:HlJzr0v6eyGp@ep-calm-brook-757839.us-east-1.postgres.vercel-storage.com:5432/verceldb"
    db_url = DATABASE_URL.split(":")

    DATABASE_URI_VAR = f'postgres+psycopg2:{db_url[1]}:{db_url[2]}:{db_url[3]}'
    engine = create_engine(DATABASE_URI_VAR, echo=True)
    print(engine)

else:
    print("\033[1;32;40m Running in Development mode")
    TOKEN = "852053528:AAEOdgDErcNtHbbK2E-80uSFmF5tsCeJdSc"
    # TOKEN = "746406709:AAHGsGOKxHwPOhRMdUOM5JNKsVxI2cCTbyQ" #fcxtrader bot
    # URL = "https://3a7a746b.ngrok.io/"
    # URL = 'https://8828-richardokoni-teletrader-1q4ifr00tyi.ws-eu96b.gitpod.io/'
    URL = 'https://5000-richardokoni-teletrader-1q4ifr00tyi.ws-eu96b.gitpod.io/'
    # DATABASE_URL = 'mysql://o0o1vr0hworagxo8ehdp:pscale_pw_TNVjf1YgB4OMXcwseOUYAwahFNGhWm8TU2ehfwcjgml@aws.connect.psdb.cloud/testdb?sslaccept=strict'
    # DATABASE_URL = 'postgres+psycopg2://postgres:postgres@localhost:5432'
    # DATABASE_URL = "postgres://default:HlJzr0v6eyGp@ep-calm-brook-757839.us-east-1.postgres.vercel-storage.com:5432/verceldb"
    ADMIN_ID = 1053579181

    SQLITE = 'sqlite:///database/database.db'
    engine = create_engine(SQLITE, echo=True, connect_args={
                           'check_same_thread': False})
    print(engine)
