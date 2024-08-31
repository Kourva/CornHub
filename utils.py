#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard imports
import subprocess
from typing import List, NoReturn, Any

# 3rd-party imports
import flet as ft

# Local imports

def get_screen_resolution() -> List[str]:
    """
    Helper function to get screen resolution from shell

    :params: None
    :return: Width and Height inside list
    """
    resolution: str = subprocess.run(
        "xrandr | grep '\\*' | cut -d' ' -f4",
        shell=True, 
        stdout=subprocess.PIPE
    ).stdout.decode("utf-8")

    return resolution.strip().split("x")


def remove_control(page: ft.Page, control: Any) -> NoReturn:
    """
    helper function to remove control from list view

    :params:
        page: Flet page
        control: Target control

    :return: None
    """
    # Initialize main list view
    list_view: Ft.ListView = page.controls[0]
    
    # Try to find the index of the control and pop it
    try:
        target: Any = list_view.controls.index(control)
        list_view.controls.pop(target)

    # Handle exception
    except Exception as e:
        print(e)

    # Update the list view
    finally:
        list_view.update()

