import commands


# Currently it offers a very simple solution to split the string by ' ' (space character)
def parse_command(string):
    return string.split(" ")


#
def route_command(command):

    root_command = command[0]

    if root_command == "camera":
        commands.camera.proc(command)

    elif root_command == "help":
        commands.help.proc(command)

    elif root_command == "lights":
        commands.lights.proc(command)

    elif root_command == "subscribe":
        commands.subscribe.proc(command)

    else:
        commands.default.proc(command)
