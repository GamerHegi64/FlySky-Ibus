# FlySky iBus Python Library for Raspberry Pi

## Description

This is a Python package named `flySkyiBus` to communicate with FlySky iBus protocol using a Raspberry Pi. It makes use of the `pyserial` package to communicate with the serial port.

## Installation


~~This package is distributed via PyPi, and can be installed via pip. To install it, you can run:~~

<!---
```bash
pip install flySkyiBus
```
--->

You can also install directly from the GitHub repository by running:

```bash
pip install git+https://github.com/GamerHegi64/FlySky-Ibus.git
```

## Dependencies

This library depends on `pyserial` version 3.4 or higher.

## Usage

Here is a simple example of how to use this library:

```python
from flySkyiBus import IBus

bus = IBus('/dev/serial0')  # use your serial port name here

data = bus.read()  # Read data from serial port
print(data)  # print the data read from the serial port

bus.write([1500]*14)  # Write data to the serial port, replace with your data
```

Please note that the write method expects a list of 14 channels each ranging between 1000 and 2000.

## To-Dos

- write tests
- upload to pip

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
