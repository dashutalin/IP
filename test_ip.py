import pytest
from IP import ip2bin4
from IP import ip2bin6


@pytest.mark.parametrize("number, result", [
    ('192.168.1.2', '11000000101010000000000100000010'),
    ('192.0.0.0', '11000000000000000000000000000000'),
    ('0.0.0.0', '00000000000000000000000000000000')
])
def test_ip2bin4_good(number, result):
    ip2bin4(number) == result


@pytest.mark.parametrize("number, exception", [
    (19216812, AttributeError),
    ('0', IndexError),
    ('19216811', IndexError),
    ('192.168', IndexError),
    ('', ValueError),
    ('abcd', ValueError),
    ('0.0', IndexError)
])
def test_with_error(number, exception):
    with pytest.raises(exception):
        ip2bin4(number)


@pytest.mark.parametrize("number_of_ip, bin_number", [
    ('ffe0_0000_0000_0000_0001_0000_0000_0000', '11111111111000000000000000000000000000000000000000000000000000000000000000000001000000000000000000000000000000000000000000000000'),
    ('f000_0000_0000_0000_0000_0000_0000_0000', '11110000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'),
    ('0000_0000_0000_0000_0000_0000_0000_0000', '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
])
def test_ip2bin6_good(number_of_ip, bin_number):
    ip2bin6(number_of_ip) == bin_number


@pytest.mark.parametrize("ip, errors", [
    ('ffe0::2:0:0:0', ValueError),
    ('f0000000000000000000000000000000', IndexError),
    ('', ValueError),
    (98762341, AttributeError),
    ('abcd', IndexError)
])
def test_with_errors_2(ip, errors):
    with pytest.raises(errors):
        ip2bin6(ip)
