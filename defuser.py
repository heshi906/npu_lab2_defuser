<<<<<<< HEAD
count = 0  # 统计找到的次数

with open("bomb", "r+b") as file:
    file.seek(0x1200)  # 定位到 0x1200 的位置
    data = file.read(0x1600 - 0x1200)  # 读取指定范围的字节数据

    # 将字节数据转换为十六进制字符串
    hex_data = ' '.join(format(byte, '02X') for byte in data)

    if "55 89 E5 83 EC 14" in hex_data:
        start_index = hex_data.index("55 89 E5 83 EC 14")
        end_index = start_index + len("55 89 E5 83 EC 14")

        # 输出找到的信息
        print(f"Found at address 0x{start_index + 0x1200:04X}")
        count += 1

        # 替换字符串
        hex_data = hex_data.replace("55 89 E5 83 EC 14", "55 89 E5 C3 C3 C3", 1)

        # 将修改后的十六进制字符串转换回字节数据
        new_data = bytes.fromhex(hex_data)

        file.seek(0x1200)  # 再次定位到 0x1200 的位置
        file.write(new_data)  # 写入修改后的字节数据

print(f"Total occurrences found: {count}")
=======
count = 0  # 统计找到的次数

with open("bomb", "r+b") as file:
    file.seek(0x1200)  # 定位到 0x1200 的位置
    data = file.read(0x1600 - 0x1200)  # 读取指定范围的字节数据

    # 将字节数据转换为十六进制字符串
    hex_data = ' '.join(format(byte, '02X') for byte in data)

    if "55 89 E5 83 EC 14" in hex_data:
        start_index = hex_data.index("55 89 E5 83 EC 14")
        end_index = start_index + len("55 89 E5 83 EC 14")

        # 输出找到的信息
        print(f"Found at address 0x{start_index + 0x1200:04X}")
        count += 1

        # 替换字符串
        hex_data = hex_data.replace("55 89 E5 83 EC 14", "55 89 E5 C3 C3 C3", 1)

        # 将修改后的十六进制字符串转换回字节数据
        new_data = bytes.fromhex(hex_data)

        file.seek(0x1200)  # 再次定位到 0x1200 的位置
        file.write(new_data)  # 写入修改后的字节数据

print(f"Total occurrences found: {count}")
>>>>>>> origin/main
