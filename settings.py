class Settings():
    """存储外星人入侵设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 128, 255)
        # 子弹设置
        self.bullet_width = 1200
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # 飞船设置

        # 飞船的个数
        self.ship_limit = 3

        self.fleet_drop_speed = 10
        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人的点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        # 飞船的速度设置
        self.ship_speed_factor = 1
        # 子弹的速度
        self.bullet_speed_factor = 5
        # 外星人的移动速度
        self.alien_speed_factor = 5

        # fleet_direction为1 表示向右移，为-1表示向左移
        self.fleet_direction = 1
        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        # print(self.alien_points)
