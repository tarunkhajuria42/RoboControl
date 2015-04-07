# Readme.txt
@Description
Sending controller state form two xbox 360 controllers over tcp/ip to Server connected to a microcontroller


client to server Xbox 360 contorller to transmit data over 
Positions in Message code
Controller 1 Controls
	Hat
		0: Hat Up Neutral
		1: Hat Down
		2: Hat Up
		255: Hat Neutral Left
		3: Hat Left
		4: Hat Right
	Axis 0: No output
	Axis 1: Up and Dowm( Pwm output required)
		Up: 58 to 155
		Down:157 to 254
	Trigger
	Axis 2: + Left  - Right
		5: Left
		6: Right
		7: Nothing
	Left axis
	Axis 4: Left and right
		8: Left
		9: Right
		10: Nothing
	Axis 3: up and down
		11: Up
		12: Down
		13 Nothing
	Buttons
	Numpy Button Numbers
	Button A:0
	Button B:1
	Button X:2
	Button Y:3
	Left Bumper:4
	Right Bumper:5
	On State
		X:14
		Y:15
		A:16
		B:17
		Left Bumber:18
		Right Bumber:19 
	Off State
		X:20
		Y:21
		A:22
		B:23
		Left Bumper:24
		Right Bumper:25
Second Controller
	Hat
		26: Hat Neutral
		27: Hat Down
		28: Hat Up
		156:Hat Neutral Left
		29: Hat Left
		30: Hat Down
	Axis 0: Left and Right
		31: Left
		32: Right
		33: Nothing
	Axis 1: Up and Dowm( Pwm output required)
		34: Up
		35: Down
		36: Nothing
	Trigger
	Axis 2: + Left  - Right
		37: Left
		38: Right
		39: Nothing
	Left axis
	Axis 4: Left and right
		40: Left
		41: Right
		42: Nothing
	Axis 3: up and down
		43: Up
		44: Down
		45 Nothing
	Buttons
	Numpy Button Numbers
	Button A:0
	Button B:1
	Button X:2
	Button Y:3
	Left Bumper:4
	Right Bumper:5
	On State
		X:46
		Y:47
		A:48
		B:49
		Left Bumber:50
		Right Bumber:51 
	Off State
		X:52
		Y:53
		A:54
		B:55
		Left Bumper:56
		Right Bumper:57