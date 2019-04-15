from bullet import Bullet


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果屏幕下子弹没有达到限制，就发射一个子弹"""

    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        # print(new_bullet)
        bullets.add(new_bullet)
