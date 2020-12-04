# Choregraphe simplified export in Python.
from naoqi import ALProxy

def main(robotIP, port):
names = list()
times = list()
keys = list()

names.append("LElbowRoll")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-0.454363, -0.457746, -0.454211, -0.443547, -0.45369, -0.443548, -0.45369, -1.20817])

names.append("LElbowYaw")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-0.434748, -0.436193, -0.436193, -0.43359, -0.43359, -0.43359, -0.43359, -0.447153])

names.append("LHand")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.292421])

names.append("LShoulderPitch")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-0.885062, -0.877172, -0.867202, -0.857235, -0.857235, -0.857236, -0.857236, 0.873037])

names.append("LShoulderRoll")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([0.8957, -0.205949, 1.2767, 0.024598, 1.29769, 0.024598, 1.29769, 0.247769])

names.append("LWristYaw")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-1.82287, -1.81425, -1.81425, -1.81425, -1.81425, -1.81425, -1.81425, 0.0367021])

names.append("RElbowRoll")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([0.454363, 0.452526, 0.450451, 0.443249, 0.443249, 0.443249, 0.443249, 1.25321])

names.append("RElbowYaw")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([0.498749, 0.504517, 0.504517, 0.503989, 0.503989, 0.50399, 0.50399, 0.51337])

names.append("RHand")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.990117, 0.296697])

names.append("RShoulderPitch")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-0.885062, -0.876903, -0.867316, -0.856968, -0.867144, -0.856969, -0.867144, 0.93291])

names.append("RShoulderRoll")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([-0.8957, 0.205949, -1.2767, -0.0240161, -1.29769, -0.0240161, -1.29769, -0.28838])

names.append("RWristYaw")
times.append([0.96, 2.12, 3.6, 4.88, 6.08, 7.52, 8.96, 10.28])
keys.append([1.82287, 1.81429, 1.81429, 1.81429, 1.81429, 1.81429, 1.81429, -0.0280378])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion",robotIP, port)
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err

if __name__ == "__main__":
	robotIP = "127.0.0.1"
	port = 9559

	if len(sys.argv) <= 1:
		print "(robotIP default: 127.0.0.1)"
	elif len(sys.argv) <= 2:
		robotIP = sys.argv[1]
	else:
		port = int(sys.argv[2])
		robotIP = sys.argv[1]

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))

