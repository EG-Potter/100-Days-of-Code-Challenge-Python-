def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if wall_on_right() and front_is_clear() :
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    else:
        if (wall_on_right() != True) and front_is_clear() :
            move()
        else:
            turn_right()