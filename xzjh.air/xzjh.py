# -*- encoding=utf8 -*-
__author__ = "Holy"

import time
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

class XZJH:
    def __init__(self, device_url):
        # self.driver = connect_device("Android:///{}".format(device_url))
        auto_setup(__file__, logdir=True, devices=[
            "Android:///{}".format(device_url)
        ])

        self.package = "com.game.xiuzhenjianghu"
        self.poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        # 这只默认0区，防止先使用了logger
        self.zone = None
        
        stop_app(self.package)
        sleep(1)
        start_app(self.package)
        sleep(10)
        
    def logger(self, msg, level = 'INFO'):
        """
        :日志输出, level 默认 INFO, 暂时没分级
        """
        curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("[{}] [{}] <{} - {}> : {}".format(curr_time, level, self.package, self.zone, msg))
        
    def login(self, zone):
        """
        :登录游戏
        :zone: 数字
        """
        self.logger(msg = "invoke login()", level = 'DEBUG')
        # 等待登录按钮
        wait(Template(r"tpl1568895558005.png", record_pos=(-0.003, 0.046), resolution=(720, 1280)))
        # 登录
        touch(Template(r"tpl1568895537732.png", record_pos=(0.001, 0.042), resolution=(720, 1280)))
        # 选区
        self.choice_zone(zone)
        
    def switch_account(self, zone):
        """
        :切换账号
        """
        self.logger(msg = "invoke switch_account()", level = 'DEBUG')
        if not exists(Template(r"tpl1568900285945.png", record_pos=(-0.454, -0.224), resolution=(720, 1280))):
            self.logger(msg = "Setting not exit, Don't switch account!")
            return
        # 设置
        touch(Template(r"tpl1568900285945.png", record_pos=(-0.454, -0.224), resolution=(720, 1280)))
        sleep(0.5)
        # 切换账号
        touch(Template(r"tpl1568900371402.png", record_pos=(0.163, 0.1), resolution=(720, 1280)))
        sleep(1)
        # 重新登录即可
        self.login(zone)

        
    def choice_zone(self, zone):
        """
        :选择服务器区 (只支持3, 4)
        :zone: 数字
        """
        self.logger(msg = "invoke choice_zone()", level = 'DEBUG')
        # 等待换区按钮出现
        wait(Template(r"tpl1568895677517.png", record_pos=(0.196, 0.074), resolution=(720, 1280)))
        # 点击换区按钮
        touch(Template(r"tpl1568895677517.png", record_pos=(0.196, 0.074), resolution=(720, 1280)))
        sleep(1)
        if zone == 3:
            touch(Template(r"tpl1568895759506.png", record_pos=(0.188, -0.099), resolution=(720, 1280)))
        else:
            touch(Template(r"tpl1568895840851.png", record_pos=(-0.185, -0.1), resolution=(720, 1280)))
        # 保存当前所在区
        self.zone = zone
        sleep(1)
        # 进入游戏
        touch(Template(r"tpl1568895871774.png", record_pos=(0.004, 0.456), resolution=(720, 1280)))
        self.logger(msg = "current login zone is {}".format(zone))
        
    def confirm(self, msg = None):
        """
        :有确认框
        :msg: 确认消息
        """
        flag = False
        if exists(Template(r"tpl1568816227547.png", record_pos=(0.211, 0.149), resolution=(720, 1280))):
            touch(Template(r"tpl1568816227547.png", record_pos=(0.211, 0.149), resolution=(720, 1280)))
            flag = True
            self.logger(msg = "confirm or upgrade: {}".format(msg))
        sleep(1)
        return flag
    
    def purchase(self, name):
        """
        :购买
        """
        # 点击最大
        touch(Template(r"tpl1568900020046.png", record_pos=(0.294, 0.075), resolution=(720, 1280)))
        sleep(0.5)
        self.confirm(name)
    
    def go_home(self):
        """
        :返回主页
        """
        if not exists(Template(r"tpl1568898131729.png", record_pos=(0.444, -0.821), resolution=(720, 1280))):
            self.logger(msg = "Return button isn't exists, Can't go to homepage!")
            return
        touch(Template(r"tpl1568898131729.png", record_pos=(0.444, -0.821), resolution=(720, 1280)))
        self.logger(msg = "Go to homepage")
        sleep(0.5)

    def shenshou(self):
        """
        :神兽升级
        """
        self.logger(msg = "invoke shenshou()", level = 'DEBUG')
        if not exists(Template(r"tpl1568991919770.png", record_pos=(0.403, 0.768), resolution=(720, 1280))):
            self.logger(msg = "ShenShou not exists, This isn't the homepage!")
            return
        # 进入神兽界面
        touch(Template(r"tpl1568991919770.png", record_pos=(0.403, 0.768), resolution=(720, 1280)))
        sleep(0.5)
        # 点击 极·蛮蛮
        if not exists(Template(r"tpl1568992084275.png", record_pos=(-0.265, -0.2), resolution=(720, 1280))):
            self.logger(msg = "极·蛮蛮 不存在！")
            # 直接返回主页
            self.go_home()
            return
        touch(Template(r"tpl1568992084275.png", record_pos=(-0.265, -0.2), resolution=(720, 1280)))
        sleep(0.5)
        touch(Template(r"tpl1568992249297.png", record_pos=(0.276, 0.7), resolution=(720, 1280)))
        self.confirm()
        # 返回主页
        self.go_home()
    
    def shopping(self):
        """
        :购物
        """
        self.logger(msg = "invoke shopping()", level = 'DEBUG')
        if not exists(Template(r"tpl1568899642834.png", record_pos=(-0.392, 0.775), resolution=(720, 1280))):
            self.logger(msg = "Shop not exists, This isn't the homepage！")
            return
        # 进入商盟
        touch(Template(r"tpl1568899642834.png", record_pos=(-0.392, 0.775), resolution=(720, 1280)))
        sleep(1)
        # 进入地源堂首层
        touch(Template(r"tpl1568899756919.png", record_pos=(0.001, -0.164), resolution=(720, 1280)))
        sleep(1)
        # 进入地源堂二层
        touch(Template(r"tpl1568899784237.png", record_pos=(0.324, -0.163), resolution=(720, 1280)))
        sleep(1)
        # 点击姚曦 or 陈玄澄
        if exists(Template(r"tpl1568899822820.png", record_pos=(-0.351, 0.419), resolution=(720, 1280))):
            touch(Template(r"tpl1568899822820.png", record_pos=(-0.351, 0.419), resolution=(720, 1280)))
        elif exists(Template(r"tpl1569028635894.png", record_pos=(-0.35, 0.424), resolution=(720, 1280))):
            touch(Template(r"tpl1569028635894.png", record_pos=(-0.35, 0.424), resolution=(720, 1280)))
        else:
            # 异常返回主页
            self.go_home()
            return
        sleep(1)
        # 交易
        touch(Template(r"tpl1568899847897.png", record_pos=(-0.021, 0.192), resolution=(720, 1280)))
        # 元婴丹
        touch(Template(r"tpl1568991401177.png", record_pos=(0.035, -0.44), resolution=(720, 1280)))

        self.purchase("元婴丹")
        # 昊元丹
        touch(Template(r"tpl1568991358670.png", record_pos=(0.035, 0.163), resolution=(720, 1280)))
        self.purchase("昊元丹")
        # 返回主页(需要返回两次)
        self.go_home()
        self.go_home()

        
    def fuben(self):
        """
        :执行副本(常规地图)
        """
        self.logger(msg = "invoke fuben()", level = 'DEBUG')
        if not exists(Template(r"tpl1568896166678.png", record_pos=(-0.408, 0.243), resolution=(720, 1280))):
            self.logger(msg = "FuBen not exists, This isn't the homepage！")
            return
        # 进入副本
        touch(Template(r"tpl1568896166678.png", record_pos=(-0.408, 0.243), resolution=(720, 1280)))
        sleep(1)
        # 常规地图
        # 滑到底部, 5次差不多了
        for _ in range(5):
            swipe(Template(r"tpl1568896550173.png", record_pos=(-0.057, 0.431), resolution=(720, 1280)), vector=[-0.08, -0.2198])
            sleep(0.5)
        # 4个地图全点一遍
        self.fuben_click_auto("一 南轩草原", Template(r"tpl1568904820816.png", record_pos=(0.296, 0.787), resolution=(720, 1280)))
        self.fuben_click_auto("二 北漠原", Template(r"tpl1568991634842.png", record_pos=(0.296, 0.429), resolution=(720, 1280)))

        self.fuben_click_auto("三 桂花坪", Template(r"tpl1568991675198.png", record_pos=(0.294, 0.076), resolution=(720, 1280)))

        self.fuben_click_auto("四 望春林", Template(r"tpl1568991690577.png", record_pos=(0.299, -0.283), resolution=(720, 1280)))

        # 退出副本
        self.go_home()
        
    def fuben_click_auto(self, name, auto_btn):
        """
        :副本点击自动
        """
        if exists(auto_btn):
            touch(auto_btn)
            sleep(0.5)
            # 存在最大按钮则弹出了确认框, 直接循环点一遍, 不然没在做任务也会出确认框
            max_btn = Template(r"tpl1568897762850.png", record_pos=(0.312, -0.061), resolution=(720, 1280))
            if exists(max_btn):
                touch(max_btn)
                self.confirm("{} 副本自动".format(name))
    
    def dongfu(self):
        """
        : 洞府
        """
        self.logger(msg = "invoke dongfu()", level = 'DEBUG')
        if not exists(Template(r"tpl1568898265299.png", record_pos=(-0.199, 0.774), resolution=(720, 1280))):
            self.logger(msg = "DongFu not exists, This isn't the homepage！")
            return
        # 进入洞府
        # 仙圃
        touch(Template(r"tpl1568898265299.png", record_pos=(-0.199, 0.774), resolution=(720, 1280)))
        sleep(1)
        # 肉
        touch(Template(r"tpl1568898442957.png", record_pos=(0.332, -0.406), resolution=(720, 1280)))
        if self.confirm("升级 肉") == True:
            # 加4个工人
            for _ in range(4):
                touch(Template(r"tpl1568898876865.png", record_pos=(0.158, -0.422), resolution=(720, 1280)))
                sleep(0.5)
        # 木头
        touch(Template(r"tpl1568898488364.png", record_pos=(0.333, 0.157), resolution=(720, 1280)))
        self.confirm("升级 木头")
        # 药园 矿场 灵脉 不升
        
        # 进入灵根
        touch(Template(r"tpl1568898649325.png", record_pos=(0.231, -0.801), resolution=(720, 1280)))
        sleep(0.5)
        # 升级
        touch(Template(r"tpl1568904959876.png", record_pos=(0.35, -0.14), resolution=(720, 1280)))
        self.confirm("升级 灵根")
        touch(Template(r"tpl1568999235528.png", record_pos=(0.406, -0.601), resolution=(720, 1280)))
        self.confirm("升级 金")
        touch(Template(r"tpl1568999250006.png", record_pos=(0.407, -0.278), resolution=(720, 1280)))
        self.confirm("升级 土")
        touch(Template(r"tpl1568999271321.png", record_pos=(0.408, -0.524), resolution=(720, 1280)))
        self.confirm("升级 木")
        touch(Template(r"tpl1568999288592.png", record_pos=(0.406, -0.358), resolution=(720, 1280)))
        self.confirm("升级 火")
        touch(Template(r"tpl1568999305826.png", record_pos=(0.408, -0.444), resolution=(720, 1280)))
        self.confirm("升级 水")
        # 返回主页
        self.go_home()
        
    def execute(self):
        """
        :执行任务
        """
        self.shenshou()
        sleep(5)
        self.shopping()
        sleep(5)
        self.fuben()
        sleep(5)
        self.dongfu()
        sleep(5)
    
def main():
    # 要挂的区
    zones = [3, 4]
    # 常驻区坐标
    resident = 4
    # 切账号时间(s)
    switch_account_time = 10 * 60
    
    # xzjh = XZJH(device_url = "192.168.0.110:5555")
    xzjh = XZJH(device_url = "")
    xzjh.login(resident)
    # 记录登录时间
    login_time = time.time()
    # 记录执行次数
    exec_count = 0
    # 记录开始时间
    start_time = 0
    while True:
        start_time = time.time()
        xzjh.logger(msg = "main() exec count = {}".format(exec_count))
        xzjh.execute()
        if time.time() - login_time >= switch_account_time:
            for zone in zones:
                # 跳过当前区和常驻区
                if xzjh.zone == zone or zone == resident:
                    continue
                xzjh.switch_account(zone)
                sleep(1)
                xzjh.execute()
                sleep(5)
            # 切回常驻区
            xzjh.switch_account(resident)
            # 重置登录时间
            login_time = time.time()
        xzjh.logger(msg = "main() exec time = %.2fs" % (time.time() - start_time))
        sleep(2 * 60)
    
if __name__ == "__main__":
    main()
        
