#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
To-Do List CLI - Main Program

A command-line To-Do List application for managing daily tasks.
"""
from turtledemo.clock import display_date_time

# TODO 🇺🇸: Import utility functions from utils.py

from utils import (
    display_menu,
    clear_screen,
    normalize_input,
    confirm_exit
)

SUCCESS_PREFIX = "SUCCESS:"
ERROR_PREFIX = "Error:"

def add_task(tasks, task_name):

    tasks.append(task_name)
    print(f"Task '{task_name}' added successfully!")


def view_tasks(tasks):
#Handle empty list

    if not tasks:
        print(f"{ERROR_PREFIX}No tasks available.")
        input("Press Enter to continue...")
        return

    #Display a number of tasks
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    input("\nPress Enter to continue...")


def delete_task_by_index(tasks, index):
    try:
        # Convert 1-based index into 0-based
        real_index = index - 1

        # Check if index is valid
        removed_task = tasks.pop(real_index)
        print(f"{SUCCESS_PREFIX} Task '{removed_task}' deleted.")
        return True

    except IndexError:
        print(f"{ERROR_PREFIX} Invalid task number.")
        return False

def delete_task_by_name(tasks, task_name):

    # Normalize the input (optional but good practice)

    task_name = task_name.strip()

    if task_name in tasks:
        tasks.remove(task_name)
        print(f"{SUCCESS_PREFIX} Task '{task_name}' deleted.")
        return True
    else:
        print(f"{ERROR_PREFIX} Task '{task_name}' not found.")
        return False

def handle_task_deletion(tasks):
    print("\nChoose deletion method:")
    print("1. Delete by index")
    print("2. Delete by task name")

    delete_choice = normalize_input(input("Enter option: "))

    if delete_choice == "1":
        try:
            index = int(input("Enter task number: "))
            delete_task_by_index(tasks, index)
        except ValueError:
            print(f"{ERROR_PREFIX} Task number must be an integer.")

    elif delete_choice == "2":
        name = normalize_input(input("Enter task name: "))
        delete_task_by_name(tasks, name)

    else:
        print(f"{ERROR_PREFIX} Invalid delete option.")

def main():
#Main program loop

    tasks = ["Shower", "Eat", "Work", "Learn coding", "WorkOut", "Sleep"]

    while True:
        clear_screen()
        display_menu()

        choice = normalize_input(input("Enter your choice: "))

        # OPTION 1 — ADD TASK
        if choice == "1":
            new_task = normalize_input(input("Enter task name: "))
            add_task(tasks, new_task)
            input("\nPress Enter to continue...")

        # OPTION 2 — VIEW TASKS
        elif choice == "2":
            view_tasks(tasks)

        # OPTION 3 — DELETE TASK
        elif choice == "3":
            if not tasks:
                print(f"{ERROR_PREFIX} There are no tasks to delete.")
                input("Press Enter to continue...")
                continue

            handle_task_deletion(tasks)
            input("\nPress Enter to continue...")

        # OPTION 4 - EXIT
        elif choice == "4":
            if confirm_exit():
                print("Exit cancelled.")
                input("Press Enter to continue...")

        # INVALID OPTION
        else:
            print(f"{ERROR_PREFIX} Invalid choice. Please choose 1-4")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
