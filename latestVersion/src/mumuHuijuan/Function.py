import cv2
import time

import CaptureInactiveWindow
import CtrInacWindow
import Featurematcah
import action


class Daily:
    # 单人探索
    def __init__(self, HWND, BBOX, IMGS, L_BOARDER, U_BOARDER):
        self.HWND = HWND
        self.BBOX = BBOX
        self.IMGS = IMGS
        self.L_BOARDER = L_BOARDER
        self.U_BOARDER = U_BOARDER

    def getJiangli(self):
        flag = True
        flag1 = True
        flag2 = 0
        flag3 = 0
        while flag and flag2 < 5:
            hwnd = self.HWND
            bbox = self.BBOX
            imgs = self.IMGS
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])  # - L_Boarder
                    posi_1.append(pts[1] + bbox[1])  # - U_Boarder
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励:{}'.format(time.ctime()))
                    time.sleep(0.1)
                    flag2 = flag2 + 1
                    break

        while flag1 and flag2 < 5:
            hwnd = self.HWND
            bbox = self.BBOX
            imgs = self.IMGS
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])  # - L_Boarder
                    posi_1.append(pts[1] + bbox[1])  # - U_Boarder
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励:{}'.format(time.ctime()))
                    time.sleep(0.1)
                    flag1 = False
                    break
            flag2 = flag2 + 1

    def getPicturePoi(self, pictureName):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        screen = CtrInacWindow.capture_inactive_window(hwnd)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for i in [pictureName]:
            print('目标图片：', pictureName)
            posi_1 = []
            want = imgs[i]
            pts = action.locate_matchTemplate2(screen, want, 0)
            if not len(pts) == 0:
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                print('图片坐标：', posi_1[0], posi_1[1])
            time.sleep(2)

    def clickByPoi(self, poiX, poiY):
        hwnd = self.HWND
        screen = CtrInacWindow.capture_inactive_window(hwnd)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        posi_1 = []
        posi_1.append(poiX)
        posi_1.append(poiY)
        print('图片坐标：', posi_1[0], posi_1[1])
        print('点击坐标：', posi_1[0], posi_1[1])
        CtrInacWindow.click_inactive_window(hwnd, posi_1)
        time.sleep(1)

    def pingmudianjishijian(self, pictureName):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        screen = CtrInacWindow.capture_inactive_window(hwnd)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for i in [pictureName]:
            print('目标图片：', pictureName)
            posi_1 = []
            want = imgs[i]
            pts = action.locate_matchTemplate2(screen, want, 0)
            if not len(pts) == 0:
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                posi_1 = action.cheat(posi_1, 20, 20)
                print('点击图片：', pictureName)
                print('点击坐标：', posi_1[0], posi_1[1])
                CtrInacWindow.click_inactive_window(hwnd, posi_1)
            time.sleep(1)

    def tiaozhanshibaidianji(self, pictureName):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        findFlag = False
        t = 0
        for i in [pictureName]:
            print('目标图片：', pictureName)
            posi_1 = []
            want = imgs[i]
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            pts = action.locate_matchTemplate2(screen, want, 0)
            while len(pts) == 0 and not findFlag and t <= 10:
                want = imgs[i]
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                pts = action.locate_matchTemplate2(screen, want, 0)
                t = t + 1
                while not len(pts) == 0:
                    posi_1.append(pts[0] + bbox[0] - L_Boarder)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    print('点击图片：', pictureName)
                    print('点击坐标：', posi_1[0], posi_1[1])
                    time.sleep(2)
                    CtrInacWindow.click_inactive_window(hwnd, posi_1)
                    pts = []
                    findFlag = True
            time.sleep(1)

    def pingmudianjixiangduiweizhidianji(self, pictureName, relativePoiX, relativePoiY):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        screen = CtrInacWindow.capture_inactive_window(hwnd)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for i in [pictureName]:
            print('目标图片：', pictureName)
            posi_1 = []
            want = imgs[i]
            pts = action.locate_matchTemplate2(screen, want, 0)
            if not len(pts) == 0:
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                print('点击图片：', pictureName)
                print('点击坐标：', posi_1[0], posi_1[1])
                CtrInacWindow.click_inactive_window(hwnd, posi_1)
                time.sleep(2)
                posi_2 = action.changePoi(posi_1, relativePoiX, relativePoiY)
                print('点击坐标：', posi_2[0], posi_2[1])
                CtrInacWindow.click_inactive_window(hwnd, posi_2)
                time.sleep(1)

    def jiejietupo(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        screen = CtrInacWindow.capture_inactive_window(hwnd)
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        for i in ['tupojuan21', 'tupojuan22', 'tupojuan23', 'tupojuan24', 'tupojuan25', 'tupojuan26', 'tupojuan27',
                  'tupojuan28', 'tupojuan29', 'tupojuan30']:
            print('进入结界突破卷数量判断')
            posi_1 = []
            want = imgs[i]
            pts = action.locate_matchTemplate2(screen, want, 0)
            if not len(pts) == 0:
                print('确定结界突破卷数量大于20!')
                self.pingmudianjishijian('kun28chadiao')
                self.pingmudianjishijian('jiejietupoanniu')
                self.pingmudianjishijian('shishenlu')
                self.pingmudianjishijian('shishenlu_yushe')
                self.pingmudianjishijian('shishenlu_yushe_diyuguiwang')
                self.pingmudianjishijian('shishenlu_yushe_morenfenzu')
                self.pingmudianjixiangduiweizhidianji('shishenlu_yushe_morenfenzu_jiejietupo', 350, 0)
                self.pingmudianjishijian('shishenlu_yushe_quedinganniu')
                self.pingmudianjishijian('shishenlu_fanhui')
                # 突破9次
                self.clickByPoi(279, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(553, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(826, 150)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(2)
                self.clickByPoi(251, 268)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(553, 269)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(849, 271)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(2)
                self.clickByPoi(258, 390)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(552, 391)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(850, 390)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')

                # 退出8次
                self.clickByPoi(279, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(553, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(826, 150)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(251, 268)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(553, 269)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(849, 271)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(258, 390)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.clickByPoi(552, 391)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_tuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_querentuichuanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_shuaxinanniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_quedingshuaxinanniu')
                time.sleep(2)

                # 突破9次
                self.clickByPoi(279, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(553, 151)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(826, 150)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(2)
                self.clickByPoi(251, 268)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(553, 269)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(849, 271)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(2)
                self.clickByPoi(258, 390)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(552, 391)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.clickByPoi(850, 390)
                self.pingmudianjishijian('jiejietupo_jingonganniu')
                self.getJiangli()
                time.sleep(2)
                self.pingmudianjishijian('jiejietupo_suijianniu')
                time.sleep(1)
                self.pingmudianjishijian('jiejietupo_guanbianniu')
                time.sleep(1)
                self.pingmudianjishijian('kun28_hengban')
                time.sleep(1)
                continue

    def solo(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        flag = 0
        flag2 = 0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        print(w, h)
        while True:  # 直到取消，或者出错
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # 结界突破券数量判断
            want = imgs['guding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                want = imgs['exp']
                want2 = imgs['jian']
                want = want[0]
                pts = Featurematcah.surf(want, screen, 0.75)
                if len(pts) != 0 or flag2 < 5:
                    flag2 = flag2 + 1
                    if not len(pts) == 0:
                        print('***找到了经验怪***')
                        if pts[0] - w / 8 > 0 and pts[0] + w / 8 < w:
                            target = action.cut(screen, [pts[0] - w / 8, 0], [pts[0] + w / 8, pts[1]])
                            if target.shape[0] < want2[0].shape[0] or target.shape[1] < want2[0].shape[1]:
                                continue
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = [pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder, pts2[1] + bbox[1] - U_Boarder]
                                xx = action.cheat(posi_1, 10, 10)
                                print('***挑战经验怪***')
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(3)
                                flag2 = 0
                                continue
                            else:
                                continue
                        if pts[0] - w / 8 < 0:
                            target = action.cut(screen, [0, 0], [pts[0] + w / 8, pts[1]])
                            pts2 = action.locate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = [pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder, pts2[1] + bbox[1] - U_Boarder]
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                print('点击小怪')
                                flag2 = 0
                                time.sleep(1)
                                continue
                            else:
                                continue
                        if pts[0] + w / 8 > w:
                            target = action.cut(screen, [0, 0], [w, pts[1]])
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = [pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder, pts2[1] + bbox[1] - U_Boarder]
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(1)
                                flag2 = 0
                                continue
                            else:
                                continue
                    else:
                        continue
                else:
                    CtrInacWindow.drag_inactive_window(hwnd, bbox)
                    flag2 = 0
                    flag = 1 + flag
                    time.sleep(0.5)
                    if flag <= 1:
                        continue
                    for i in ['tuichu', 'queren']:
                        print('退出')
                        posi_1 = []
                        want = imgs[i]
                        pts = action.locate_matchTemplate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            print(want[0].shape)
                            posi_1 = action.cheat(posi_1, 20, 20)
                            # pyautogui.click(posi_1)
                            CtrInacWindow.click_inactive_window(hwnd, posi_1)
                            time.sleep(0.1)
                        screen = CaptureInactiveWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        continue
                    continue

            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])  # - L_Boarder
                    posi_1.append(pts[1] + bbox[1])  # - U_Boarder
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励:{}'.format(time.ctime()))
                    time.sleep(0.1)
                    flag2 = 0
                    break

            want = imgs['tansuo']
            target = screen
            pts = action.locate_matchTemplate(target, want, 0)
            if not len(pts) == 0:
                flag = 0
                print('重新进入地图')
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])  # - L_Boarder
                posi_1.append(pts[1] + bbox[1])  # - U_Boarder
                print(posi_1)
                xy = action.cheat(posi_1, 10, 10)
                print(xy)
                # 结界突破券数量判断
                self.jiejietupo()

                print('点击进入困28')
                CtrInacWindow.click_inactive_window(hwnd, posi_1)
                time.sleep(4)
                self.pingmudianjishijian('shishenlu')
                self.pingmudianjishijian('shishenlu_yushe')
                self.pingmudianjishijian('shishenlu_yushe_diyuguiwang')
                self.pingmudianjishijian('shishenlu_yushe_morenfenzu')
                self.pingmudianjixiangduiweizhidianji('shishenlu_yushe_morenfenzu_yuhuanjiaohuan', 350, 0)
                self.pingmudianjishijian('shishenlu_yushe_quedinganniu')
                self.pingmudianjishijian('shishenlu_fanhui')
                time.sleep(0.15)
