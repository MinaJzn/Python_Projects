import random

def monty_hall(number_of_round: int, switch_decision: bool)-> str:
    """Simulate a single Monty Hall game.

    :param switch_decision: If True, the contestant will switch their choice after a goat door is revealed.
    :return: Percent of winning in user rounds.
    """
    score = 0
    doors_keys = ['a', 'b', 'c']

    for _ in range(number_of_round):
        doors_content = ['goat', 'car', 'goat']
        random.shuffle(doors_content)
        doors = dict(zip(doors_keys, doors_content))
        
        player_initial_choice = random.choice(doors_keys)

        goat_doors=[]
        for door in doors_keys:
            if door != player_initial_choice and doors[door] == 'goat':
                goat_doors.append(door)        
        revealed_goat_door = random.choice(goat_doors)
        
        remaining_doors=[]
        for door in doors_keys:
            if door != player_initial_choice and door != revealed_goat_door:
                remaining_doors.append(door)

        if switch_decision:
            final_choice = remaining_doors[0]
        else:
            final_choice = player_initial_choice


        if doors[final_choice] == 'car':
            score += 1
            
    return (score / number_of_round) * 100


if __name__=="__main__":
    
    score_switch = monty_hall(100, True)
    score_no_switch = monty_hall(100, False)
    print(f'Winning percentage when switching: {score_switch:.1f}%')
    print(f'Winning percentage when NOT switching: {score_no_switch:.1f}%')