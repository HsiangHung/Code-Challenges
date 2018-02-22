Q5.2 binarize float number
#
def float_binarize(x):
    bit, decimal = 1, float(1/2)
    bits = ''
    while bit <= 6:
        if x > decimal:
            x -= decimal
            bits += '1'
        else:
            bits += '0'
            
        bit += 1
        decimal = decimal/2
            
    return '0.'+bits

print (float_binarize(0.33))