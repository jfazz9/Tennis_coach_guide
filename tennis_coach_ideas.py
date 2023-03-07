'''Combination of tennis shots to work on in training'''


shot_action = ["drop-shot", "drive", "lob"]
spin_shot = ["topspin", "slice", "backspin", "flat"]
direction = ["straight", "angle"]
landing = ["deep", "middle", "short"]
# Groundstrokes
shot_side = ["Forehand", "Backhand"]


# if middle and angle continue
# if drop-shot and deep or middle
for type in shot_side:
    for action in shot_action:
        for spin in spin_shot:
            for dir in direction:
                for land in landing:
                    if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                        continue
                    elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                        continue
                    else:
                        print(type +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')


# Net play
net_play = ["Volley", "Smash"]
print('HERE is the netplay')
for shot in net_play:
    for type in shot_side:
        for action in shot_action:
            for spin in spin_shot:
                for dir in direction:
                    for land in landing:
                        if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                            continue
                        elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                            continue
                        elif shot == 'Smash' and action == 'lob': # possible but not good for specfic training
                            continue
                        else:
                            print(type +' ' + shot +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')
 
# Serve
serve = ["Serve"]
speciality = ['underarm serve']
angles_serving = ['wide', 'middle', 'tee']


for s in serve:
    for action in shot_action:
        for spin in spin_shot:
            for dir in angles_serving:
                if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                        continue
                elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                    continue
                elif action == 'lob': # not possible to do a lob serve
                    continue
                elif spin == 'backspin': # yeah....
                    continue
                else:
                    print(spin +' ' + s + ' ' + action + ' ' + dir + ' ')


# Return of Serve
return_serve = ["Return Serve"]

for r in return_serve:
    for type in shot_side:
        for action in shot_action:
            for spin in spin_shot:
                for dir in direction:
                        for land in landing:
                            if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                                continue
                            elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                                continue
                            else:
                                print(r + ' ' + type +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')


