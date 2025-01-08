import pyautogui as pag

#
#    21ms best
#

def is_similar_color(color1, color2):
    
    return all(abs(c1 - c2) <= 10 for c1, c2 in zip(color1, color2))
    
if pag.confirm("Start the reaction test?") == 'OK':
    
    clicks_made = 0
    pag.click(605 + 35 // 2, 291 + 37 // 2)
    
    while clicks_made < 5:
        
        if is_similar_color(pag.pixel(605 + 35 // 2, 291 + 37 // 2), (75, 218, 107)):
            
            pag.click(605 + 35 // 2, 291 + 37 // 2)
            clicks_made += 1
            pag.click(605 + 35 // 2, 291 + 37 // 2)