import sys
import time
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	try:
		ttsProxy = ALProxy("ALTextToSpeech",robotIP,port)
	except Exception,e:
		print("Could not create a proxy to ALTextToSpeech")

	ttsProxy.say("Follow the rhythm with me!!")

	names.append("HeadPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.356047, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.270526, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.356047, [3, -0.111111, 0], [3, 0.111111, 0]], [0.270526, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.356047, [3, -0.111111, 0], [3, 0.111111, 0]], [0.270526, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.356047, [3, -0.111111, 0], [3, 0.111111, 0]], [0.270526, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0, [3, -0.0555556, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0.111111, 0]], [0, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.348738, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.348738, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.00852969, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00852969, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-1.00126, [3, -0.0555556, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.00126, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-1.39872, [3, -0.0555556, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [-1.39872, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.25, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.448337, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.000286866, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0.111111, 0]], [0.000286866, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.000487671, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.697734, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0.111111, 0]], [0.697734, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[1.39727, [3, -0.0555556, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.301284, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [0.301284, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.00728834, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.00728834, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.5044, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.354476, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.5044, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.354476, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.5044, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.354476, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.5044, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.354476, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.355665, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.00589853, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00589853, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[1.00126, [3, -0.0555556, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0.111111, 0]], [1.00126, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[1.39872, [3, -0.0555556, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39872, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.25, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0.111111, 0]], [0.25, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.448337, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.448337, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.0715585, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.0628318, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0715585, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0628318, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0715585, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0628318, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0715585, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.0628318, [3, -0.111111, -0.00872665], [3, 0.111111, 0.00872665]], [0, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.000487671, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.000487671, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.699999, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0.111111, 0]], [0.699999, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[1.39727, [3, -0.0555556, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0.111111, 0]], [1.39727, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[-0.301284, [3, -0.0555556, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0.111111, 0]], [-0.301284, [3, -0.111111, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([0.166667, 0.5, 0.833333, 1.16667, 1.5, 1.83333, 2.16667, 2.5, 2.83333])
	keys.append([[0.00728834, [3, -0.0555556, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0.111111, 0]], [0.00728834, [3, -0.111111, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion",robotIP,port)
	  motion.angleInterpolationBezier(names, times, keys)
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
