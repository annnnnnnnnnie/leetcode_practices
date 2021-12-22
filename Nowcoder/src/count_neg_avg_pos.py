def main():
    negative_count = 0
    non_negative_count = 0
    current_avg = 0
    while True:
        try:
            input_string = input()
            val = int(input_string)
            if val < 0:
                negative_count += 1
            else:
                if non_negative_count == 0:
                    current_avg = val
                else:
                    current_avg = ((current_avg / (non_negative_count + 1)) * non_negative_count
                                   + val / (non_negative_count + 1))
                non_negative_count += 1
        except Exception as e:
            break

    print(negative_count)
    print("{:.1f}".format(current_avg))


if __name__ == '__main__':
    main()
