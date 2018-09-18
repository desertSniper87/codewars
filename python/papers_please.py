class Inspector:
    self.allow_nation = []
    self.deny_nation = []

    def receiveBulletin(self, bulletin):
        bulletin_words = bulletin.split(" ")
        if 'allow' in bulletin:
            self.allow.append(


