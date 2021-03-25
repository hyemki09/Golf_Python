import numpy as np
from anal_poses.utils import p3_angle
from anal_poses.utils import p2_diff


class Top:
    def __init__(self, kp):
        self.kp = kp
        self.feedback = dict()

    # 왼 팔의 구부러짐 체크
    def bending_left_arm(self):
        lshoulder = self.kp[3][5]
        lelbow = self.kp[3][6]
        lwrist = self.kp[3][7]

        angle = p3_angle(lshoulder, lelbow, lwrist)

        if 120 <= angle:
            self.feedback["bending_arms"] = {
                0: 2,
                1: angle,
                2: "팔 구부러짐이 없습니다."
            }
        elif 100 <= angle:
            self.feedback["bending_arms"] = {
                0: 1,
                1: angle,
                2: "손을 몸에서 멀리 밀면 클럽이 더 먼 거리를 이동하게 됩니다. 샷의 일관성 또한 향상됩니다. "
            }
        else:
            self.feedback["bending_arms"] = {
                0: 0,
                1: angle,
                2: "손을 몸에서 멀리 밀면 클럽이 더 먼 거리를 이동하게 됩니다. 샷의 일관성 또한 향상됩니다."
            }

    def reverse_pivot(self):
        lshoulder = self.kp[3][5]
        lfoot = self.kp[3][14]
        rfoot = self.kp[3][11]

        angle = p3_angle(lshoulder, lfoot, rfoot)

        if 50 <= angle <= 85:
            self.feedback["reverse_pivot"] = {
                0: 2,
                1: angle,
                2: "체중 이동이 정상적입니다.",
            }
        elif 85 < angle <= 100:
            self.feedback["reverse_pivot"] = {
                0: 1,
                1: angle,
                2: "백스윙 자세에서 체중이 앞발로 이동하고 있습니다. 역피봇은 볼의 윗부분을 맟출 확률을 높이고 thin shots를 유도합니다.",
            }
        else:
            self.feedback["reverse_pivot"] = {
                0: 0,
                1: angle,
                2: "백스윙 자세에서 체중이 앞발로 이동하고 있습니다. 역피봇은 볼의 윗부분을 맟출 확률을 높이고 thin shots를 유도합니다.",
            }



    def left_knee_moving(self):
        lhip = self.kp[3][12]
        lknee = self.kp[3][13]
        lfoot = self.kp[3][14]

        angle = p3_angle(lhip, lknee, lfoot)

        if 165 <= angle:
            self.feedback["left_knee_moving"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 150 <= angle:
            self.feedback["left_knee_moving"] = {
                0: 1,
                1: angle,
                2: "체중 이동 중 왼 다리가 과다하게 이동해서는 안 됩니다. 왼 무릎이 공을 바라본다고 생각하세요."
            }
        else:
            self.feedback["left_knee_moving"] = {
                0: 0,
                1: angle,
                2: "체중 이동 중 왼 다리가 과다하게 이동해서는 안 됩니다. 왼 무릎이 공을 바라본다고 생각하세요."
            }

    # 도훈 만듬


    def head_postion(self):
        nose_address = self.kp[0][0]
        nose_top = self.kp[3][0]

        diff = p2_diff(nose_address, nose_top)

        if 0 <= diff[1] <= 23:
            self.feedback["head_position"] = {
                0: 2,
                1: diff[0],
                2: "Good"
            }
        else:
            self.feedback["head_position"] = {
                0: 0,
                1: diff[0],
                2: "Bad"
            }

        # 도훈 만듬

    def back_face(self):
        lshoulder = self.kp[3][5]
        rshoulder = self.kp[3][2]
        lfoot = self.kp[3][14]

        angle = p3_angle(lshoulder, rshoulder, lfoot)

        if 70 <= angle <= 80:
            self.feedback["back_face"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 65 <= angle <=88:
            self.feedback["back_face"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["back_face"] = {
                0: 0,
                1: angle,
                2: "bad"
            }

    def club_head(self):
        rfoot = self.kp[3][11]
        lwrits = self.kp[3][4]
        ghead = self.kp[3][25]

        angle = p3_angle(rfoot, lwrits, ghead)

        if 95 <= angle <= 115:
            self.feedback["club_head"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 90 <= angle <= 120:
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




    #측면 왼팔의 구부러짐
    def side_bending_arm(self):
        lshoulder = self.kp[3][4]
        head = self.kp[3][25]
        lwrist = self.kp[3][5]

        angle = p3_angle(lshoulder, head, lwrist)

        if 0 <= angle <= 18:
            self.feedback["side_bending_arm"] = {
                0: 2,
                1: angle,
                2: "good"
            }
        elif 0 <= angle <= 60:
            self.feedback["side_bending_arm"] = {
                0: 1,
                1: angle,
                2: "So So"
            }
        else:
            self.feedback["side_bending_arm"] = {
                0: 0,
                1: angle,
                2: "bad"
            }


    def run(self):
        self.bending_left_arm()
        self.reverse_pivot()
        self.left_knee_moving()
        self.head_position()
        self.back_face()
        self.club_head()
        self.side_bending_arm()  #측면
        return self.feedback

KOREAN_KEYWORD = {
    "bending_left_arm": "왼 팔의 구부러짐",
    "reverse_pivot": "리버스 피벗",
    "left_knee_moving": "공을 향해 왼쪽 무릎 이동",
    "head_position": "머리의 포지션 유지",
    "back_face": "척추 각도가 일정하게 유지",
    "club_head": "클럽 헤드의 위치",
    "side_bending_arm" : "왼 팔 구부러짐"
}