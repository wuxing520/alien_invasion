class Settings():
    """存储外星人入侵设置的类"""

    def __init__(self):
        """初始化游戏设置"""

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 128, 255)

        self.bullet_width = 800
        self.bullet_height = 650
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 飞船的速度设置
        self.ship_speed_factor = 1
        # 飞船的个数
        self.ship_limit = 1
        # 子弹的速度
        self.bullet_speed_factor = 5
        # 外星人的移动速度
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 10
        # fleet_direction为1 表示向右移，为-1表示向左移
        self.fleet_direction = 1
