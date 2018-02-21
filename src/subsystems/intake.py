import wpilib

import networktables
from wpilib.command.subsystem import Subsystem
from commands import grabber


class Intake(Subsystem):

    def __init__(self):
        super().__init__('Intake')
        self.intake_motor_closeOpen = wpilib.VictorSP(8)
        self.intake_motor_rightWheel = wpilib.VictorSP(7)
        self.intake_motor_leftWheel = wpilib.VictorSP(9)
        self.limit_switch = wpilib.DigitalOutput(0)
        self.intake_table = networktables.NetworkTables.getTable('/Intake')

    def initDefaultCommand(self):
        self.setDefaultCommand(grabber.Grabber())

    def closeGrabber(self, x):
        self.motor_closeOpen_set(x)

    def openGrabber(self):
        '''
        if self.limit_switch == True:
            self.grabberOff()
        else:'''
        self.motor_closeOpen_set(-0.5)

    def open2Grabber(self):
        self.intake_motor_closeOpen.set(-0.1)
        self.cubeOut()



    def grabberOff(self):
        self.motor_closeOpen_set(0)

    def cubeOut(self):
        self.intake_motor_rightWheel.set(1)
        self.intake_motor_leftWheel.set(-1)

    def cubeIn(self):
        self.intake_motor_rightWheel.set(-1)
        self.intake_motor_leftWheel.set(1)

    def intakeWheelsOff(self):
        self.intake_motor_rightWheel.set(0)
        self.intake_motor_leftWheel.set(0)

    def motor_closeOpen_set(self, voltage_percent):
        self.intake_motor_closeOpen.set(voltage_percent)

    def motor_rightWheel_set(self, voltage_percent):
        self.intake_motor_rightWheel.set(voltage_percent)

    def motor_leftWheel_set(self, voltage_percent):
        self.intake_motor_leftWheel.set(voltage_percent)

    def periodic(self):
        self.intake_table.putBoolean("LimitSwitch", self.limit_switch.get())
