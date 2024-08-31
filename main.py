#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Standard imports
import json
import time
from typing import Dict, List, Any, NoReturn

# 3rd-party Imports
import flet as ft

# Local imports
import utils
from libs.app_bar import AppBar
from libs.video_container import Video

def main(page: ft.Page) -> NoReturn:
    """
    Main function for PornHub app

    :params: page: Page control
    :return: None
    """
    # Window size
    resolution: List[str] = utils.get_screen_resolution()
    page.window.width = int(resolution[0]) - 150
    page.window.height = int(resolution[1]) - 150

    # Page padding and spacing
    page.padding = 0
    page.spacing = 0

    # Page background color
    page.bgcolor = "#000000"

    # App title
    page.title = "CornHub"

    # Initialize AppBar
    app_bar: AppBar = AppBar(
        page=page
    )

    # Initialize Page controls
    page_controls = ft.ListView(
        expand=True,
        spacing=0,
        padding=0,
        controls=[
            # App bar's controls
            app_bar.top_row(),
            app_bar.middle_row(),
            app_bar.bottom_tab(),

            # Little empty space
            ft.Text(
                value="", 
                height=10
            ),

            # AdBlocker banner
            adblocker_banner := ft.Container(
                width=page.width,
                height=30,
                bgcolor="#1b1b1b",
                # Main row
                content=ft.Row(
                    alignment="center",
                    width=page.width,
                    controls=[
                        # Info icon
                        ft.Icon(
                            name="info", 
                            color="#c6c6c6"
                        ),
                        # Banner text
                        ft.Text(
                            value=(
                                "If you are having issues with video "
                                "playback, please try disabling Adblock, "
                            ),
                            # Yellow text
                            spans=[
                                ft.TextSpan(
                                    text=(
                                        "contact Adblock support to "
                                        "fix the issue"
                                    ),
                                    style=ft.TextStyle(
                                        color="#ff9000"
                                    )
                                )
                            ],
                            size=10,
                            color="#c6c6c6"
                        ),
                        # Close icon
                        ft.IconButton(
                            icon="close", 
                            icon_color="#c6c6c6",
                            height=30,
                            style=ft.ButtonStyle(
                                padding=0
                            ),
                            on_click=lambda _: utils.remove_control(
                                page=page,
                                control=adblocker_banner
                            )
                        )
                    ]
                )
            ),

            # Divider
            ft.Divider(
                color="#2b2b2b"
            ),

            # Little empty space
            ft.Text(
                value="", 
                height=15
            ),

            # Video container (To have little padding around page)
            video_container := ft.Container(
                padding=25,
                content=ft.Column(
                    controls=[
                        # Porn videos title
                        ft.Text(
                            value="Hot Corn Videos in your region", 
                            size=20, 
                            color="#ffffff"
                        ),
                        # Tags row
                        ft.Row(
                            scroll=ft.ScrollMode.ALWAYS,
                            alignment="start",
                            # Tags
                            controls=[
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        value=i, 
                                        color="#c6c6c6", 
                                        weight="normal"
                                    ),
                                    bgcolor="#151515", 
                                    height=45,
                                    style=ft.ButtonStyle(
                                        side=ft.BorderSide(
                                            width=1,
                                            color="#242424"
                                        )
                                    )
                                ) for i in [
                                    "Step Corn",
                                    "Milf",
                                    "School girl",
                                    "Hardcorn",
                                    "monster",
                                    "corn",
                                    "lena corn",
                                    "submissive",
                                    "doggy corn",
                                    "Corn Khalifa", 
                                    "Russian",
                                    "corn mom",
                                    "cute corn"
                                ]
                            ]
                        ),
                        # Little empty space
                        ft.Text(
                            value="", 
                            height=10
                        )

                        # Videos will be added during running app
                    ]
                )
            )
        ]
    )

    # Add controls to page and wait for a second
    page.add(page_controls)
    time.sleep(1)

    # Load porn data
    with open("data.json", "r") as data:
        porn_data: Dict[str, str] = json.load(data)

    # Add videos to video container
    # Loop through videos in 4 sequences
    for i in range(0, len(porn_data) + 1, 4):
        # Continue if there is videos
        if porn_data[i-4:i]:
            # Initialize the row
            row: ft.Row = ft.Row(
                width=page.width,
                controls=[]
            )
            # Add videos to row
            for video in porn_data[i-4:i]:
                row.controls.append(
                    Video(video=video).build()
                )

            # Update video container
            video_container.content.controls.append(row)
            video_container.content.update()

# Run flet app
if __name__ == "__main__":
    ft.app(
        target=main
    )