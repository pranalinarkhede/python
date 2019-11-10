def count_substring(string, sub_string):
    return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)])

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
