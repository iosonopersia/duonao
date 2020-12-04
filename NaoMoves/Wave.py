# Choregraphe simplified export in Python.
from naoqi import ALProxy

def main(robotIP, port):


# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-0.0385808, -0.0385808, -0.0385808, -0.0385808, -0.0385808, -1.20686])

names.append("LElbowYaw")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-0.0580294, -0.0580294, -0.0580294, -0.0580294, -0.0580294, -0.449089])

names.append("LHand")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.999057, 0.999057, 0.999057, 0.999057, 0.999057, 0.292776])

names.append("LShoulderPitch")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-1.13408, -1.09507, -1.1302, -1.09592, -1.12881, 0.86999])

names.append("LShoulderRoll")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.0281088, -0.203226, 0.571384, -0.208213, 0.570629, 0.253433])

names.append("LWristYaw")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-0.497479, -0.497479, -0.497479, -0.497479, -0.497479, 0.0340756])

names.append("RElbowRoll")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.0385964, 0.0385964, 0.0385964, 0.0385964, 0.0385964, 1.25389])

names.append("RElbowYaw")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.0594192, 0.0594192, 0.0594192, 0.0594192, 0.0594192, 0.514299])

names.append("RHand")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.999057, 0.999057, 0.999057, 0.999057, 0.999057, 0.296343])

names.append("RShoulderPitch")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-1.13415, -1.13415, -1.09282, -1.14402, -1.09261, 0.930716])

names.append("RShoulderRoll")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([-0.0270566, -0.578711, 0.213113, -0.576467, 0.216522, -0.297706])

names.append("RWristYaw")
times.append([1.6, 3.2, 4.8, 6.4, 8, 9.4])
keys.append([0.499835, 0.499835, 0.499835, 0.499835, 0.499835, -0.0207238])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion", robotIP, port)
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err



if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 55650 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)

