from importlib import import_module


# Entry point for raw input
def process_command(raw_data, message):
    command = parse_command(raw_data)
    response = route_command(command, message)
    return response


# Currently it offers a very simple solution to split the string by ' ' (space character)
def parse_command(string):
    return string.split(" ")


# Route a command to a respective handler
def route_command(command, message):

    root_command = command[0].lower()

    allowed_commands = [
        "camera", "help", "lights", "event"
    ]

    if root_command in allowed_commands:
        return getattr(import_module(f"commands.{root_command}"), "proc")(command[1:], message)

    else:
        return getattr(import_module("commands.default"), "proc")(command[1:], message)
