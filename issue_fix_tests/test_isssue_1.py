import io
import sys
from types import ModuleType
from typing import Sequence, Type

import pytest

from rich import inspect
from rich._inspect import (
    get_object_types_mro,
    get_object_types_mro_as_strings,
    is_object_one_of_types,
)
from rich.console import Console

import click

def render(obj, methods=False, value=False, width=76) -> str:
    console = Console(file=io.StringIO(), width=width, legacy_windows=False)
    inspect(obj, console=console, methods=methods, value=value, help=True)
    return console.file.getvalue()

    
def test_argument_printing():    
    expected = (
        "╭────────────────────── <class 'click.core.Command'> ──────────────────────╮\n"
        "│ class Command(                                                           │\n"
        "│         name: Optional[str],                                             │\n"
        "│         context_settings: Optional[Dict[str, Any]] = None,               │\n"
        "│         callback: Optional[Callable[..., Any]] = None,                   │\n"
        "│         params: Optional[List[ForwardRef('Parameter')]] = None,          │\n"
        "│         help: Optional[str] = None,                                      │\n"
        "│         epilog: Optional[str] = None,                                    │\n"
        "│         short_help: Optional[str] = None,                                │\n"
        "│         options_metavar: Optional[str] = '[OPTIONS]',                    │\n"
        "│         add_help_option: bool = True,                                    │\n"
        "│         no_args_is_help: bool = False,                                   │\n"
        "│         hidden: bool = False,                                            │\n"
        "│         deprecated: bool = False                                         │\n"
        "│ ) -> None:                                                               │\n"
        "│                                                                          │\n"
    )
    assert render(click.Command).startswith(expected)