import platform

def UserOS():
    return platform.system()

os = UserOS()

print(f'The user is running {os}.')
