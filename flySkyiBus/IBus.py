import serial
import struct

class IBus:
  
  IBUS_START = b'\x20'
  IBUS_START_BYTES = [0x20, 0x40]
  IBUS_FORMAT = '<BBHHHHHHHHHHHHHHh'
  IBUS_FORMAT_CALC_CHECKSUM = '<BBHHHHHHHHHHHHHH'
  
  def __init__(self, serialPort: str, baudrate: int=115200) -> None:
    self.port = serialPort
    self.baudrate = baudrate
    self.connect()
  
  """
  connect to serial port
  """
  def connect(self) -> None:
    self.serial = serial.Serial(self.port, self.baudrate)
    
  """
  read iBus package from serial port
  
  Returns:
    list: unpacked iBus package
  """
  def read(self) -> tuple:
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
  
  """
  check if iBus package is valid
  
  Args:
    data: list
      data 32 bytes of the iBus package
  Returns:
    bool: True if valid, False if not
  """
  def validate(self, data: list) -> bool:
    data = self.unpack(data)
    
    return data[0] == 32 and data[1] == 64 and data[-1] == self.calc_checksum(data[:-1])
  
  """
  write data to serial port
  
  Args:
    data: str
      list of 14 channels each channel should be between 1000 and 2000

  Returns:
      None: non
  """
  def write(self, data: list) -> None:
    if len(data) != 14:
      raise ValueError('Data length must be 14')
    
    data.insert(0, self.IBUS_START_BYTES[1])
    data.insert(0, self.IBUS_START_BYTES[0])
    
    data.append(self.calc_checksum(data))
    
    self.serial.write(struct.pack(self.IBUS_FORMAT, *data))
  
  """
  unpack data iBus package bytestream
  
  Args:
    data: list
      data 32 bytes of the iBus package
      
  Returns:
    list: unpacked data
  """
  def unpack(self, data: tuple) -> tuple:
    if len(data) != 32:
      raise ValueError('Data length must be 32')
    
    return struct.unpack(self.IBUS_FORMAT, data)
  
  """
  calculate ibus checksum for data 30 first bytes
  
  Args:
    data: list
      list of the first 30 bytes of the iBus package
      
  Returns:
    int: checksum
      checksum for the first 30 bytes of the iBus package
  """
  def calc_checksum(self, data: list) -> int:
    return ((sum(bytearray(struct.pack(self.IBUS_FORMAT_CALC_CHECKSUM, *data))))*-1)-1
      
  def __str__(self) -> str:
    return f'Connected to {self.port} with {self.baudrate} baudrate'