import zlib


def crc32(value):
    crc_value = zlib.crc32(value)
    return crc_value


bin_list = []
counter = 1

for i in range(1, 100000):
    data = i.to_bytes(4, byteorder="big")
    new_crc_value = crc32(data)

    if new_crc_value in bin_list:
        print(f"A collision occurred at element {counter} for number {i} (CRC: {new_crc_value})")
        break

    bin_list.append(new_crc_value)
    counter += 1
print(bin_list)
