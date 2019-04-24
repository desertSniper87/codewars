class Thing ():


    def __init__(self, name):
        self.name = name

        if name not in ['arm', 'head', 'eye', 'finger']:
            self.is_a_woman = name == 'Jane'
            self.is_a_man = not self.is_a_woman
            self.parent_of = 'joe'

            left_arm = Thing('arm')
            right_arm = Thing('arm')
            self.arms = (left_arm, right_arm)

            self.head = Thing('head')

            self.is_head = False
            self.is_arm = False
            self.is_eye = False
            self.is_finger = False

        elif self.name == 'arm':
            self.is_arm = True
            self.is_a_man = False
            self.is_a_woman = False
            self.is_head = False
            self.is_eye = False

            self.fingers = []
            for i in range(5):
                self.fingers.append(Thing('finger'))


        # if self.name != 'head' and self.is_arm!=True:

        elif self.name == 'head':
            self.is_head = True
            left_eye = Thing('eye')
            right_eye = Thing('eye')
            self.eyes = (left_eye, right_eye)
            self.is_arm = False

        elif self.name == 'eye':
            self.color = 'blue'
            self.shape = 'round'





