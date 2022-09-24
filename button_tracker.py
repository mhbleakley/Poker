class ButtonTracker:

    def __init__(self, player_list):
        self.player_list = player_list
        self.button_position = 0
        self.small_blind = self.player_list[self.button_position]
        self.big_blind = self.player_list[self.button_position + 1]

    def redefine_blinds(self, split=False):
        if split:
            self.small_blind = self.player_list[-1]
            self.big_blind = self.player_list[0]
        else:
            self.small_blind = self.player_list[self.button_position]
            self.big_blind = self.player_list[self.button_position + 1]
    
    def rotate_button(self):
        self.button_position += 1
        if self.button_position == len(self.player_list - 1):
            self.redefine_blinds(split=True)
            self.button_position = -1
        else:
            self.redefine_blinds()

    def small(self):
        return self.small_blind

    def big(self):
        return self.big_blind

    def smalln(self):
        return self.small_blind.name

    def bign(self):
        return self.big_blind.name

