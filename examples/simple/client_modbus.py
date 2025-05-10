import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as cst

# Connect to the server
master = modbus_tcp.TcpMaster(host="localhost", port=502)
master.set_timeout(2.0)

# Read holding registers from slave ID 1, address 0, count 3
values = master.execute(1, cst.READ_HOLDING_REGISTERS, 0, 3)
print("Read values:", values)

