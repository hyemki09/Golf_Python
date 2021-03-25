import numpy as np
from anal_poses.utils import p3_angle


# 1번 자세
class Release:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()

    def chicken_wing(self):
        lshoulder = self.kp[6][5]
        lelbow = self.kp[6][6]
        lwrist = self.kp[6][7]

        angle = p3_angle(lshoulder, lelbow, lwrist)

        if 165 <= angle <= 180:
            self.feedback["chicken_wing"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 155 <= angle <= 180:
            self.feedback["chicken_wing"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["chicken_wing"] = {
                0: 0,
                1: angle,
                2: "bad"
            }






# 측면 허리각도
    def back_angle(self):
        lshoulder = self.kp[6][1]
        lhip = self.kp[6][8]
        lwrist = self.kp[6][9]

        angle = p3_angle(lshoulder, lhip, lwrist)

        if 70 <= angle <= 85:
            self.feedback["back_angle"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 65 <= angle <= 92:
            self.feedback["back_angle"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["back_angle"] = {
                0: 0,
                1: angle,
                2: "bad"
            }

    def run(self):
        self.chicken_wing()
        self.back_angle()
        return self.feedback



KOREAN_KEYWORD = {
    "chicken_wing": "임팩트시 손목이 클럽보다 빠르게 나와야함",
    "back_angle": "백스윙때의 척추의 각도와 임팩트시 척추의 각도는 그대로 유지"
}