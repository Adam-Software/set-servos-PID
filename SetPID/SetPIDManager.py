from SyncWritePIDServos import SyncWritePIDServos

ServosID = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ServosPID = [15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]

HeadID = [1, 2]
HeadPID = [15, 15]
ArmID = [11, 9, 7, 5, 12, 10, 8, 6]
ArmPID = [15, 15, 15, 15, 15, 15, 15, 15]
PressID = [14, 15]
PressPID = [15, 15]
BodyID = [13, 0]
BodyPID = [15, 0]
LegID = [16, 17, 18, 19, 20, 21]
LegPID = [6, 6, 6, 6, 6, 6]

#Function run example
WritePID = SyncWritePIDServos.SyncWriteData(LegID, LegPID)
print(WritePID)
