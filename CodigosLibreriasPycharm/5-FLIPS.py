from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())

tello.takeoff()

tello.flip_forward()
tello.flip_back()
tello.flip_left()
tello.flip_right()


tello.land()