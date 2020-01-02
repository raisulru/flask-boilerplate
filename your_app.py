import os
from main import create_app
from config import Config
# from commands import register_cli_handlers
# from logger import configure

is_gunicorn = "gunicorn" in os.environ.get("SERVER_SOFTWARE", "")

app = create_app(config_class=Config)
# register_cli_handlers(app)
# if app.config['LOGGER_ENABLED']:
#     configure(app, is_gunicorn)

if __name__ == "__main__":
    app.run(debug=True)
