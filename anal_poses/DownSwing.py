import numpy as np
from anal_poses.utils import p3_angle
from anal_poses.utils import p2_diff


# 1번 자세
class DownSwing:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()

     # 도훈 만듬
    def sway_downswing(self):
        lhip_address = self.kp[0][9]
        lhip_downswing = self.kp[4][9]

        diff = p2_diff(lhip_address, lhip_downswing)

        if 280 <= diff[0] <= 310:
            self.feedback["sway_downswing"] = {
                0: 2,
                1: diff[0],
                2: "Good"
            }
        else:
            self.feedback["sway_downswing"] = {
                0: 0,
                1: diff[0],
                2: "Bad"
            }



    # 도훈 만듬 왼 발로 체중이동이 돼야 리버스 피벗이 안됨
    def bending_left_arm(self):
        lhip = self.kp[4][12]
        lfoot = self.kp[2][14]
        line = [lfoot[0], lhip[1]]

        angle = p3_angle(lhip, lfoot, line)

        if 6 <= angle <= 12.5:
            self.feedback["bending_arms"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 5 <= angle <= 16:
            self.feedback["bending_arms"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["bending_arms"] = {
                0: 0,
                1: angle,
                2: "bad"
            }

    # 도훈 만듬 다운 스윙시 손목 각도

    def wrist_angle_downswing(self):
        kkumchi = self.kp[4][3]
        lwrits = self.kp[4][4]
        clubhead = self.kp[4][25]

        angle = p3_angle(kkumchi, lwrits, clubhead)

        if 55 <= angle <= 90:
            self.feedback["wrist_angle_downswing"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 43 <= angle <= 110:
            self.feedback["wrist_angle_downswing"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["wrist_angle_downswing"] = {
                0: 0,
                1: angle,
                2: "bad"
            }



    # 도훈 만듬 (측면) 클럽헤드의 위치 파악
    def club_head(self):
        kkumchi = self.kp[4][3]
        lwrits = self.kp[4][4]
        clubhead = self.kp[4][25]

        angle = p3_angle(kkumchi, lwrits, clubhead)

        if 140 <= angle <= 170:
            self.feedback["club_head"] = {
                0: 2,
                1: angle,
                2: "Good."
            }
        elif 120 <= angle <= 180:
            self.feedback["club_head"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["club_head"] = {
                0: 0,
                1: angle,
                2: "bad"
            }

    def run(self):
        self.sway_downswing()
        self.bending_left_arm()
        self.wrist_angle_downswing()
        self.club_head()  # 측면
        return self.feedback


KOREAN_KEYWORD = {
    "sway_downswing": "다운스윙시 스웨이",
    "bending_left_arm": "왼팔의 구부러짐",
    "wrist_angle_downswing": "다운 스윙 중에 손목 각도 유지",
    "club_head": "클럽 헤드의 움직임"

}