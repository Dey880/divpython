import pyautogui as pag
import math
# 
# 134 ms best
# 
clicks = 30
found = False
target_color = (254, 254, 254)
tolerance = 10
x, y, width, height = 560, 190, 1000, 450
clicked_positions = []
radius = 8

def is_similar_color(color1, color2, tolerance=10):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))
    
def is_nearby(click_position, existing_positions, radius=8):
    return any(math.sqrt((click_position[0] - pos[0])**2 + (click_position[1] - pos[1])**2) <= radius for pos in existing_positions)
    
if pag.confirm("Start?") == 'OK':
    pag.click(970, 397)
    while clicks > 0:
        found = False
        screenshot = pag.screenshot(region=(x, y, width, height))
        
        for i in range(0, width, 15):
            if found == True:
                break
            for j in range(0, height, 15):
                pixel_color = screenshot.getpixel((i, j))
                if is_similar_color(pixel_color, target_color, tolerance):
                    click_position = (x + i, y + j)
                    if not is_nearby(click_position, clicked_positions, radius):
                        pag.click(*click_position)
                        clicked_positions.append(click_position)
                        clicks -= 1
                        found = True
                        break
        # if not found:
        #     button = pag.locateOnScreen('img.png', confidence=0.8, region=(x, y, width, height), grayscale=True)
        #     if button:
        #         pag.click(button)
        #         clicked_positions.append((button.left, button.top))
        #         clicks -= 1
        #         print(f"Fallback to image detection at: {button.left}, {button.top}, {clicks} clicks remaining.")
        #         time.sleep(0.05)