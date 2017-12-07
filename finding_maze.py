from carModule import *
from time import sleep


def findMaze():
    while True:
        output = get_DBACE()
        OTD, OTB, OTA, OTC, OTE = output[0], output[1] ,output[2], output[3], output[4]

        print(output)

        # MainCase: E = 0 (우측 교차로 우회전)
        if OTA == 0 and OTE == 0:
            go_forward_diff(0, 0)
            sleep(0.3)

            go_forward_diff(40, 40)
            sleep(0.5)

            rightPointTurn(40, 0.5)
            go_forward_diff(0, 0)
            sleep(0.3)

            rightPointTurn(50, 0.1)
            get_line()

            go_forward_diff(0, 0)
            sleep(0.5)

        # 직진
        elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 1 and OTE == 1:
            go_forward_diff(70, 70)

        # Case: 왼쪽으로 살짝 치우쳐짐
        elif OTB == 0:
            go_forward_diff(30, 65)
        # Case: 오른쪽으로 살짝 치우쳐짐
        elif OTC == 0:
            go_forward_diff(65, 30)

        elif OTD == 0 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(5, 90)
        elif OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 0:
            go_forward_diff(90, 5)

        # MainCase: [1,1,1,1,1] (uTurn or Left Turn)
        elif OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
            go_forward_diff(0, 0)
            sleep(0.3)

            go_forward_diff(40, 40)
            sleep(0.5)

            leftPointTurn(40, 0.5)
            go_forward_diff(0, 0)
            sleep(0.3)

            leftPointTurn(50, 0.1)
            get_line()

            go_forward_diff(0, 0)
            sleep(0.5)

        sleep(0.02)


def get_line():
    while get_DBACE()[2]:
        continue


if __name__ == '__main__':
    try:
        setup()
        findMaze()
    except KeyboardInterrupt:
        pwm_low()
        GPIO.cleanup()