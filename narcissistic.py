def narcissistic( value ):
    len = 0;
    base = 1;
    if (value ==1):
        return True;
    while (value > base):
        base = base * 10;
        len = len + 1;
    sum = 0;

    tmp_val = value
    for x in range(0, len):
        base = base / 10;
        sum += pow(tmp_val // base, len);
        tmp_val -= base * (tmp_val // base)
    print (sum);  
    return sum == value;
    