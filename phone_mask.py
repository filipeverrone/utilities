from functools import reduce


def is_phone_valid(mask: str, phone_length: int):
    mask_length = reduce(lambda acc, b: acc + 1 if b.isnumeric()
                         or b == '#' else acc, list(mask), 0)
    return mask_length == phone_length


def mask_string(mask: str, phone: str):
    if (not is_phone_valid(mask, len(phone))):
        return 'phone or mask is not valid'
    mask_list = list(mask)
    i = 0  # mask
    j = 0  # phone

    new_phone = mask_list

    while i < len(mask_list):
        if mask_list[i].isnumeric():
            i, j = i + 1, j + 1
        elif mask_list[i] != '#':
            i += 1
        else:
            new_phone[i] = phone[j]
            i, j = i + 1, j + 1

    return reduce(lambda a, b: a + b, new_phone, '')


# use example
masks = [
    '(93) #####-####',
    '93-##-####-###',
    '+24 (###) ###-###',
    '+672-1##-###',
    '+37 (##) ###-##-##'
]
phone = '93123456789'

for mask in masks:
    print(mask_string(mask, phone))
