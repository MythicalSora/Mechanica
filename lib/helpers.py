import json
import discord

def __read_file(config):
    with open(config, 'r') as file:
        return json.loads(file.read())


def get_config(config):
    return __read_file(config)


def permission_error(permission):
    description = ""

    if isinstance(permission, list):
        description = "Missing several permissions."
    else:
        description =  f"Missing `{permission}`."

    return discord.Embed(
        title="Action not allowed!",
        description=description,
        color=discord.Colour.red()
    )


def error_handler(error):
    print(f"Error->{type(error).__name__}:\n{error}")
    return discord.Embed(
        title="An error occured!",
        description=f"```{type(error).__name__}:\n{str(error)}```",
        color=discord.Colour.red()
    )


def notif_handler(notif):
    return discord.Embed(
        title=notif,
        color=discord.Colour.gold()
    )


def is_developer(user: discord.User):
    developers = get_config('/home/michael/programming/discord/mechanica/config.json')
    developers = developers["developers"]

    result = False

    for dev in developers:
        if int(dev['id']) == user.id:
            result = True
    
    return result


def no_developer():
    return discord.Embed(
        title="No permission!",
        description="Only developers are allowed to use this function.",
        color=discord.Colour.red()
    )