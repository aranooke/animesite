import pygame 

game = pygame.init();


# game window
width = 500;
height = 500;
screen = pygame.display.set_mode((500,500));
pygame.display.set_caption("snake game");

# game variables
running = True;
snake_x = 45;
snake_y = 55;
snake_size = 10;
snake_vel = 5;
fps = 60;
clock = pygame.time.Clock();

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;
        if event.type == pygame.KEYUP:
            
            pass;
    screen.fill((255,255,255));
    pygame.draw.rect(screen,(255,0,0),(snake_x,snake_y,snake_size,snake_size));
    pygame.display.update();
    clock.tick(fps);
#     pygame.quit();
# quit();
# if __name__ == "__main__":
#     main();
