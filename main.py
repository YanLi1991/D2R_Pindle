import io
import time
from datetime import datetime

import cv2
import numpy as np
import pyautogui
import pytesseract

hp_full = 1161
mana_full = 586

ice_armor_key = "A"
ice_spike_key = "X"
blizzard_key = "D"
tele_key = "C"

difficult = cv2.cvtColor(cv2.imread('elements/difficult.PNG'), cv2.COLOR_BGR2GRAY)
portal = cv2.cvtColor(cv2.imread('elements/portal.PNG'), cv2.COLOR_BGR2GRAY)
replay = cv2.cvtColor(cv2.imread('elements/replay.PNG'), cv2.COLOR_BGR2GRAY)
play_button = cv2.cvtColor(cv2.imread('elements/play_button.PNG'), cv2.COLOR_BGR2GRAY)
nightmare = cv2.cvtColor(cv2.imread('elements/nightmare.PNG'), cv2.COLOR_BGR2GRAY)
hellgame = cv2.cvtColor(cv2.imread('elements/hellgame.PNG'), cv2.COLOR_BGR2GRAY)
mf_diadem = cv2.cvtColor(cv2.imread('mf/diadem.png'), cv2.COLOR_BGR2GRAY)
mf_amulet = cv2.cvtColor(cv2.imread('mf/amulet.png'), cv2.COLOR_BGR2GRAY)
mf_shako = cv2.cvtColor(cv2.imread('mf/shako.PNG'), cv2.COLOR_BGR2GRAY)
mf_smallcharm = cv2.cvtColor(cv2.imread('mf/smallcharm.PNG'), cv2.COLOR_BGR2GRAY)
mf_grandcharm = cv2.cvtColor(cv2.imread('mf/grandcharm.PNG'), cv2.COLOR_BGR2GRAY)
mf_flawless = cv2.cvtColor(cv2.imread('mf/flawless.PNG'), cv2.COLOR_BGR2GRAY)
mf_perfect = cv2.cvtColor(cv2.imread('mf/perfect.PNG'), cv2.COLOR_BGR2GRAY)
mf_rune_bow = cv2.cvtColor(cv2.imread('mf/rune_bow.png'), cv2.COLOR_BGR2GRAY)
mf_rune_sword = cv2.cvtColor(cv2.imread('mf/rune_sword.png'), cv2.COLOR_BGR2GRAY)
mf_rune_scepter = cv2.cvtColor(cv2.imread('mf/rune_scepter.png'), cv2.COLOR_BGR2GRAY)
mf_rune_staff = cv2.cvtColor(cv2.imread('mf/rune_staff.png'), cv2.COLOR_BGR2GRAY)
mf_rune_talon = cv2.cvtColor(cv2.imread('mf/rune_talon.png'), cv2.COLOR_BGR2GRAY)
mf_rune = cv2.cvtColor(cv2.imread('mf/rune.png'), cv2.COLOR_BGR2GRAY)
mf_ring_mail = cv2.cvtColor(cv2.imread('mf/ring_mail.PNG'), cv2.COLOR_BGR2GRAY)
mf_ring = cv2.cvtColor(cv2.imread('mf/ring.png'), cv2.COLOR_BGR2GRAY)
mf_ring = cv2.cvtColor(cv2.imread('mf/ring.png'), cv2.COLOR_BGR2GRAY)
not_pindle_yet3 = cv2.cvtColor(cv2.imread('elements/not_pindle_yet3.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet2 = cv2.cvtColor(cv2.imread('elements/not_pindle_yet2.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet_again = cv2.cvtColor(cv2.imread('elements/not_pindle_yet_again.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet = cv2.cvtColor(cv2.imread('elements/not_pindle_yet.PNG'), cv2.COLOR_BGR2GRAY)
in_pindle_temple = cv2.cvtColor(cv2.imread('elements/in_temple.PNG'), cv2.COLOR_BGR2GRAY)
malah = cv2.cvtColor(cv2.imread('elements/malah.PNG'), cv2.COLOR_BGR2GRAY)
malah2 = cv2.cvtColor(cv2.imread('elements/malah2.PNG'), cv2.COLOR_BGR2GRAY)
malah3 = cv2.cvtColor(cv2.imread('elements/malah3.PNG'), cv2.COLOR_BGR2GRAY)
malah4 = cv2.cvtColor(cv2.imread('elements/malah4.PNG'), cv2.COLOR_BGR2GRAY)
malah5 = cv2.cvtColor(cv2.imread('elements/malah5.PNG'), cv2.COLOR_BGR2GRAY)
qualx1 = cv2.cvtColor(cv2.imread('elements/qualx1.PNG'), cv2.COLOR_BGR2GRAY)
qualx2 = cv2.cvtColor(cv2.imread('elements/qualx2.PNG'), cv2.COLOR_BGR2GRAY)
qualx3 = cv2.cvtColor(cv2.imread('elements/qualx3.PNG'), cv2.COLOR_BGR2GRAY)
qualx4 = cv2.cvtColor(cv2.imread('elements/qualx4.PNG'), cv2.COLOR_BGR2GRAY)
qualx5 = cv2.cvtColor(cv2.imread('elements/qualx5.PNG'), cv2.COLOR_BGR2GRAY)
qualx6 = cv2.cvtColor(cv2.imread('elements/qualx6.PNG'), cv2.COLOR_BGR2GRAY)
qualx7 = cv2.cvtColor(cv2.imread('elements/qualx7.PNG'), cv2.COLOR_BGR2GRAY)
qualx8 = cv2.cvtColor(cv2.imread('elements/qualx8.PNG'), cv2.COLOR_BGR2GRAY)
resurrect = cv2.cvtColor(cv2.imread('elements/resurrect.PNG'), cv2.COLOR_BGR2GRAY)
merc = cv2.cvtColor(cv2.imread('elements/merc.PNG'), cv2.COLOR_BGR2GRAY)
screen_width, screen_height = pyautogui.size()


def mimic_mouse_click(x, y, duration_in=0.2):
    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x, y, duration=duration_in)

    # Perform a left mouse button click
    pyautogui.click()


def mimic_mouse_hold(x, y, duration=2.0):
    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x, y, duration=0.1)

    # Perform a left mouse button click
    pyautogui.mouseDown()

    # Optional: Sleep for the specified duration to hold the click
    time.sleep(duration)

    # Release the mouse button
    pyautogui.mouseUp()


def take_screenshot(top_left_x=0, top_left_y=0, width=screen_width, height=screen_height):
    screenshot = pyautogui.screenshot(region=(int(top_left_x), int(top_left_y), int(width), int(height)))
    buffer = io.BytesIO()
    screenshot.save(buffer, format='PNG')
    return buffer


def convert_resolution(width=0, height=0):
    return width / 1920 * screen_width, height / 1080 * screen_height


def get_portal():
    mimic_mouse_hold(*convert_resolution(820, 700), 5.5)
    time.sleep(1)
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(portal, take_screenshot())
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(40, 60))])
    while loc_x != 0 and loc_y != 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(portal, take_screenshot())


def mimic_keyboard_press(key, duration=0.5):
    # Press the specified key
    pyautogui.press(key)

    # Optional: Sleep for the specified duration
    time.sleep(duration)


def start_game(template=nightmare):
    wait_time = 0.5
    select_game()
    enter_game(template)
    time.sleep(1)
    loc_x, loc_y = detect_template_bin(replay,
                                       take_screenshot(*convert_resolution(560, 300), *convert_resolution(600, 600)))
    while loc_x != 0 and loc_y != 0:
        time.sleep(10)
        mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(620, 325))])
        time.sleep(wait_time)
        enter_game()
        time.sleep(wait_time)
        loc_x, loc_y = detect_template_bin(replay, take_screenshot(*convert_resolution(560, 300),
                                                                   *convert_resolution(600, 600)))


def select_game(wait_time=1):
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(play_button, take_screenshot(*convert_resolution(560, 900),
                                                                        *convert_resolution(600, 200)))
    time.sleep(wait_time)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(640, 935))])
    time.sleep(wait_time)


def enter_game(template='nightmare.PNG', wait_time=1):
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(template, take_screenshot(*convert_resolution(560, 300),
                                                                     *convert_resolution(600, 600)))
    time.sleep(wait_time)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(620, 325))])
    time.sleep(wait_time)


def detect_template_bin(template, screenshot, threshold=0.85):
    img = cv2.cvtColor(cv2.imdecode(np.frombuffer(screenshot.getvalue(), np.uint8), cv2.IMREAD_COLOR),
                       cv2.COLOR_BGR2GRAY)

    # Match the template using cv2.matchTemplate
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    max_val = np.max(result)
    if len(locations[0]) == 0 or len(locations[1]) == 0:
        return 0, 0
    max_loc = (locations[1][0], locations[0][0])
    return max_loc


def detect_template(template_path, image_path, output_image_path, threshold=0.85):
    # Read the template and the image
    template = cv2.cvtColor(cv2.imread(template_path), cv2.COLOR_BGR2GRAY)
    img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2GRAY)
    # img = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2BGRA)

    # Match the template using cv2.matchTemplate
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    max_val = np.max(result)
    if len(locations[0]) == 0 or len(locations[1]) == 0:
        return 0, 0
    max_loc = (locations[1][0], locations[0][0])
    top_left = max_loc
    bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    cv2.imwrite(output_image_path, img)
    return max_loc


def farm():
    pyautogui.keyDown('alt')
    if not merc_died() and not need_heal(0.9):
        time.sleep(1.5)
    time.sleep(0.1)
    found = mfrune()
    found = mf(mf_diadem) or found
    found = mf(mf_amulet) or found
    found = mfring() or found
    found = mf(mf_shako) or found
    found = mf(mf_smallcharm) or found
    found = mf(mf_grandcharm) or found
    found = mf(mf_flawless) or found
    found = mf(mf_perfect) or found
    pyautogui.keyUp('alt')
    return found


def mfrune():
    loc_x, loc_y, try_count = 0, 0, 0
    found, check = False, False
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        buffer = take_screenshot(*convert_resolution(500, 0), *convert_resolution(1500, 600))
        loc_x2, loc_y2 = detect_template_bin(mf_rune_bow, buffer)
        loc_x3, loc_y3 = detect_template_bin(mf_rune_sword, buffer)
        loc_x4, loc_y4 = detect_template_bin(mf_rune_scepter, buffer)
        loc_x5, loc_y5 = detect_template_bin(mf_rune_staff, buffer)
        loc_x6, loc_y6 = detect_template_bin(mf_rune_talon, buffer)

        if loc_x2 == 0 and loc_y2 == 0 and loc_x3 == 0 and loc_y3 == 0 and loc_x4 == 0 and loc_y4 == 0 and loc_x5 == 0 and loc_y5 == 0 and loc_x6 == 0 and loc_y6 == 0:
            loc_x, loc_y = detect_template_bin(mf_rune, buffer)
            if loc_x != 0 or loc_y != 0:
                found = True
                mimic_mouse_hold(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(510, 5))])
                try_count += 1
            else:
                break
        check = True
    return found


def mfring():
    loc_x, loc_y, try_count = 0, 0, 0
    found, check = False, False
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        buffer = take_screenshot(*convert_resolution(500, 0), *convert_resolution(1500, 600))
        loc_x2, loc_y2 = detect_template_bin(mf_ring_mail, buffer)
        if loc_x2 == 0 and loc_y2 == 0:
            loc_x, loc_y = detect_template_bin(mf_ring, buffer)
            if loc_x != 0 or loc_y != 0:
                found = True
                mimic_mouse_hold(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(510, 5))])
                try_count += 1
            else:
                break
        check = True
    return found


def mf(template):
    loc_x, loc_y = 0, 0
    found, check = False, False
    try_count = 0
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        loc_x, loc_y = detect_template_bin(template,
                                           take_screenshot(*convert_resolution(500, 0), *convert_resolution(1500, 600)))
        if loc_x != 0 or loc_y != 0:
            found = True
            mimic_mouse_hold(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(510, 5))])
            try_count += 1
        else:
            break
        check = True
    return found


def wait_to_load():
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(difficult,
                                           take_screenshot(*convert_resolution(1700, 0), *convert_resolution(220, 60)))
        time.sleep(0.1)


def to_pindle(cd=0.3):
    mimic_keyboard_press(tele_key, duration=0.2)
    time.sleep(0.1)
    loc_x, loc_y = detect_template_bin(not_pindle_yet3,
                                       take_screenshot(*convert_resolution(800, 0), *convert_resolution(700, 300)))
    tele_count = 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(not_pindle_yet3,
                                           take_screenshot(*convert_resolution(800, 0), *convert_resolution(700, 300)))

    while loc_x != 0 or loc_y != 0:
        pyautogui.rightClick(*convert_resolution(1480, 100), duration=0.2)
        time.sleep(cd)
        tele_count += 1
        loc_x, loc_y = detect_template_bin(not_pindle_yet3,
                                           take_screenshot(*convert_resolution(800, 0), *convert_resolution(700, 300)))

    loc_x, loc_y = detect_template_bin(not_pindle_yet2,
                                       take_screenshot(*convert_resolution(800, 0), *convert_resolution(700, 300)))
    while loc_x != 0 or loc_y != 0:
        pyautogui.rightClick(*convert_resolution(1480, 130), duration=0.2)
        time.sleep(cd)
        tele_count += 1
        loc_x, loc_y = detect_template_bin(not_pindle_yet2,
                                           take_screenshot(*convert_resolution(800, 0), *convert_resolution(700, 300)))

    if tele_count < 3:
        pyautogui.rightClick(*convert_resolution(1485, 105), duration=0.3)
        time.sleep(cd)


def ice_gun(cd=0.3):
    count = 0
    with pyautogui.hold('shift'):
        pyautogui.rightClick(screen_width // 2, screen_height // 2, duration=0.1)
        while count < 8:
            pyautogui.leftClick(*convert_resolution(1450, 200), duration=0.1)
            time.sleep(cd)
            pyautogui.leftClick(*convert_resolution(1500, 250), duration=0.1)
            time.sleep(cd)
            count += 1
    print("shot done")


def in_temple():
    loc_x, loc_y = detect_template_bin(in_pindle_temple,
                                       take_screenshot(*convert_resolution(1000, 200), *convert_resolution(300, 300)))
    return loc_x != 0 and loc_y != 0


def fight():
    fight_rounds = 0
    while fight_rounds < 2 or (in_temple() and fight_rounds < 3):
        mimic_keyboard_press(ice_spike_key, duration=0.1)
        time.sleep(0.1)
        pyautogui.rightClick(*convert_resolution(1560, 200), duration=0.1)
        time.sleep(0.1)
        pyautogui.rightClick(*convert_resolution(1570, 250), duration=0.1)
        time.sleep(0.1)
        pyautogui.rightClick(*convert_resolution(1620, 250), duration=0.1)
        time.sleep(0.1)
        mimic_keyboard_press(blizzard_key, duration=0.2)
        time.sleep(0.1)
        pyautogui.rightClick(*convert_resolution(1420, 230), duration=0.3)
        time.sleep(0.3)
        fight_rounds += 1

    return False


def leave():
    pyautogui.press('esc')
    time.sleep(0.1)
    mimic_mouse_click(*convert_resolution(880, 470), 0.1)


def wait_to_leave():
    loc_x, loc_y = detect_template_bin(play_button,
                                       take_screenshot(*convert_resolution(560, 900), *convert_resolution(600, 200)))
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(play_button, take_screenshot(*convert_resolution(560, 900),
                                                                        *convert_resolution(600, 200)))


def put_to_chest():
    mimic_mouse_hold(*convert_resolution(800, 700), 2)
    time.sleep(1)
    mimic_mouse_click(*convert_resolution(1500, 570))
    time.sleep(1)
    mimic_mouse_click(*convert_resolution(550, 200))
    time.sleep(0.1)
    with pyautogui.hold('ctrl'):
        mimic_mouse_click(*convert_resolution(1740, 720))
        time.sleep(0.1)
        mimic_mouse_click(*convert_resolution(1740, 675))
        time.sleep(0.1)
        mimic_mouse_click(*convert_resolution(1740, 630))
        time.sleep(0.1)
        mimic_mouse_click(*convert_resolution(1740, 585))
        time.sleep(0.1)
        # mimic_mouse_click(*convert_resolution(1700, 720))
        # time.sleep(0.1)
        # mimic_mouse_click(*convert_resolution(1700, 675))
        # time.sleep(0.1)
        # mimic_mouse_click(*convert_resolution(1700, 630))
        # time.sleep(0.1)
        # mimic_mouse_click(*convert_resolution(1700, 585))
        # time.sleep(0.1)
    pyautogui.press('esc')
    mimic_mouse_click(*convert_resolution(900, 550))
    time.sleep(0.1)


def heal_malah():
    mimic_mouse_click(*convert_resolution(200, 400))
    time.sleep(1.5)
    loc_x = 0
    loc_y = 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        buffer = take_screenshot(*convert_resolution(560, 100), *convert_resolution(600, 600))
        loc_x, loc_y = detect_template_bin(malah2, buffer, 0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah, buffer, 0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah3, buffer, 0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah4, buffer, 0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah5, buffer, 0.8)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(570, 130))])
    time.sleep(1.5)
    pyautogui.press('esc')


def need_heal(threshold=0.8):
    buffer = take_screenshot(*convert_resolution(430, 863), *convert_resolution(55, 30))
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(cv2.imdecode(np.frombuffer(buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR),
                              cv2.COLOR_BGR2GRAY)

    # Apply any necessary preprocessing steps (e.g., resizing, thresholding)

    # Use Tesseract to perform OCR on the preprocessed image, specifying output as digits only
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    try:
        hp_left = int(pytesseract.image_to_string(gray_image, config=custom_config))
    except ValueError as e:
        hp_left = 1000

    if hp_left / hp_full < threshold:
        return True
    return False


def need_mana(threshold=0.8):
    buffer = take_screenshot(*convert_resolution(1430, 863), *convert_resolution(55, 30))
    # Convert the image to grayscale

    gray_image = cv2.cvtColor(cv2.imdecode(np.frombuffer(buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR),
                              cv2.COLOR_BGR2GRAY)

    # Apply any necessary preprocessing steps (e.g., resizing, thresholding)

    # Use Tesseract to perform OCR on the preprocessed image, specifying output as digits only
    custom_config = r'--oem 3 --psm 6 outputbase digits'
    try:
        mana_left = int(pytesseract.image_to_string(gray_image, config=custom_config))
    except ValueError as e:
        mana_left = 300

    if mana_left / mana_full < threshold:
        return True
    return False


def heal_back(level="nightmare.PNG", wait=6):
    heal_malah()
    leave()
    wait_to_leave()
    time.sleep(wait)
    start_game(level)
    wait_to_load()


def ice_armor():
    mimic_keyboard_press(ice_armor_key, duration=0.1)
    time.sleep(0.1)
    pyautogui.rightClick(920, 500, duration=0.1)
    time.sleep(0.1)


def revive_merc():
    mimic_mouse_click(*convert_resolution(0, 400))
    time.sleep(1.5)
    mimic_mouse_hold(*convert_resolution(700, 700), 2.5)
    time.sleep(1)
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        buffer = take_screenshot(*convert_resolution(260, 0), *convert_resolution(800, 800))
        loc_x, loc_y = detect_template_bin(qualx1, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx2, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx3, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx4, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx5, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx6, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx7, buffer, 0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx8, buffer, 0.6)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(280, 30))])
    time.sleep(1.5)
    loc_x, loc_y = detect_template_bin(resurrect,
                                       take_screenshot(*convert_resolution(500, 100), *convert_resolution(600, 600)),
                                       0.8)
    while loc_x == 0 and loc_y == 0:
        time.sleep(0.1)
        loc_x, loc_y = detect_template_bin(resurrect, take_screenshot(*convert_resolution(500, 100),
                                                                      *convert_resolution(600, 600)), 0.8)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(530, 105))])
    time.sleep(1.5)
    pyautogui.press('esc')
    time.sleep(0.5)


def merc_died():
    loc_x, loc_y = detect_template_bin(merc, take_screenshot(*convert_resolution(0, 0), *convert_resolution(600, 600)),
                                       0.8)
    if loc_x == 0 and loc_y == 0:
        return True
    return False


def merc_back(level, wait=6):
    revive_merc()
    leave()
    wait_to_leave()
    time.sleep(wait)
    start_game(level)
    wait_to_load()


def start():
    start_time = datetime.now()
    game_load_wait = 1
    hell = True
    level = nightmare
    if hell:
        level = hellgame
    try:
        counter = 0
        found_counter = 0
        success_counter = 0
        found = False
        while True:
            start_time_round = datetime.now()
            if found:
                start_game(level)
                wait_to_load()
                put_to_chest()
                leave()
                wait_to_leave()
                time.sleep(game_load_wait)
            start_game(level)
            wait_to_load()
            if merc_died():
                merc_back(level, game_load_wait)
            if need_mana(0.35) or need_heal():
                heal_back(level, game_load_wait)
            ice_armor()
            get_portal()
            wait_to_load()
            to_pindle(0.2)
            time.sleep(0.5)
            fight()
            found = farm()
            if found:
                found_counter += 1
            success_counter += 1
            leave()
            wait_to_leave()
            counter += 1
            end_time_round = datetime.now()
            print("found drop rounds: {}".format(found_counter))
            print("total rounds: {}".format(counter))
            print("round time: {}\n".format(end_time_round - start_time_round))
            time.sleep(game_load_wait)
    except KeyboardInterrupt:
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print('Loop interrupted')


if __name__ == "__main__":
    start()
