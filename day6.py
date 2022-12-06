from getdata import getdata

content = getdata.getdata('day6')

def has_repeated_chars(window: str):
    for char in window:
        if window.count(char) > 1:
            return True

    return False
def stars(data, window_size):
    char_num = window_size
    window = data[char_num-window_size:char_num]
    repeated = has_repeated_chars(window)
    while char_num < len(data) and repeated:
        char_num += 1
        window = data[char_num-window_size:char_num]
        repeated = has_repeated_chars(window)
    return char_num

print(stars(content, 14))