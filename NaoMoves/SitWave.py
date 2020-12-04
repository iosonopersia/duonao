# Choregraphe simplified export in Python.
from naoqi import ALProxy

def main(robotIP, port):


names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.0440856, -0.039926, -0.0440856, -0.0440856, -0.0440856, -0.0440856])

names.append("HeadYaw")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.0270945, -0.030722, -0.0270945, -0.0270945, -0.0270945, -0.0270945])

names.append("LAnklePitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.828103, 0.828103, 0.828103, 0.828103, 0.828103, 0.828103])

names.append("LAnkleRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.0148023, -0.0109967, -0.0148023, -0.0148023, -0.0148023, -0.0148023])

names.append("LElbowRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.035488, -0.0358391, -0.0358344, -0.0358344, -0.0358344, -0.0358344])

names.append("LElbowYaw")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.0678327, -0.0591351, -0.056607, -0.056607, -0.056607, -0.056607])

names.append("LHand")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([1, 1, 1, 1, 1, 1])

names.append("LHipPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-1.53098, -1.53098, -1.53098, -1.53098, -1.53098, -1.53098])

names.append("LHipRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.266548, 0.27205, 0.266548, 0.266548, 0.266548, 0.266548])

names.append("LHipYawPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.618735, -0.618735, -0.618735, -0.618735, -0.618735, -0.618735])

names.append("LKneePitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([1.3959, 1.3959, 1.3959, 1.3959, 1.3959, 1.3959])

names.append("LShoulderPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.184141, -1.14456, -1.11341, -1.13785, -1.11341, -1.13784])

names.append("LShoulderRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.0219738, 0.0191574, -0.247717, 0.573778, -0.247716, 0.573777])

names.append("LWristYaw")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.496526, -0.499864, -0.496526, -0.496526, -0.496525, -0.496525])

names.append("RAnklePitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.849878, 0.849878, 0.849878, 0.849878, 0.849878, 0.849878])

names.append("RAnkleRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.025733, 0.025733, 0.025733, 0.025733, 0.025733, 0.025733])

names.append("RElbowRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.0355055, 0.0358391, 0.0355055, 0.0355055, 0.0355054, 0.0355054])

names.append("RElbowYaw")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.0567426, 0.0590731, 0.0567426, 0.0567426, 0.0567426, 0.0567426])

names.append("RHand")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([1, 1, 1, 1, 1, 1])

names.append("RHipPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-1.53589, -1.53589, -1.53589, -1.53589, -1.53589, -1.53589])

names.append("RHipRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.25773, -0.262941, -0.25773, -0.25773, -0.257731, -0.257731])

names.append("RHipYawPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.618735, -0.618735, -0.618735, -0.618735, -0.618735, -0.618735])

names.append("RKneePitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([1.40519, 1.40519, 1.40519, 1.40519, 1.40519, 1.40519])

names.append("RShoulderPitch")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.184141, -1.14463, -1.14406, -1.10987, -1.14407, -1.10987])

names.append("RShoulderRoll")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([-0.0209017, -0.0186347, -0.582006, 0.252012, -0.582006, 0.252012])

names.append("RWristYaw")
times.append([0.04, 1.2, 2.4, 3.6, 4.8, 6])
keys.append([0.498887, 0.499864, 0.498887, 0.498887, 0.498887, 0.498887])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
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

