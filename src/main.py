import math

from . import compute, ui

if __name__ == '__main__':
    # Getting inputs
    QUIT_PHRASE = 'q'
    print(f'At any time, enter {QUIT_PHRASE} to quit')
    base = ui.get_int(
        lambda n: n > 1,
        msg='Enter the base (i.e, if the circuit should comprise of 1-to-X splitters, enter X): ',
        err_msg='Base must be greater than 1',
        exit_phrase=QUIT_PHRASE)
    if base is None:
        exit()
    num = ui.get_int(
        lambda n: n > 0,
        msg='Enter the output numerator: ',
        err_msg='Numerator must be a positive integer',
        exit_phrase=QUIT_PHRASE)
    if num is None:
        exit()
    condition = lambda d: d > num
    denom = ui.get_int(
        condition,
        msg='Enter the output denominator: ',
        err_msg=f'Denominator must be an integer greater than the numerator {num}',
        exit_phrase=QUIT_PHRASE)
    if denom is None:
        exit()
    # Reducing inputs
    g = math.gcd(num, denom)
    num //= g
    denom //= g
    # Outputting calculations
    b = math.ceil(math.log(denom, base))
    new_denom = base ** b
    if new_denom == denom:
        print(f'Primary output ({num}/{denom}): {num}\xb7{base}{compute.as_exponent(-b)}')
        print(f'Secondary output ({denom - num}/{denom}): Everything else')
    else:
        # Subtracting from exponents to account for fraction
        pri_as_base = {(p - b, s) for p, s in compute.as_base(base, num).items()}
        sec_as_base = {(p - b, s) for p, s in compute.as_base(base, denom - num).items()}
        new_as_base = {(p - b, s) for p, s in compute.as_base(base, new_denom - denom).items()}
        print(f'Primary output ({num}/{denom}): {ui.expand_as_base(base, pri_as_base)}')
        print(f'Secondary output ({denom - num}/{denom}): {ui.expand_as_base(base, sec_as_base)}')
        print(f'Loopback (everything else): {ui.expand_as_base(base, new_as_base)}')
