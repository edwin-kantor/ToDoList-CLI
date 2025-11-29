import os

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To-Do List CLI - Utility Functions

Helper functions for To-Do List application logic.
"""


def display_menu():
    """
    Display the main menu with options
    """
    print("=== To-Do List CLI ===")
    print("\nMenu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def clear_screen():
    """
    Clear the terminal screen
    """
    os.system("cls" if os.name == "nt" else "clear")


def normalize_input(user_input):
    """
    Normalize user input by removing whitespace
    """
    return user_input.strip()


def confirm_exit():
    """
    Ask user for exit confirmation
    """
    choice = input("Are you sure you want to exit? [y/n]: ")
    choice = normalize_input(choice).lower()

    return choice in ["y", "yes"]

