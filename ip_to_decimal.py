def ip_to_decimal(ip_address):
    segments = ip_address.split('.')
    decimal_ip = 0

    for segment in segments:
        decimal_ip = decimal_ip * 256 + int(segment)

    return decimal_ip

ip_address = ""  # Please enter your desired IP address here
decimal_ip = ip_to_decimal(ip_address)
print(decimal_ip)