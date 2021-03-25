import numpy as np
from anal_poses.utils import p3_angle
from anal_poses.utils import p2_diff


# 1번 자세
class FollowThrough:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()

    def target(self):
        nose = self.kp[7][0]
        lfoot = self.kp[7][13]

        height = (nose - lfoot)[1]

        boob = self.kp[7][1]
        dick = self.kp[7][8]

        diff = p2_diff(boob, dick) / height

        if -0.01 <= diff[1] <= 0.01:
            self.feedback["target"] = {
                0: 2,
                1: diff[0],
                2: "Good"
            }
        else:
            self.feedback["target"] = {
                0: 0,
                1: diff[0],
                2: "Bad"
            }



    # 측면  마무리 자세시, 왼발과 허리의 궤도가 일치
    def side_target(self):
        nose = self.kp[7][0]
        lfoot = self.kp[7][13]

        height = (nose - lfoot)[1]

        boob = self.kp[7][8]
        dick = self.kp[7][9]

        diff = p2_diff(boob, dick) / height

        if 0.01 <= diff[1] <= 0.04:
            self.feedback["target"] = {
                0: 2,
                1: diff[0],
                2: "Good"
            }
        else:
            self.feedback["target"] = {
                0: 0,
                1: diff[0],
                2: "Bad"
            }

    def run(self):
        self.target()
        self.side_target()  # 측면
        return self.feedback


KOREAN_KEYWORD = {
    "target": "엉덩이가 목표물과 직각 유지",
    "side_target": "왼발과 허리가 일직선 유지",


}