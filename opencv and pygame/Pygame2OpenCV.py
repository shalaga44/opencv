import pygame
import cv2
import numpy as np

pygame.init()
W, H = 720, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("pygame window")
CLOCK = pygame.time.Clock()
FPS = 25
BLACK = (0, 0, 0,)
WHITE = (255, 255, 255)
small_ball = pygame.image.load("purple_ball.png")
big_ball = pygame.image.load("orange_ball.png")
big_ball_x = 0
big_ball_y = 0
big_ball_velocity = 5
Game_Loop = True
while Game_Loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            Game_Loop = False
    # to get the mouse cursor position
    (mouse_x, mouse_y) = pygame.mouse.get_pos()
    # to hide mouse cursor
    pygame.mouse.set_visible(False)
    # small ball show
    screen.blit(small_ball, [mouse_x, mouse_y])
    # logic for the big ball to move with keyboard  in the display surface
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        big_ball_x += big_ball_velocity
    if keys[pygame.K_LEFT]:
        big_ball_x -= big_ball_velocity
    if keys[pygame.K_DOWN]:
        big_ball_y += big_ball_velocity
    if keys[pygame.K_UP]:
        big_ball_y -= big_ball_velocity
    # logic for the big ball to stay at the display surface
    if big_ball_x < 0:
        big_ball_x = 0
    if big_ball_y < 0:
        big_ball_y = 0
    if big_ball_x + big_ball.get_rect().width > W:
        big_ball_x = W - big_ball.get_rect().width
    if big_ball_y + big_ball.get_rect().height > H:
        big_ball_y = H - big_ball.get_rect().height
    # big ball show
    screen.blit(big_ball, [big_ball_x, big_ball_y])

    # converting pygame frame to opencv

    # This  is pygame reversed colourful pixels array in RGB
    RBG_rev_gray_array_pygame_frame = pygame.PixelArray(screen.copy())

    # This in the numpy array of reversed pygame gray decode frame
    RBG_rev_gray_array_pygame_frame = np.array(RBG_rev_gray_array_pygame_frame, 'uint8')

    # This in the right pygame colourful decode frame
    RBG_gray_array_pygame_frame = np.fliplr(np.rot90(RBG_rev_gray_array_pygame_frame[::-1, ::-1]))

    # This is the final pygame frame
    gray_frame = RBG_gray_array_pygame_frame

    # This  is pygame reversed colourful pixels array in RGB
    RBG_rev_color_array_pygame_frame = pygame.surfarray.array3d(screen.copy())

    # This in the numpy array of reversed pygame colourful decode frame
    RBG_rev_color_array_pygame_frame = np.array(RBG_rev_color_array_pygame_frame, 'uint8')

    # This in the right pygame colourful decode frame
    RBG_color_array_pygame_frame = np.fliplr(np.rot90(RBG_rev_color_array_pygame_frame[::-1, ::-1]))

    # This is the final pygame frame
    frame = cv2.cvtColor(RBG_color_array_pygame_frame, cv2.COLOR_RGB2BGR)

    # This line to show the frame in opencv window called Computer vision window
    cv2.imshow("Computer vision window", frame)
    cv2.waitKey(FPS)
    pygame.display.update()
    CLOCK.tick(FPS)
    screen.fill(BLACK)
pygame.quit()
cv2.destroyAllWindows()
