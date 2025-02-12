# -*- coding: utf-8 -*-

__author__ = "Ash Christopher"
__email__ = "ash.christopher@gmail.com"

from django.db.backends.postgresql import base
from django.db.backends.postgresql.client import DatabaseClient

from ._version import __version__  # noqa: F401


class PgCLIDatabaseClient(DatabaseClient):
    executable_name = "pgcli"

    def runshell(self, parameters=None):
        super().runshell(parameters=parameters)
        # PgCLIDatabaseClient.runshell_db(self.connection.get_connection_params(), parameters=parameters)


base.DatabaseWrapper.__old_database_client_class = base.DatabaseClient  # type: ignore
base.DatabaseWrapper.client_class = PgCLIDatabaseClient
