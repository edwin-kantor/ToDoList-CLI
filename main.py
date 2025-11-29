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

def add_task(tasks, task_name):
    """
    Add a new task to the list
    
    Args:
        tasks: List of tasks
        task_name: Name of the task to add
    """
    # TODO 🇺🇸: Add task_name to tasks list using append(),
    #          and display success message
    tasks.append(task_name)
    print(f"Task '{task_name}' added successfully!")


def view_tasks(tasks):
    """
    Display all tasks with numbers
    
    Args:
        tasks: List of tasks
    """
    # TODO 🇺🇸: Use enumerate() to display numbered tasks,
    #          handle empty list case, and wait for user
    #          to press Enter
#Handle empty list

    if not tasks:
        print("No tasks added!")
        input("Press Enter to continue...")
        return

    #Display a number of tasks
    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

    input("\nPress Enter to continue...")


def delete_task_by_index(tasks, index):
    """
    Delete a task by its index
    
    Args:
        tasks: List of tasks
        index: Index of the task to delete (1-based)
    
    Returns:
        True if task was deleted, False if index is invalid
    """
    # TODO 🇺🇸: Use try/except to handle invalid index,
    #          check if index is valid (1 <= index <= len(tasks)),
    #          remove task from list, display success message,
    #          and return True. Return False if index is invalid
    try:
        # Convert 1-based index into 0-based
        real_index = index - 1

        # Check if index is valid
        if 1 <= index <= len(tasks):
            removed_task = tasks.pop(real_index)
            print(f"Task '{removed_task}' has been deleted successfully.")
            return True
        else:
            print("Invalid task number.")
            return False

    except Exception:
        # Catch unexpected issues (e.g., non-integer input)
        print("Error: Unable to delete task. Invalid index.")
        return False

def delete_task_by_name(tasks, task_name):
    """
    Delete a task by its name
    
    Args:
        tasks: List of tasks
        task_name: Name of the task to delete
    
    Returns:
        True if task was deleted, False if task not found
    """
    # TODO 🇺🇸: Check if task_name exists in tasks list,
    #          remove it if found, display success message,
    #          and return True. Return False if task not found
    # Normalize the input (optional but good practice)

    task_name = task_name.strip()

    if task_name in tasks:
        tasks.remove(task_name)
        print(f"Task '{task_name}' has been deleted successfully.")
        return True
    else:
        print(f"Error: Task '{task_name}' not found.")
        return False

def main():
    """
    Main program loop
    """
    # TODO 🇺🇸: Initialize empty tasks list, create infinite
    #          loop, clear screen, display menu, get user choice,
    #          handle each option (add, view, delete by index/name,
    #          exit with confirmation), and keep loop active
    #          until user chooses exit

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
                print("There are no tasks to delete.")
                input("Press Enter to continue...")
                continue

            print("\nChoose deletion method:")
            print("1. Delete by index")
            print("2. Delete by task name")

            delete_choice = normalize_input(input("Enter option: "))

            if delete_choice == "1":
                try:
                    index = int(input("Enter task number: "))
                    delete_task_by_index(tasks, index)
                except ValueError:
                    print("Invalid number format.")

            elif delete_choice == "2":
                name = normalize_input(input("Enter task name: "))
                delete_task_by_name(tasks, name)

            else:
                print("Invalid delete option.")

            input("Press Enter to continue...")

        # OPTION 4 — EXIT
        elif choice == "4":
            if confirm_exit():
                print("Exiting program...")
                break
            else:
                print("Exit cancelled.")
                input("Press Enter to continue...")

        # INVALID OPTION
        else:
            print("Invalid choice. Please choose 1–4.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
