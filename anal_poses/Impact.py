import numpy as np
from anal_poses.utils import p3_angle
from anal_poses.utils import p2_diff


# 도훈 만듬 임팩트시 손목의 위치
class Impact:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()


    def left_foot(self):
        lhip = self.kp[4][12]
        lfoot = self.kp[4][14]
        line = [lfoot[5],lhip[7]]

        angle = p3_angle(lhip, lfoot, line)

        if 6 <= angle <= 12.5:
            self.feedback["left_foot"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 2.5 <= angle <= 16:
            self.feedback["left_foot"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["left_foot"] = {
                0: 0,
                1: angle,
                2: "bad"
            }


    def wrist_impact(self):
        lshoulder = self.kp[5][5]
        lelbow = self.kp[5][6]
        lwrist = self.kp[5][7]

        angle = p3_angle(lshoulder, lelbow, lwrist)

        if 160 <= angle <= 180:
            self.feedback["wrist_impact"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 150 <= angle <= 169:
            self.feedback["wrist_impact"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["wrist_impact"] = {
                0: 0,
                1: angle,
                2: "bad"
            }








        # 측면 임팩트 시 머리 유지
    def head(self):


        lfoot = self.kp[5][14]
        neck = self.kp[5][1]

        height = (lfoot - neck)[1]

        lf_address = self.kp[0][21] / height
        lf_backswing = self.kp[2][21] / height

        diff = p2_diff(lf_address, lf_backswing)

        if -0.1 <= diff[1] <= 0.2:
            self.feedback["head"] = {
                0: 2,
                1: diff[1],
                2: "Good"
            }
        elif -0.3 <= diff[1] <= -25:
            self.feedback["head"] = {
                0: 0,
                1: diff[1],
                2: "So SO"
            }
        else:
            self.feedback["head"] = {
                0: 0,
                1: diff[1],
                2: "bad"
            }


        #측면 척추 각도도
    def back_angle(self):
        lshoulder = self.kp[5][0]
        lelbow = self.kp[5][8]
        lwrist = self.kp[5][9]

        angle = p3_angle(lshoulder, lelbow, lwrist)

        if 55 <= angle <= 65:
            self.feedback["back_angle"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 45 <= angle <= 70:
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

        self.wrist_impact()
        self.left_foot()
        self.head()  # 측면
        self.back_angle()  # 측면

        return self.feedback


KOREAN_KEYWORD = {
    "wrist_impact": "임팩트시 손목이 위치",
    "left_foot": "임팩트시 왼쪽 무릎의 각도",
    "head": "임팩트시 머리의 위치",
    "back_angle": "백스윙때의 척추의 각도와 임팩트시 척추의 각도"
}