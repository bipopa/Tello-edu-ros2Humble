from djitellopy import Tello
tello = Tello()
tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.move_back(100)
tello.move_left(100)
tello.move_forward(100)
tello.move_right(100)

tello.land()