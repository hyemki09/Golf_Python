import numpy as np
from anal_poses.utils import p3_angle
from anal_poses.utils import p2_diff


# 1번 자세
class Address:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()

    # 도훈 만듬 (스탠스 거리)
    def stance(self):
        rfoot = self.kp[0][11]
        lfoot = self.kp[0][14]

        neck = self.kp[0][1]

        height = (lfoot - neck)[1]

        diff = np.array(rfoot) - np.array(lfoot) / height

        # 640 * 640 이미지 기준
        # -50~ 50 사이
        if -0.2 <= diff[0] <= -0.5:
            self.feedback["stance"] = {
                0: 2,
                1: diff[0],
                2: "스탠스 자세에서 양발의 위치가 완벽합니다.",
            }
        elif -0.4 <= diff[0] <= -0.1:
            self.feedback["stance"] = {
                0: 1,
                1: diff[0],
                2: "골반과 몸통이 축을 중심으로 회전하지 않고, 좌우로 밀리고 있습니다. 스윙의 축이 변하여 정확한 임팩트가 어렵고 거리 손실을 보게 됩니다."
            }
        else:
            self.feedback["stance"] = {
                0: 0,
                1: diff[0],
                2: "골반과 몸통이 축을 중심으로 회전하지 않고, 좌우로 밀리고 있습니다. 스윙의 축이 변하여 정확한 임팩트가 어렵고 거리 손실을 보게 됩니다."
            }











    # 도훈 만듬 (측면 무릎 각도)

    def knee_angle(self):
        upfoot = self.kp[0][9]
        middlefoot = self.kp[0][10]
        downfoot = self.kp[0][11]

        angle = p3_angle(upfoot, middlefoot, downfoot)

        if 154 <= angle <= 156:
            self.feedback["knee_angle"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 150 <= angle <= 161:
            self.feedback["knee_angle"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["knee_angle"] = {
                0: 0,
                1: angle,
                2: "Bad"
            }

    # 도훈 만듬 (측면 허리 각도)

    def back_angle(self):
        oue = self.kp[0][9]
        chukan = self.kp[0][10]
        sita = self.kp[0][11]

        angle = p3_angle(oue, chukan, sita)

        if 148 <= angle <= 153:
            self.feedback["back_angle"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 144 <= angle <= 147:
            self.feedback["back_angle"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["back_angle"] = {
                0: 0,
                1: angle,
                2: "Bad"
            }

    def run(self):

        self.stance()
        self.knee_angle()  # 측면
        self.back_angle()  # 측면
        return self.feedback



KOREAN_KEYWORD = {
    "stance" : "스탠스",
    "knee_angle" : "무릎 각도",
    "back_angle" : "등 각도"
}