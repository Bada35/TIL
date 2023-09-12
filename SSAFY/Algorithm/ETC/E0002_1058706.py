import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'E0002_1058706'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')

# 함수 선언 시작
size_ball = 5.73


def dot(start, end):
    return start[0] * end[0] + start[1] * end[1]


def cross(start, end):
    return math.fabs(start[0] * end[1] - start[1] * end[0])


def cal_angle(start, end):
    w = math.fabs(start[0] - end[0])
    h = math.fabs(start[1] - end[1])
    temp_angle = math.degrees(math.atan2(h, w))
    if (start[0] <= end[0]) and (start[1] <= end[1]):
        return 90.0 - temp_angle
    if (start[0] >= end[0]) and (start[1] <= end[1]):
        return 270.0 + temp_angle
    if (start[0] >= end[0]) and (start[1] >= end[1]):
        return 270.0 - temp_angle
    if (start[0] <= end[0]) and (start[1] >= end[1]):
        return 90.0 + temp_angle   


def find_destination(start, end):
    rad_angle = math.radians(cal_angle(start, end))
    dx = math.sin(rad_angle) * size_ball
    dy = math.cos(rad_angle) * size_ball
    return start[0] - dx, start[1] - dy


def cal_distance(start, end):
    w = math.fabs(start[0] - end[0])
    h = math.fabs(start[1] - end[1])
    return math.sqrt(w**2 + h**2)


def check_dist(start, end, ball):
    path_x = end[0] - start[0]
    path_y = end[1] - start[1]
    len_path = math.sqrt(path_x**2 + path_y**2)
    path = [path_x, path_y]
    vec_x = ball[0] - start[0]
    vec_y = ball[1] - start[1]
    vec = [vec_x, vec_y]
    dist = cross(path, vec)/len_path
    return dist



def play():
    global size_ball
    global angle
    global power
    global balls
    size_ball = 5.73
    if order == 1:
        tballs = [balls[1], balls[3]]
    else:
        tballs = [balls[2], balls[4]]
    
    whiteBall = [balls[0][0], balls[0][1]]
    blackBall = [balls[5][0], balls[5][1]]
    min_distance = 100000.0
    min_destination = [100, 100]
    min_dif = 90.0
    if tballs == [[-1.0, -1.0], [-1.0, -1.0]]:
        tballs = [blackBall]
    
    for ball in tballs:
        if (ball[0] == -1.0) and (ball[1] == -1.0):
            continue
        for hole in HOLES:
            len_distance = 0.0
            dif_angle = math.fabs(cal_angle(ball, hole) - cal_angle(whiteBall, ball))
            for check_ball in balls:
                if (check_ball == whiteBall) or (check_ball == ball):
                    continue

            len_distance += cal_distance(whiteBall, ball)
            len_distance += cal_distance(ball, hole) * math.cos(math.radians(dif_angle)) * 1.22
            if min_dif > dif_angle:
                min_dif = dif_angle
                min_distance = len_distance
                min_destination = find_destination(ball, hole)
    if min_dif > 80:
        size_ball = 5.3
    t_distance = cal_distance(whiteBall, min_destination)
    print('최소 거리', min_distance, '공까지 거리', t_distance)
    angle = cal_angle(whiteBall, min_destination)
     
    if min_distance > t_distance*2:
        power = min_distance * 0.2
    else:
        power = t_distance * 0.7
        

    return 

while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################


    play()


    ##############################

    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')