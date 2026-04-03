def add_binary(a, b):
    if a.startswith('0b'):
        a = a[2:]
    if b.startswith('0b'):
        b = b[2:]
    
    maxlen = len(a)
    if len(b) > maxlen:
        maxlen = len(b)
        
    a = ('0' * (maxlen - len(a))) + a
    b = ('0' * (maxlen - len(b))) + b
    
    result = ""
    carry = 0
    
    for i in range(maxlen - 1, -1, -1):
        bit_sum = int(a[i]) + int(b[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
        
    if carry:
        result = '1' + result
        
    idx = 0
    while idx < len(result) and result[idx] == '0':
        idx += 1
        
    res_str = result[idx:]
    if res_str == "":
        res_str = "0"
        
    return '0b' + res_str