def dividing_steps(number, divider):
    check_decimal = 1

    if number % divider == 0:
        check_decimal = 0

    if check_decimal == 1:
        recur = True
        phase = 1
        
        while(recur):
            result = number//divider
            if result != 0:
                shown = result
                remain = number % divider
                if remain != 0 and phase != 9:
                    print('Phase {}: number shown is {}, remaining {}, decimal {}'.format(phase, shown, remain, False))
                    number = remain
                    phase += 1
                    if phase == 9:
                        recur = False
                    else:
                        pass
                else:
                    print('Phase {}: number shown is {}, remaining {}, decimal {}'.format(phase, shown, remain, False))
                    recur = False
            else:
                number = number * 10
                result2 = number//divider
                remain = number%divider
                if phase !=9 and remain != 0:
                    print('Phase {}: number shown is {}, remaining {}, decimal {}'.format(phase, result2, remain, True))
                    number = remain
                    phase += 1
                    if phase == 9:
                        recur = False
                    else:
                        pass
                else:
                    print('Phase {}: number shown is {}, remaining {}, decimal {}'.format(phase, result2, remain, True))
                    recur = False
    else:
        shown = number // divider
        remain = number % divider
        print('Phase {}: number shown is {}, remaining {}, decimal {}'.format(1, shown, remain, False))


if __name__ == "__main__":
    number_choose = 11
    divider_choose =6

    dividing_steps(number_choose, divider_choose)