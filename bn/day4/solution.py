

def test_password(input):
    test_pass = False
    array_form = [int(d) for d in str(input)]
    for i in range(1, len(array_form)):
        if array_form[i] == array_form[i-1]:
            test_pass = True
        if array_form[i] < array_form[i-1]:
            return False
    return test_pass


valid_passwords = 0

for i in range(197487, 673251):
    if test_password(i):
        valid_passwords += 1

print(valid_passwords)
