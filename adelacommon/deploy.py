from flask import current_app, Blueprint
from flask_migrate import upgrade, history
import os

deploy_cmd = Blueprint("deploy", __name__)

@deploy_cmd.cli.command('db-upgrade')
def db_upgrade():
    """Apply database migrations

    The migrations directory should be distribute along the application
    package
    """
    migrations_dir = os.path.join(current_app.root_path, "migrations")
    upgrade(directory=migrations_dir)


@deploy_cmd.cli.command('db-history')
def db_history():
    """Show database migrations history

    The migrations directory should be distribute along the application
    package
    """
    migrations_dir = os.path.join(current_app.root_path, "migrations")
    history(directory=migrations_dir, indicate_current=True)
