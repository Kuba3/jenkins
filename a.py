import mraa
import time
import unittest

gpio1=mraa.Gpio(7)
gpio1.dir(mraa.DIR_IN)

x= mraa.Pwm(3)
x.period_us(700)
x.enable(True)

value = 0.0
x.write(0.0)
time.sleep(0.5)
class TestStringMethods(unittest.TestCase):
	def test_on(self):
		x.write(0.0)
		time.sleep(2)
		test1 = gpio1.read()
		self.assertEqual(1,test1)

	def test_off(self):
		x.write(1)
		time.sleep(2)
		test2 = gpio1.read()
		self.assertEqual(0,test2)

	def test_ext_h(self):
		x.write(0.12)
		time.sleep(2)
		test3 = gpio1.read()
		self.assertEqual(0, test3)
	
	def test_ext_l(self):
		x.write(0.09)
		time.sleep(2)
		test4 = gpio1.read()
		self.assertEqual(1, test4)

if __name__ == '__main__':
	unittest.main()
	
