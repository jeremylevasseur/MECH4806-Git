from simple_pid import PID

kp = 10
ki = 0.005
kd = 7

pid_x = PID(kp, ki, kd, 0)
pid_y = PID(kp, ki, kd, 0)

print(pid_x(10))