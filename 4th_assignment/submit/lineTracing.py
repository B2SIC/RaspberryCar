from carModule import *


def lineTracing():

    while True:
        # set OTD ~ OTE
        output = get_DBACE()
        dis = getDistance()
        OTD, OTB, OTA, OTC, OTE = output[0], output[1] ,output[2], output[3], output[4]

        # Show me output, dis
        print(output, dis)

        if dis < 17:
            avoidObstacle()
        else:
            # Line Tracing Start ##############################
            # 라인 이탈 (All White)
            if OTD == 1 and OTB == 1 and OTA == 1 and OTC == 1 and OTE == 1:
                go_forward_diff(90, 5)
            # 감지 불가 (All Black)
            elif OTD == 0 and OTB == 0 and OTA ==0 and OTC == 0 and OTE == 0:
                go_forward_diff(0, 0)
            # 중앙 감지
            elif OTD == 1 and OTB == 1 and OTA == 0 and OTC == 1 and OTE == 1:
                go_forward_diff(70, 70)
            # 왼쪽으로 치우친 중앙 감지
            elif OTB == 0:
                go_forward_diff(30, 65)
            # 오른쪽으로 치우친 중앙 감지
            elif OTC == 0:
                go_forward_diff(65, 30)
            # 왼쪽으로 심하게 치우침
            elif OTD == 0:
                go_forward_diff(5, 90)
            # 오른쪽으로 심하게 치우침
            elif OTE == 0:
                go_forward_diff(90, 5)
            else:
                go_forward_diff(0, 0)

            sleep(0.1)

def avoidObstacle():
    go_forward_diff(0, 0)
    sleep(0.5)
    rightPointTurn(35, 0.5)
    go_forward_diff(60, 60)
    sleep(0.8)
    leftPointTurn(35, 0.7)
    go_forward_diff(60, 60)
    sleep(0.3)

if __name__ == '__main__':
    try:
        setup()
        lineTracing()
    except KeyboardInterrupt:
        pwm_low()
        GPIO.cleanup()
