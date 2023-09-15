import platform


def UserOS():
    return platform.system()


print(f"The user is running {UserOS()}.")
