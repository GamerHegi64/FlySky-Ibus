import serial
import struct
import time

class iBus:
  
  IBUS_START = b'\x20'
  IBUS_FORMAT = '<BBHHHHHHHHHHHHHHh'
  IBUS_FORMAT_CALC_CHECKSUM = '<BBHHHHHHHHHHHHHH'
  
  def __init__(self, serialPort: str, baudrate: int=115200) -> None:
    self.port = serialPort
    self.baudrate = baudrate
    self.connect()
  
  def connect(self) -> None:
    self.serial = serial.Serial(self.port, self.baudrate)
    
  def read(self) -> list:
    data = self.serial.read(32)
    
    while self.validate(data) == False:
      data = self.serial.read(1)
      
      while data != self.IBUS_START:
        data = self.serial.read(1)
        
      data += self.serial.read(31)
  
    if self.validate(data):
      return self.unpack(data)
    else:
      return 'error'
  
  def validate(self, data: list) -> bool:
    data = self.unpack(data)
    print(self.calc_checksum(data[:-1]))
    return data[0] == 32 and data[1] == 64 and data[-1] == self.calc_checksum(data[:-1])
  
  def write(self, data: list) -> None:
    if len(data) != 30:
      raise ValueError('Data length must be 30')
    data.append(self.calc_checksum(data))
    self.serial.write(struct.pack(self.IBUS_FORMAT, data))
  
  def unpack(self, data: list) -> list:
    if len(data) != 32:
      raise ValueError('Data length must be 32')
    return struct.unpack(self.IBUS_FORMAT, data)
  
  def calc_checksum(self, data: list) -> int:
    return ((sum(bytearray(struct.pack(self.IBUS_FORMAT_CALC_CHECKSUM, *data))))*-1)-1
      
  def __str__(self) -> str:
    return f'Connected to {self.port} with {self.baudrate} baudrate'
    
    
if __name__ == '__main__':
  ibus = iBus('/dev/ttyS0')
  print(ibus)
  
  while True:
    print(ibus.read())
    print('####################')