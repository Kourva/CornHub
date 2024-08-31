#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard imports
from typing import Self, NoReturn, Dict

# 3rd-Party imports
import flet as ft

class Video:
    """Video container"""
    def __init__(self: Self, video: Dict[str, str]) -> NoReturn:
        """
        Initial method of class
        
        :params: video: Video data
        :return: None
        """
        self.video: Dict[str, str] = video

    def build(self: Self) -> ft.Container:
        """
        Method to return video's container

        :params: Self
        :return: ft.Container
        """
        # Main container
        return ft.Container(
            ink=True,
            on_click=lambda _: None,
            expand=4,
            content=ft.Column(
                spacing=0,
                controls=[
                    # Thumbnail container
                    ft.Stack(
                        controls=[
                            # Thumbnail
                            ft.Image(
                                src=self.video["image"]
                            ),
                            # Duration
                            ft.Text(
                                value="12:63", 
                                bottom=5, 
                                right=5, 
                                color="#c6c6c6",
                                bgcolor="#99000000", 
                                size=14
                            )
                        ]
                    ),
                    # Video details
                    ft.Row(
                        height=40,
                        spacing=0,
                        controls=[
                            # PornStar name
                            ft.Text(
                                value=self.video["pornstar"], 
                                color="#ffffff"
                            ),
                            # Verified badge
                            ft.Image(
                                src="https://raw.githubusercontent.com/GetRealTiktokFollowers/InstagramVerifiedBadges.github.io/main/badge.png",
                                width=16,
                                height=16,
                            ),
                            # Expanded divider
                            ft.Text(
                                value="", 
                                expand=True
                            ),
                            # Views 
                            ft.Row(
                                spacing=2, 
                                controls=[
                                    ft.Icon(
                                        name="visibility", 
                                        size=15, 
                                        color="#888888"
                                    ),
                                    ft.Text(
                                        value=self.video["views"],
                                        color="#888888",
                                        size=12
                                    )
                                ]
                            ),
                            # Little empty space
                            ft.Text(
                                value="", 
                                width=15
                            ),
                            # Rating
                            ft.Row(
                                spacing=2, 
                                controls=[
                                    ft.Icon(
                                        name="thumb_up",
                                        size=15,
                                        color="#888888"
                                    ),
                                    ft.Text(
                                        value=self.video["rating"],
                                        color="#888888",
                                        size=12
                                    )
                                ]
                            )
                        ]
                    ),
                    # Video title and actions
                    ft.Row(
                        spacing=4,
                        controls=[
                            # Video title
                            ft.Text(
                                value=self.video["title"],
                                color="#ffffff",
                                expand=4,
                                max_lines=2,
                                overflow="ellipsis"
                            ),
                            # Action menu
                            ft.IconButton(
                                icon="more_vert", 
                                icon_size=22, 
                                icon_color="#ffffff"
                            )
                        ]
                    ),
                    # Little empty space
                    ft.Text(
                        value="",
                        height=10
                    )
                ]
            )
        )