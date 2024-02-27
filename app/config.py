from twelve_factor_app_framework.bootstrap import app

app = app
borrowing_app = app()
logger = app.logger
config = app.config
