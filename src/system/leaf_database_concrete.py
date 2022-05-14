
""" System Leaf Database """

import datetime
import sqlite3 as db
from .leaf_database_abc import LeafDatabaseAbc

class LeafDatabaseConcrete(LeafDatabaseAbc):

    def __init__(self, p_database_name:str, p_table_name:str) -> None:
        self.database_name = p_database_name
        self.table_name = p_table_name
        self.connection = self._connect_to_db(self.database_name)
        self.cursor = self._get_db_cursor(self.connection)

    def save_information(self,
            p_system:str,
            p_node:str,
            p_release:str,
            p_version:str,
            p_machine:str,
            p_total_ram:str,
            p_cpu_count:str) -> None:

        if(self._check_if_table_exists(self.cursor, self.database_name)):
            self._insert_into_table(
                    self.cursor,
                    self.table_name,
                    p_system,
                    p_node,
                    p_release,
                    p_version,
                    p_machine,
                    p_total_ram,
                    p_cpu_count)
        else:
            self._create_table(self.cursor, self.table_name)
            self._insert_into_table(
                    self.cursor,
                    self.table_name,
                    p_system,
                    p_node,
                    p_release,
                    p_version,
                    p_machine,
                    p_total_ram,
                    p_cpu_count)

        self._commit_changes(self.connection)

    def _connect_to_db(self, p_db_name:str) -> db.Connection:

        connection = db.connect(p_db_name)

        return connection

    def _get_db_cursor(self, p_connection:db.Connection) -> db.Cursor:

        cursor = p_connection.cursor()
        
        return cursor

    def _check_if_table_exists(self,
            p_cursor:db.Cursor,
            p_table_name:str) -> bool:

        sql_cmd = ("" +
            "SELECT name FROM sqlite_master " +
            "WHERE type='table' " +
            f"AND name='{p_table_name}';")

        table = p_cursor.execute(sql_cmd).fetchall()

        if table:
            return True
        else:
            return False

    def _create_table(self, p_cursor:db.Cursor, p_table_name:str) -> None:

        sql_cmd = ("" +
            "CREATE TABLE IF NOT EXISTS {} ( ".format(p_table_name) +
            "id INTEGER PRIMARY KEY, " +
            "timestamp TIMESTAMP, " +
            "system TEXT NOT NULL, " +
            "node TEXT NOT NULL, " +
            "release TEXT NOT NULL, " +
            "version TEXT NOT NULL, " +
            "machine TEXT NOT NULL, " +
            "total_ram TEXT NOT NULL, " +
            "cpu_count TEXT NOT NULL); ")

        p_cursor.execute(sql_cmd)


    def _insert_into_table(self,
            p_cursor: db.Cursor,
            p_table_name:str,
            p_system:str,
            p_node:str,
            p_release:str,
            p_version:str,
            p_machine:str,
            p_total_ram:str,
            p_cpu_count:str) -> None:

        sql_cmd = ("" +
            "REPLACE INTO {} VALUES ".format(p_table_name) +
            "('1'," +
            "'{}',".format(datetime.datetime.now()) +
            "'{}',".format(p_system) +
            "'{}',".format(p_node) +
            "'{}',".format(p_release) +
            "'{}',".format(p_version) +
            "'{}',".format(p_machine) +
            "'{}',".format(p_total_ram) +
            "'{}');".format(p_cpu_count))

        p_cursor.execute(sql_cmd)

    def _commit_changes(self, p_connection:db.Connection) -> None:
        p_connection.commit()

