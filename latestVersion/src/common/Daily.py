import CtrInacWindow
import cv2,time
import Functions
from latestVersion.src.common import Flows

from latestVersion.src.common.Flows import chYuHun, mainPagePoiReduction, mainPageToTanSuo

class Daily:
    # 单人探索
    def __init__(self, HWND, BBOX, IMGS, L_BOARDER, U_BOARDER):
        self.HWND = HWND
        self.BBOX = BBOX
        self.IMGS = IMGS
        self.L_BOARDER = L_BOARDER
        self.U_BOARDER = U_BOARDER

    def solo(self):
        # chYuHun(self, "", "")
        # mainPagePoiReduction(self)
        mainPageToTanSuo(self)

    # 单人御魂
    def huntu_solo(self):
        self.commonFight('yuhun_gerentiaozhan');

    # 刷业原火
    def yeyuahuo_solo(self):
        self.commonFight('yeyuanhuo_tiaozhan');

    # 御灵挑战
    def yuling_solo(self):
        self.commonFight('yuling_tiaozhan');

    # 觉醒挑战
    def juexing_solo(self):
        self.commonFight('juexing_tiaozhan');

    # 活动挑战（需及时更换活动挑战按钮图片）
    def huodong_solo(self):
        self.commonFight('huodong_tiaozhan');
    
    # 魂土开车司机  
    def huntu_driver(self):      
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['yuhuntiaozhan']
            pts = Functions.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                time.sleep(1)
                CtrInacWindow.click_inactive_window(hwnd, pts)

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['zhunbei']
            pts = Functions.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                print("检测到司机准备按钮")
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = Functions.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                print("司机准备完毕")
                time.sleep(19)
                continue

            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = Functions.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 40)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = Functions.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(1)
                    break

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['yaoqing']
            pts = Functions.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = Functions.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.5)

            want = imgs['queding']
            pts = Functions.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = Functions.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.1)
                continue
            time.sleep(2)

    # 魂土打手
    def huntu_fighter(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['zhunbei']
            pts = Functions.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                print("检测到打手准备按钮")
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = Functions.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                print("打手准备完毕")
                time.sleep(19)
                continue

            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = Functions.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 50)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = Functions.cheat(posi_1, 5, 5)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(1)
                    break

            Functions.autoReceive(hwnd, imgs, bbox)
            Functions.fixTeam(hwnd, imgs, bbox)
            time.sleep(2)

    # 单刷御灵，觉醒，御魂，业原火的共通方法
    # imageName:图片名称
    def commonFight(self, imageName: any):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            Flows.closeCollaborativeTask(self);
            pts = Functions.getPosition(hwnd, imgs, imageName)[0]
            screen = Functions.getPosition(hwnd, imgs, imageName)[1]
            if not len(pts) == 0:
                print("检测到进攻按钮按钮")
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                jingong = Functions.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, jingong)
                print("开始吧")
                time.sleep(19)
                continue

            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = Functions.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 50)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    jixu = Functions.cheat(posi_1, 5, 5)
                    CtrInacWindow.click_inactive_window(hwnd, jixu)
                    time.sleep(1)
                    break
            time.sleep(1.2)
