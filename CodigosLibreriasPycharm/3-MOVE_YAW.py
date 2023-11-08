from djitellopy import Tello
tello = Tello()
tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.move_back(100)
tello.move_left(100)
tello.move_right(100)
tello.move_back(100)
tello.move_forward(100)
tello.move_up(100)
tello.move_down(100)
tello.rotate_clockwise(180)
tello.rotate_counter_clockwise(180)

tello.land()