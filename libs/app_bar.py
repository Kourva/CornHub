#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Github: https://github.com/Kourva/CornHub

# Standard imports
from typing import Self, NoReturn

# 3rd-Party imports
import flet as ft

class AppBar:
    """Custom AppBar"""
    def __init__(self: Self, page: ft.Page) -> NoReturn:
        """
        Initial method of class
        
        :params: page: Page control
        :return: None
        """
        self.page: ft.page = page

    def top_row(self: Self) -> ft.Row:
        """
        Method to return app bar's top row

        :params: Self
        :return: ft.Row
        """
        # Main row
        return ft.Row(
            spacing=30,
            alignment="center",
            controls=[
                # Expanded divider
                ft.Icon(
                    name="info_outline", 
                    color="#888888", 
                    size=15
                ),
                *list(
                    ft.Text(
                        value=i,
                        color="#888888",
                        size=12
                    ) for i in [
                        "SEXUAL WELLNESS",
                        "INSIGHTS",
                        "SITES",
                        "SHOP",
                        "TRUST & SAFETY",
                        "EN"
                    ]
                )
            ]
        )

    def middle_row(self: Self) -> ft.Container:
        """
        Method to return app bar's middle row

        :params: Self
        :return: ft.Container
        """
        # Main Container
        # I used container to set background color to row
        return ft.Container(
            width=self.page.width,
            height=70,
            bgcolor="#0e0e0e",

            # Main row
            content=ft.Row(
                spacing=5,
                controls=[
                    # Little empty space
                    ft.Text(
                        value="", 
                        width=5
                    ),

                    # Menu icon
                    ft.IconButton(
                        icon="menu",
                        icon_color="#ff9000",
                        icon_size=30
                    ),

                    # PornHub logo image
                    ft.Image(
                        src="./logo.png",
                        height=70,
                        fit="fill"
                    ),

                    # Expanded divider
                    ft.Text(
                        value="",
                        expand=True
                    ),

                    # Search bar
                    ft.SearchBar(
                        width=500,
                        height=40,
                        full_screen=True,
                        view_elevation=4,
                        bar_bgcolor="#242424",
                        bar_hint_text="Search Cornhub",
                        view_hint_text="Search or Choose trending corns.",
                        # Leading search icon 
                        bar_leading=ft.Icon(
                            name="search", 
                            color="#c6c6c6"
                        )
                    ),

                    # Another little empty space
                    ft.Text(
                        value="", 
                        width=5
                    ),

                    # Video icon
                    ft.IconButton(
                        icon="smart_display",
                        icon_color="#c6c6c6",
                        icon_size=30
                    ),

                    # Photo icon
                    ft.IconButton(
                        icon="photo_camera",
                        icon_color="#c6c6c6",
                        icon_size=30
                    ),

                    # Another another little empty space
                    ft.Text(
                        value="", 
                        expand=True
                    ),

                    # Account icon
                    ft.IconButton(
                        icon="account_circle",
                        icon_color="#c6c6c6",
                        icon_size=30
                    ),

                    # Another another another little empty space
                    ft.Text(
                        value="", 
                        width=5
                    )
                ]
            )
        )

    def bottom_tab(self: Self) -> ft.Container:
        """
        Method to return app bar's bottom tab

        :params: Self
        :return: ft.Container
        """
        # Main Container
        # I used container to set background color to row 
        return ft.Container(
            width=self.page.width,
            height=40,
            bgcolor="#0e0e0e",

            # Segment button
            content=ft.CupertinoSegmentedButton(
                selected_index=0,
                border_color="#0e0e0e",
                selected_color="#00000000",
                unselected_color="#00000000",

                # Tabs
                controls=[
                    # Home tab (with bottom border)
                    ft.Container(
                        width=self.page.width/1.2,
                        border=ft.border.only(
                            bottom=ft.border.BorderSide(
                                width=3, 
                                color="#ff9000"
                            )
                        ),
                        content=ft.Text(
                            value="HOME",
                            color="#c6c6c6",
                            size=13,
                            text_align="center", 
                            height=30
                        )
                    ),
                    # Other tabs
                    *list(
                        ft.Text(
                            value=i,
                            color="#c6c6c6",
                            size=13,
                            expand=7,
                            text_align="center",
                            height=30
                        ) for i in [
                            "CORN VIDEOS",
                            "CATEGORIES",
                            "LIVE CAMS",
                            "CORNSTART",
                            "COMMUNITY",
                            "PHOTOS & GIFTS"
                        ]
                    )
                ]
            )
        )