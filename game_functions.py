import pygame
import sys
from bullets1 import Bullets
from aliens import Alien


def check_events(settings, screen, ship, bullets, play_button):
    """ checks for key/mouse events and responds"""
    # loop to check keypress events
    for event in pygame.event.get():
        # if escape key pressed, exit game
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            keydown_event(event, settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            keyup_event(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                settings.game_active = True


def keydown_event(event, settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    if event.key == pygame.K_q:
        ship.rotate_counterclockwise = True
    if event.key == pygame.K_e:
        ship.rotate_clockwise = True
    if event.key == pygame.K_SPACE:
        new_bullet = Bullets(settings, screen, ship)
        bullets.add(new_bullet)


def keyup_event(event, ship):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False
    if event.key == pygame.K_q:
        ship.rotate_counterclockwise = False
    if event.key == pygame.K_e:
        ship.rotate_clockwise = False


def update_screen(settings, screen, ship, bullets, aliens, play_button):
    # color the screen with background color
    screen.fill(settings.bg_color)

    if not settings.game_active:
        play_button.draw_button()

    elif settings.game_active:

        # draw new bullets on the screen; move bullets
        for bullet in bullets.sprites():
            bullet.draw_bullet()
            bullet.update()
            if bullet.rect.bottom < 0:
                bullet.kill()

        # draw fleet of aliens
        aliens.draw(screen)

        # update the ship
        ship.update()
        # draw the ship on the screen
        ship.blitme()

        aliens.update()

        # update_fleet(aliens)

        print_text(settings, screen)

    # update the display
    pygame.display.flip()


def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings, screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number

    aliens.add(alien)


def get_number_of_aliens(settings, alien_width):
    """determine the number of aliens that fit in a row"""
    available_space_x = settings.screen_width - 2 * alien_width
    number_of_aliens = int(available_space_x/(2*alien_width))
    return number_of_aliens


def get_number_rows(settings, alien_height, ship_height):
    available_space_y = settings.screen_height - 3 * alien_height - ship_height
    number_of_rows = int(available_space_y/(2*alien_height))
    return number_of_rows


def create_fleet(settings, screen, aliens, ship):
    """create a fleet of aliens"""
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = get_number_rows(settings, alien.rect.height, ship.rect.height)

    for row_number in range(number_of_rows):
        for alien_number in range(number_of_aliens):
            create_alien(settings, screen, aliens, alien_number, row_number)



"""def update_fleet(Aliens):
    if Aliens.check_wall() == True:
        for row_number in range(get_number_of_aliens):
            Aliens.rect.y += 30"""


def check_collision(bullets, aliens, settings, ship):
    alien_collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    ship_collision = pygame.sprite.spritecollideany(ship, aliens)
    if ship_collision:
        sys.exit()

    if alien_collision:
        settings.points += 1


def print_text(settings, screen):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Score: " + str(0 + settings.points), True, (255, 255, 255))
    screen.blit(surface, (430, 20))


def end_game(aliens, settings):
    for alien in aliens:
        if alien.rect.y == 570:
            print(settings.points)
            sys.exit()


