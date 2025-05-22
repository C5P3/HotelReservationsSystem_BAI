import os
import sqlite3
from typing import Optional, Tuple, List, Any

class BaseDataAccess:
    def __init__(self, db_connection_str: Optional[str] = None):
        """Initialisiert die Datenbankverbindung.
        Args:
            db_connection_str: Pfad zur SQLite-DB. Falls None, wird die Umgebungsvariable DB_FILE verwendet.
        Raises:
            Exception: Wenn kein Datenbankpfad gesetzt ist.
        """
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE")
            if self.__db_connection_str is None:
                raise Exception("DB_FILE environment variable and parameter db_connection_str are not set.")
        else:
            self.__db_connection_str = db_connection_str

    def _connect(self) -> sqlite3.Connection:
        """Erstellt eine Verbindung zur SQLite-DB."""
        conn = sqlite3.connect(
            self.__db_connection_str,
            detect_types=sqlite3.PARSE_DECLTYPES  # Ermöglicht das automatische Parsen von Datentypen (z. B. datetime).
        )
        conn.row_factory = sqlite3.Row
        return conn

    def fetchone(self, sql: str, params: Optional[Tuple] = None) -> Optional[Any]:
        """Führt eine SQL-Abfrage aus und gibt eine Zeile zurück.
        Args:
            sql: SQL-Query mit Platzhaltern (`?`).
            params: Parameter für die Query.
        Returns:
            Ein Tupel mit den Werten der Zeile oder None, wenn kein Ergebnis.
        """
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                return cur.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e

    def fetchall(self, sql: str, params: Optional[Tuple] = None) -> List[Any]:
        """Führt eine SQL-Abfrage aus und gibt alle Zeilen zurück.
        Args:
            sql: SQL-Query mit Platzhaltern (`?`).
            params: Parameter für die Query.
        Returns:
            Eine Liste von Tupeln (Zeilen) oder eine leere Liste.
        """
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                return cur.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e

    def execute(self, sql: str, params: Optional[Tuple] = None) -> Tuple[int, int]:
        """Führt eine INSERT/UPDATE/DELETE-Query aus.
        Args:
            sql: SQL-Query mit Platzhaltern (`?`).
            params: Parameter für die Query.
        Returns:
            (lastrowid, rowcount): ID der letzten Zeile & Anzahl betroffener Zeilen.
        """
        if params is None:
            params = ()
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                conn.commit()
                return cur.lastrowid, cur.rowcount
            except sqlite3.Error as e:
                conn.rollback()
                raise e