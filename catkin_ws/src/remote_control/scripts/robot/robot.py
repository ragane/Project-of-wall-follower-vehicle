import time
import sys

class RobotBot(object):
	
	def __init__(self,in1=7,in2=11,in3=13,in4=15,ena=16,enb=18):
		self.IN1 = in1
		self.IN2 = in2
		self.IN3 = in3
		self.IN4 = in4
		self.ENA = ena
		self.ENB = enb
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		GPIO.setup(self.IN1,GPIO.OUT)
		GPIO.setup(self.IN2,GPIO.OUT)
		GPIO.setup(self.IN3,GPIO.OUT)
		GPIO.setup(self.IN4,GPIO.OUT)
		GPIO.setup(self.ENA, GPIO.OUT)
		GPIO.setup(self.ENB, GPIO.OUT)
		self.forward()
		self.PWMA = GPIO.PWM(self.ENA, 100)
		self.PWMB = GPIO.PWM(self.ENB, 100)
		self.PWMA.start(0)
		self.PWMB.start(0)

	def forward(self):
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)

	def stop(self):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.LOW)

	def backward(self):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)

	def left(self):
		GPIO.output(self.IN1,GPIO.LOW)
		GPIO.output(self.IN2,GPIO.HIGH)
		GPIO.output(self.IN3,GPIO.HIGH)
		GPIO.output(self.IN4,GPIO.LOW)
		
	def right(self):
		GPIO.output(self.IN1,GPIO.HIGH)
		GPIO.output(self.IN2,GPIO.LOW)
		GPIO.output(self.IN3,GPIO.LOW)
		GPIO.output(self.IN4,GPIO.HIGH)
	
	def setPWMA(self, value):
		self.PWMA.ChangeDutyCycle(value)
		
	def setPWMB(self, value):
		self.PWM.ChangeDutyCycle(value)

	def setMotor(self, left, right):
		if ((left == 0) and ( right == 0)):
			GPIO.output(self.IN1, GPIO.LOW)
			GPIO.output(self.IN2, GPIO.LOW)
			GPIO.output(self.IN3, GPIO.LOW)
			GPIO.output(self.IN4, GPIO.LOW)
			self.PWMA.ChangeDutyCycle(0)
			self.PWMB.ChangeDutyCycle(0)
		else:
			if((left > 0) and (left <= 100)):
				GPIO.output(self.IN1,GPIO.HIGH)
				GPIO.output(self.IN2,GPIO.LOW)
				self.PWMA.ChangeDutyCycle(left)

			elif((left < 0) and (left >= -100)):
				GPIO.output(self.IN1,GPIO.LOW)
				GPIO.output(self.IN2,GPIO.HIGH)
				self.PWMA.ChangeDutyCycle(0 - left)
			
			if((right > 0) and (right < 100)):
				GPIO.output(self.IN3,GPIO.LOW)
				GPIO.output(self.IN4,GPIO.HIGH)
				self.PWMB.ChangeDutyCycle(right)

			elif((right < 0) and (right >= -100)):
				GPIO.output(self.IN3,GPIO.HIGH)
				GPIO.output(self.IN4,GPIO.LOW)
				self.PWMB.ChangeDutyCycle(0 - right)
