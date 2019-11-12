
class Path:
	def __init__(self):
		self.path = []

	def __add__(self, path: "Path", direction:tuple) -> 'Position':
		if direction == (1, 0):
			return path.append("r")
		if direction == (-1, 0):
			return path.append("l")
		if direction == (0, -1):
			return path.append("u")
		if direction == (0, 1):
			return path.append("d")