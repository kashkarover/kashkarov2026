def is_access_allowed(ip_addres, mode, ip_access_lists):
    if mode == 1 and ip_addres not in ip_access_lists['black list']:
        return 'ДА'
    elif mode == 2 and ip_addres in ip_access_lists['white list']:
        return 'ДА'
    else:
        return 'НЕТ'