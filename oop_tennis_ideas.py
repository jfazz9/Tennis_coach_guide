class Tennis:
    def __init__(self):

        #shot details
        self.shot_action = ["drop-shot", "drive", "lob"]
        self.spin_shot = ["topspin", "slice", "backspin", "flat"]
        self.direction = ["straight", "angle"]
        self.landing = ["deep", "middle", "short"]
        self.angles_serving = ['wide', 'middle', 'tee']
        
        # game situation
        self.return_serve = ["Return Serve"]
        self.shot_side = ["Forehand", "Backhand"]
        self.serve = ["Serve"]
        self.net_play = ["Volley", "Smash"]
    
    def groundstrokes(self): # returns all grounstroke combinations
        file = []
        for type in self.shot_side:
            for action in self.shot_action:
                for spin in self.spin_shot:
                    for dir in self.direction:
                        for land in self.landing:
                            if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                                continue
                            elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                                continue
                            elif action == 'lob' and land != 'deep': # no short lobs here
                                    continue 
                            else:
                                file.append(type +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')
        return file
    
    def net(self):
        file = []
        for shot in self.net_play:
            for type in self.shot_side:
                for action in self.shot_action:
                    for spin in self.spin_shot:
                        for dir in self.direction:
                            for land in self.landing:
                                if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                                    continue
                                elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                                    continue
                                elif shot == 'Smash' and action == 'lob': # possible but not good for specfic training
                                    continue
                                elif action == 'lob' and land != 'deep': # no short lobs please
                                    continue 
                                else:
                                    file.append(type +' ' + shot +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')
        return file

    def serving(self):
        file = []
        for s in self.serve:
            for action in self.shot_action:
                for spin in self.spin_shot:
                    for dir in self.angles_serving:
                        if action == 'drop-shot': # ignoring drop shots that land near the back or middle of court
                                continue
                        elif action == 'lob': # not possible to do a lob serve
                            continue
                        elif spin == 'backspin': # yeah....
                            continue
                        else:
                            file.append(spin +' ' + s + ' ' + dir + ' ')
        return file
    
    def return_of_serve(self):
        file = []
        for r in self.return_serve:
            for type in self.shot_side:
                for action in self.shot_action:
                    for spin in self.spin_shot:
                        for dir in self.direction:
                                for land in self.landing:
                                    if action == 'drop-shot' and land in ["deep", "middle"]: # ignoring drop shots that land near the back or middle of court
                                        continue
                                    elif action == 'drop-shot' and spin in ['flat', 'topspin']: # you wouldn't do a topspin drop shot, Would youuu??? :)
                                        continue
                                    elif action == 'lob' and land != 'deep': # short lobs?? nope not here
                                        continue 
                                    else:
                                        file.append(r + ' ' + type +' ' + spin + ' ' + action + ' ' + dir + ' ' + land + ' ')
        return file
    
    def all_tennis_shots(self):
        return Tennis.groundstrokes(self), Tennis.net(self), Tennis.serving(self), Tennis.return_of_serve(self)
    



if __name__=="__main__":
    manual = Tennis()

    with open('manual.txt', 'w') as files:
        shots = manual.all_tennis_shots()
        for shot in shots:
            for detail in shot:
                files.write(detail + '\n')

        