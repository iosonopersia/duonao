# Choregraphe simplified export in Python.
from naoqi import ALProxy

def main(robotIP, port):

names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-1.42104, -0.569503, -1.38758, -0.569503, -1.38758, -0.569503, -1.38758, -1.38841])

names.append("LElbowYaw")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-1.03632, -1.28183, -1.29194, -1.28183, -1.29194, -1.28183, -1.29194, -1.30122])

names.append("LHand")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377])

names.append("LShoulderPitch")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-0.904459, -0.906371, -0.906371, -0.90637, -0.90637, -0.90637, -0.90637, 0.850113])

names.append("LShoulderRoll")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([0.433958, 0.235368, 0.256203, 0.235368, 0.256202, 0.235368, 0.256202, 0.263257])

names.append("LWristYaw")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-0.93993, -0.93993, -0.93993, -0.93993, -0.93993, -0.93993, -0.93993, -0.93993])

names.append("RElbowRoll")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([1.42106, 0.569719, 1.38757, 0.569719, 1.38757, 0.569719, 1.38757, 1.3884])

names.append("RElbowYaw")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([1.03621, 1.28193, 1.29194, 1.28193, 1.29194, 1.28193, 1.29194, 1.30119])

names.append("RHand")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377, 0.00291377])

names.append("RShoulderPitch")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-0.905158, -0.906574, -0.906574, -0.906575, -0.906575, -0.906575, -0.906575, 0.850119])

names.append("RShoulderRoll")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([-0.433675, -0.234958, -0.255925, -0.234958, -0.255925, -0.234958, -0.255925, -0.262971])

names.append("RWristYaw")
times.append([1, 1.8, 2.8, 3.6, 4.4, 5, 5.52, 6.2])
keys.append([0.93993, 0.93993, 0.93993, 0.93993, 0.93993, 0.93993, 0.93993, 0.93993])

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
