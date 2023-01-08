from latestVersion.src.common.Flows import chYuHun


class Daily:
    # 单人探索
    def __init__(self, HWND, BBOX, IMGS, L_BOARDER, U_BOARDER):
        self.HWND = HWND
        self.BBOX = BBOX
        self.IMGS = IMGS
        self.L_BOARDER = L_BOARDER
        self.U_BOARDER = U_BOARDER

    def solo(self):
        chYuHun(self, "", "")
