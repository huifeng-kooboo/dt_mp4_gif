import ipaddress


def is_valid_address(ip_address_str):
    """
    判断是否是个有效的Ip地址
    """
    try:
        ipaddress.ip_address(ip_address_str)
    except ValueError:
        return False
    return True
