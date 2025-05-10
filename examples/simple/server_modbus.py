import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as cst
import time

# Create Modbus TCP server
server = modbus_tcp.TcpServer(address="localhost", port=502)
server.start()

# Add a slave with ID 1
slave = server.add_slave(1)

# Add a block of 10 holding registers (type 'hr'), starting at address 0
slave.add_block('hr_block', cst.HOLDING_REGISTERS, 0, 10)

# Set some initial values
slave.set_values('hr_block', 0, [100, 200, 300])

print("Modbus TCP server is running. Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down server.")
    server.stop()

