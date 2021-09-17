# https://blog.teclado.com/python-pythons-ternary-operator/

username = input("Enter username: ")
users = ["James", "Loen", "Adam", "John", "Smith"]


ADMIN = "Admin"

if username == ADMIN:
    print("You Have All Permissions!")


if username != ADMIN:
    print("You are not superuser")


class SpeedStatus:
    UNKNOWN = "Unknown"
    SLOW = "Slow"
    NORMAL = "Normal"
    WARNING = "Warning, Please Slow down"
    DANGER = "Danger speed, Stopping the car"


SLOW_SPEED = range(1, 41)
NORMAL_SPEED = range(40, 101)
WARNING_SPEED = range(100, 161)
DANGER_SPEED = range(161, 201)

speed = 130

if speed in SLOW_SPEED:
    print(SpeedStatus.SLOW)

elif speed in NORMAL_SPEED:
    print(SpeedStatus.NORMAL)

elif speed in WARNING_SPEED:
    print(SpeedStatus.WARNING)

elif speed in DANGER_SPEED:
    print(SpeedStatus.DANGER)

else:
    print(SpeedStatus.UNKNOWN)


if username:
    print(f"Your Username is {username}")


if username in users:
    print(f"Your Username Is Found {username}")

else:
    print(f"Username {username} Not Found")


is_smoke = True

status = "Smoking" if is_smoke else "No Smoking"

print(status)