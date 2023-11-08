from djitellopy import Tello

tello = Tello()

tello.connect()

print(tello.get_battery())

tello.takeoff()

tello.go_xyz_speed(0,100,0,20)



tello.land()