def main():
    time = convert(input('What time is it? '))
    #print(convert(time))

    if 8 >= time >= 7:
        print('breakfast time')
    elif 13 >= time >= 12:
        print('lunch time')
    elif 19 >= time >= 18:
        print('dinner time')

def convert(time):
    time = time.split(':')
    return int(time[0]) + (int(time[1]) / 60)


if __name__ == "__main__":
    main()
