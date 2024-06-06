

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str = "") -> str:
    if friend_name == "":
        return "Hello, World!"

    return f"Hello, {friend_name}!"

