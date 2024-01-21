def startproc_mc():
    import subprocess
    pygame.init()
    pygame.display.set_caption("Windows Terminal")
    font = pygame.font.SysFont(None, 24)
    white = (255, 255, 255)
    black = (0, 0, 0)
    # Set up variables
    input_text = ""
    output_text = ""
    # Set up variables for scrolling
    scroll_offset = 0
    scroll_speed = 20  # Adjust the scroll speed as needed
    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    try:
                        input_text = "pip3 install pyopengl==3.1.5 pyglet==1.5.28 numpy==1.26.1 pygame==2.5.2"
                        output = subprocess.check_output(input_text, shell=True, stderr=subprocess.STDOUT)
                        output_text = output.decode("utf-8")
                        output_text = output_text + "\n"
                    except subprocess.CalledProcessError as e:
                        output_text = e.output.decode("utf-8")
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_UP:
                    scroll_offset += scroll_speed
                elif event.key == pygame.K_DOWN:
                    scroll_offset -= scroll_speed
                else:
                    input_text += event.unicode

        # Clear the screen
        screen.fill(black)
        # Draw the input and output text
        input_surface = font.render("press enter to run" + input_text, True, white)
        screen.blit(input_surface, (10, 10))
        #"press ESC to run minecraft 按ESC运行minecraft"
        input_surface = font.render("press ESC to run minecraft 按ESC运行minecraft" , True, white)
        # Split the output text by the newline character and display each line with scrolling
        output_lines = output_text.split("\n")
        y_position = 40 + scroll_offset
        for line in output_lines:
            output_surface = font.render(line, True, white)
            screen.blit(output_surface, (10, y_position))
            y_position += 20

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    user_defalt()
