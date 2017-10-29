import commands


# Entry point for raw input
def process_command(raw_data):
    command = parse_command(raw_data)
    response = route_command(command)
    return response


# Currently it offers a very simple solution to split the string by ' ' (space character)
def parse_command(string):
    return string.split(" ")


# Route a command to a respective handler
def route_command(command):

    root_command = command[0].lower()

    if root_command == "camera":
        return commands.camera.proc(command)

    elif root_command == "help":
        return commands.help.proc(command)

    elif root_command == "lights":
        return commands.lights.proc(command)

    elif root_command == "subscribe":
        return commands.subscribe.proc(command)

    else:
        return commands.default.proc(command)
