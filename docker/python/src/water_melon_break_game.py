import random

LOWER_X_AXIS = 0
UPPER_X_AXIS = 2
LOWER_Y_AXIS = 0
UPPER_Y_AXIS = 2

def calc_diff(point1, point2):
    x_axis_diff = point1[0] - point2[0]
    y_axis_diff = point1[1] - point2[1]

    return (x_axis_diff, y_axis_diff)

def get_moving_range_of_player(player_point):
    lower_x = -player_point[0]
    upper_x = UPPER_X_AXIS - player_point[0]
    lower_y = -player_point[1]
    upper_y = UPPER_Y_AXIS - player_point[1]

    return (lower_x, upper_x, lower_y, upper_y)

water_melon_point = (
    random.randint(LOWER_X_AXIS, UPPER_X_AXIS),
    random.randint(LOWER_X_AXIS, UPPER_X_AXIS)
)
player_point = (
    random.randint(LOWER_Y_AXIS, UPPER_Y_AXIS),
    random.randint(LOWER_Y_AXIS, UPPER_Y_AXIS)
)

water_melon_output_message = 'スイカの位置は左から%dマス目, 上から%dマス目です。'
player_output_message = 'プレイヤーの位置は左から%dマス目, 上から%dマス目です。'

print(water_melon_output_message % water_melon_point)
print(player_output_message % player_point)

lower_x, upper_x, lower_y, upper_y = get_moving_range_of_player(player_point)

count = 0;
while(count < 3):
    remain_count = 3 - count
    val = input('スイカ割りを始めるにはそのままエンターキーを押してください。あと'+str(remain_count)+'回まで挑戦できます。')
    if val != '':
        print('言う通りにしなかったので終了します。')
        break

    # 2点間の距離
    diff_of_each_point = calc_diff(water_melon_point, player_point)
    print('2点間の距離:', diff_of_each_point)

	# プレイヤーがこれから移動する距離
    moving_distance = (random.randint(lower_x, upper_x), random.randint(lower_y, upper_y))
    print('これから移動する距離:', moving_distance)

    if diff_of_each_point == moving_distance:
        print('スイカが割れました！おめでとう！')
        break
    elif count < 2:
        print('残念！もう一回チャレンジしてね！')
        count += 1
        
        continue
    else:
        print('運がなかったみたいだね..')
        break