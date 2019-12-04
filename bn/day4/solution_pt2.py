def test_password(input):
    pair_found = False
    array_form = [int(d) for d in str(input)]
    if array_form[0] == array_form[1] and array_form[1] != array_form[2]:
        pair_found = True
    for i in range(3, len(array_form)):
        if array_form[i-2] == array_form[i-1] and array_form[i-1] != array_form[i] and array_form[i-3] != array_form[i-2]:
            pair_found = True
    for i in range(1, len(array_form)):
        if array_form[i] < array_form[i-1]:
            return False
    if array_form[len(array_form)-1] == array_form[len(array_form)-2] and array_form[len(array_form) - 1] != array_form[len(array_form)-3]:
        pair_found = True
    return pair_found


valid_passwords = 0

for i in range(197487, 673251):
    if test_password(i):
        valid_passwords += 1

print(valid_passwords)
