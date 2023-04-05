from rich import inspect, console
from PySide6.QtCore import Qt
import click
inspect(click.Command, help=True)
inspect(click.Argument, help=True)
inspect(Qt.DateFormat, help=True)