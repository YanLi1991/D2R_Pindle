import io
import multiprocessing
import os
import sys
import threading
import time
from multiprocessing import Queue

from PIL import Image
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from datetime import datetime

import cv2
import numpy as np
import pyautogui
import pytesseract

hp_full = 1283
mana_full = 481

fury = "D"
valkyrie = "Z"
# foh_key = "C"
# conviction_key = "A"
# tele_key = "C"

hell = True
counter = 0
mouse = MouseController()
keyboard = KeyboardController()

difficult = cv2.cvtColor(cv2.imread('elements/difficult.PNG'), cv2.COLOR_BGR2GRAY)
portal = cv2.cvtColor(cv2.imread('elements/portal.PNG'), cv2.COLOR_BGR2GRAY)
replay = cv2.cvtColor(cv2.imread('elements/replay.PNG'), cv2.COLOR_BGR2GRAY)
battlenet_play = cv2.cvtColor(cv2.imread('elements/play.PNG'), cv2.COLOR_BGR2GRAY)
play_button = cv2.cvtColor(cv2.imread('elements/play_button.PNG'), cv2.COLOR_BGR2GRAY)
nightmare = cv2.cvtColor(cv2.imread('elements/nightmare.PNG'), cv2.COLOR_BGR2GRAY)
hellgame = cv2.cvtColor(cv2.imread('elements/hellgame.PNG'), cv2.COLOR_BGR2GRAY)
unidentified = cv2.cvtColor(cv2.imread('elements/unidentified.PNG'), cv2.COLOR_BGR2GRAY)
empty = cv2.cvtColor(cv2.imread('elements/empty.PNG'), cv2.COLOR_BGR2GRAY)
stash = cv2.cvtColor(cv2.imread('elements/chest.PNG'), cv2.COLOR_BGR2GRAY)
inventory = cv2.cvtColor(cv2.imread('elements/inventory.PNG'), cv2.COLOR_BGR2GRAY)

mf_diadem = cv2.cvtColor(cv2.imread('mf/diadem.png'), cv2.COLOR_BGR2GRAY)
mf_coronet = cv2.cvtColor(cv2.imread('mf/coronet.PNG'), cv2.COLOR_BGR2BGRA)
mf_circlet = cv2.cvtColor(cv2.imread('mf/circlet.PNG'), cv2.COLOR_BGR2BGRA)
mf_tiara = cv2.cvtColor(cv2.imread('mf/tiara.PNG'), cv2.COLOR_BGR2BGRA)
mf_talrasha_armor = cv2.cvtColor(cv2.imread('mf/talrasha_armor.png'), cv2.COLOR_BGR2BGRA)
mf_diadem_unique = cv2.cvtColor(cv2.imread('mf/diadem.png'), cv2.COLOR_BGR2BGRA)
mf_monarch = cv2.cvtColor(cv2.imread('mf/monarch.PNG'), cv2.COLOR_BGR2GRAY)
mf_vortex = cv2.cvtColor(cv2.imread('mf/vortex.PNG'), cv2.COLOR_BGR2GRAY)
mf_monarch_magic = cv2.cvtColor(cv2.imread('mf/monarch_magic.PNG'), cv2.COLOR_BGR2BGRA)
mf_wand_unique = cv2.cvtColor(cv2.imread('mf/wand.PNG'), cv2.COLOR_BGR2BGRA)
mf_orb = cv2.cvtColor(cv2.imread('mf/orb.PNG'), cv2.COLOR_BGR2GRAY)
mf_orb_magic = cv2.cvtColor(cv2.imread('mf/orb_blue.PNG'), cv2.COLOR_BGR2BGRA)
mf_javelin = cv2.cvtColor(cv2.imread('mf/javelin.PNG'), cv2.COLOR_BGR2GRAY)
mf_javelin2 = cv2.cvtColor(cv2.imread('mf/javelin2.PNG'), cv2.COLOR_BGR2GRAY)
mf_javelin2_magic = cv2.cvtColor(cv2.imread('mf/javelin2.PNG'), cv2.COLOR_BGR2BGRA)
mf_amulet = cv2.cvtColor(cv2.imread('mf/amulet.png'), cv2.COLOR_BGR2GRAY)
mf_amulet_unique = cv2.cvtColor(cv2.imread('mf/amulet.png'), cv2.COLOR_BGR2BGRA)
mf_amulet_green = cv2.cvtColor(cv2.imread('mf/amulet_green.png'), cv2.COLOR_BGR2BGRA)
mf_jewel = cv2.cvtColor(cv2.imread('mf/jewel.PNG'), cv2.COLOR_BGR2GRAY)
mf_jewel_unique = cv2.cvtColor(cv2.imread('mf/jewel.PNG'), cv2.COLOR_BGR2BGRA)
mf_shako = cv2.cvtColor(cv2.imread('mf/shako.PNG'), cv2.COLOR_BGR2BGRA)
mf_dimentional_shard = cv2.cvtColor(cv2.imread('mf/dimentional_shard.PNG'), cv2.COLOR_BGR2BGRA)
mf_corona = cv2.cvtColor(cv2.imread('mf/corona.PNG'), cv2.COLOR_BGR2BGRA)
mf_smallcharm = cv2.cvtColor(cv2.imread('mf/smallcharm.PNG'), cv2.COLOR_BGR2GRAY)
mf_grandcharm = cv2.cvtColor(cv2.imread('mf/grandcharm.PNG'), cv2.COLOR_BGR2GRAY)
mf_flawless = cv2.cvtColor(cv2.imread('mf/flawless.PNG'), cv2.COLOR_BGR2GRAY)
mf_flawless_ame = cv2.cvtColor(cv2.imread('mf/flawless_ame.PNG'), cv2.COLOR_BGR2GRAY)
mf_flawless_topaz = cv2.cvtColor(cv2.imread('mf/flawless_topaz.PNG'), cv2.COLOR_BGR2GRAY)
mf_vampire = cv2.cvtColor(cv2.imread('mf/vampire.PNG'), cv2.COLOR_BGR2BGRA)
# mf_flawless = cv2.cvtColor(cv2.imread('mf/flaw.PNG'), cv2.COLOR_BGR2GRAY)
mf_boots = cv2.cvtColor(cv2.imread('mf/boots.PNG'), cv2.COLOR_BGR2GRAY)
mf_boots_unique = cv2.cvtColor(cv2.imread('mf/nboots.PNG'), cv2.COLOR_BGR2BGRA)
mf_greaves_unique = cv2.cvtColor(cv2.imread('mf/greaves.PNG'), cv2.COLOR_BGR2BGRA)
mf_mitts_rare = cv2.cvtColor(cv2.imread('mf/mitts.PNG'), cv2.COLOR_BGR2BGRA)
mf_gloves_rare = cv2.cvtColor(cv2.imread('mf/gloves.PNG'), cv2.COLOR_BGR2BGRA)
mf_gauntlets_rare = cv2.cvtColor(cv2.imread('mf/gauntlets.PNG'), cv2.COLOR_BGR2BGRA)
mf_perfect = cv2.cvtColor(cv2.imread('mf/perfect.PNG'), cv2.COLOR_BGR2GRAY)
mf_perfect_ame = cv2.cvtColor(cv2.imread('mf/perfect_ame.PNG'), cv2.COLOR_BGR2GRAY)
mf_rune_bow = cv2.cvtColor(cv2.imread('mf/rune_bow.png'), cv2.COLOR_BGR2GRAY)
mf_rune_sword = cv2.cvtColor(cv2.imread('mf/rune_sword.png'), cv2.COLOR_BGR2GRAY)
mf_rune_scepter = cv2.cvtColor(cv2.imread('mf/rune_scepter.png'), cv2.COLOR_BGR2GRAY)
mf_rune_staff = cv2.cvtColor(cv2.imread('mf/rune_staff.png'), cv2.COLOR_BGR2GRAY)
mf_rune_talon = cv2.cvtColor(cv2.imread('mf/rune_talon.png'), cv2.COLOR_BGR2GRAY)
mf_rune = cv2.cvtColor(cv2.imread('mf/rune.png'), cv2.COLOR_BGR2GRAY)
mf_ring_mail = cv2.cvtColor(cv2.imread('mf/ring_mail.PNG'), cv2.COLOR_BGR2GRAY)
mf_ring = cv2.cvtColor(cv2.imread('mf/ring.png'), cv2.COLOR_BGR2GRAY)
mf_ring_unique = cv2.cvtColor(cv2.imread('mf/ring.png'), cv2.COLOR_BGR2BGRA)
not_pindle_yet3 = cv2.cvtColor(cv2.imread('elements/not_pindle_yet3.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet2 = cv2.cvtColor(cv2.imread('elements/not_pindle_yet2.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet_again = cv2.cvtColor(cv2.imread('elements/not_pindle_yet_again.PNG'), cv2.COLOR_BGR2GRAY)
not_pindle_yet = cv2.cvtColor(cv2.imread('elements/not_pindle_yet.PNG'), cv2.COLOR_BGR2GRAY)
in_pindle_temple = cv2.cvtColor(cv2.imread('elements/in_temple.PNG'), cv2.COLOR_BGR2GRAY)
mf_glove = cv2.cvtColor(cv2.imread('mf/mfglove.PNG'), cv2.COLOR_BGR2BGRA)
mf_belt = cv2.cvtColor(cv2.imread('mf/mfbelt.PNG'), cv2.COLOR_BGR2BGRA)
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
merc_archer = cv2.cvtColor(cv2.imread('elements/merc_archer.PNG'), cv2.COLOR_BGR2GRAY)
merc_aura = cv2.cvtColor(cv2.imread('elements/merc_aura.PNG'), cv2.COLOR_BGR2GRAY)
hp_check = cv2.cvtColor(cv2.imread('elements/hp_check.PNG'), cv2.COLOR_BGR2GRAY)
hp_merc_check = cv2.cvtColor(cv2.imread('elements/merc_aura_danger.PNG'), cv2.COLOR_BGR2GRAY)
valkyrie_check = cv2.cvtColor(cv2.imread('elements/valkyrie.PNG'), cv2.COLOR_BGR2GRAY)
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
    pyautogui.sleep(duration)

    # Release the mouse button
    pyautogui.mouseUp()


def take_screenshot(top_left_x=0, top_left_y=0, width=screen_width, height=screen_height):
    screenshot = None
    while screenshot is None:
        try:
            screenshot = pyautogui.screenshot(region=(int(top_left_x), int(top_left_y), int(width), int(height)))
        except OSError:
            continue

    buffer = io.BytesIO()
    screenshot.save(buffer, format='PNG')
    return buffer


def convert_resolution(width=0, height=0):
    return width / 1920 * screen_width, height / 1080 * screen_height


def find_portal():
    retry, loc_x, loc_y = 0, 0, 0
    while loc_x == 0 and loc_y == 0 and retry <= 10:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(portal, take_screenshot())
        retry += 1
    return loc_x, loc_y


def get_portal():
    # mimic_mouse_hold(*convert_resolution(820, 700), 5.5)
    mimic_mouse_hold(*convert_resolution(820, 700), 4.5)
    pyautogui.sleep(1)
    loc_x, loc_y = find_portal()
    while loc_x == 0 and loc_y == 0:
        mimic_mouse_hold(*convert_resolution(820, 700), 0.5)
        loc_x, loc_y = find_portal()
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(40, 60))])
    while loc_x != 0 and loc_y != 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(portal, take_screenshot())


def mimic_keyboard_press(key, duration=0.5):
    # Press the specified key
    pyautogui.press(key)

    # Optional: Sleep for the specified duration
    pyautogui.sleep(duration)


def start_game(template=nightmare):
    wait_time = 0.5
    select_game()
    enter_game(template)
    pyautogui.sleep(1)
    # loc_x, loc_y = detect_template_bin(replay,
    #                                    take_screenshot(*convert_resolution(560, 300), *convert_resolution(600, 600)))

    loc_x, loc_y, loc_x2, loc_y2 = 0, 0, 0, 0
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(difficult,
                                           take_screenshot(*convert_resolution(1700, 0),
                                                           *convert_resolution(220, 60)))
        loc_x2, loc_y2 = detect_template_bin(replay, take_screenshot(*convert_resolution(560, 300),
                                                                     *convert_resolution(600, 600)))
        pyautogui.sleep(0.1)
        if loc_x2 != 0 and loc_y2 != 0:
            mimic_mouse_click(*[x + y for x, y in zip((loc_x2, loc_y2), convert_resolution(620, 325))])
            pyautogui.sleep(wait_time)
            enter_game(template)

    # while loc_x != 0 and loc_y != 0:
    #     pyautogui.sleep(10)
    #     mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(620, 325))])
    #     pyautogui.sleep(wait_time)
    #     enter_game(template)
    #     pyautogui.sleep(wait_time)
    #     loc_x, loc_y = detect_template_bin(replay, take_screenshot(*convert_resolution(560, 300),
    #                                                                *convert_resolution(600, 600)))


def select_game(wait_time=1):
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(play_button, take_screenshot(*convert_resolution(560, 900),
                                                                        *convert_resolution(600, 200)))
    pyautogui.sleep(wait_time)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(640, 935))])
    pyautogui.sleep(wait_time)


def enter_game(template=nightmare, wait_time=1):
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(template, take_screenshot(*convert_resolution(560, 300),
                                                                     *convert_resolution(600, 600)))
    pyautogui.sleep(wait_time)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(620, 325))])
    pyautogui.sleep(wait_time)


def detect_template_bin(template, screenshot, color_format=cv2.COLOR_BGR2GRAY, threshold=0.85):
    img = cv2.cvtColor(cv2.imdecode(np.frombuffer(screenshot.getvalue(), np.uint8), cv2.IMREAD_COLOR),
                       color_format)

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


def mf_screenshot():
    return take_screenshot(*convert_resolution(500, 0), *convert_resolution(1500, 600))


def farm():
    pyautogui.keyDown('alt')
    if not merc_died() and not need_heal(0.9):
        pyautogui.sleep(1.5)
    pyautogui.sleep(0.1)
    screenshot = mf_screenshot()
    boolean_array = []
    # found = mf(mf_jewel, screenshot)
    found1 = mf(mf_flawless_ame, screenshot)
    screenshot = mf_screenshot() if found1 else screenshot
    boolean_array.append(found1)

    found2 = mf(mf_perfect_ame, screenshot)
    screenshot = mf_screenshot() if found2 else screenshot
    boolean_array.append(found2)

    found3 = mf(mf_jewel_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found3 else screenshot
    boolean_array.append(found3)

    found4 = mfrune(screenshot)
    screenshot = mf_screenshot() if found4 else screenshot
    boolean_array.append(found4)

    found5 = mfring(screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found5 else screenshot
    boolean_array.append(found5)

    found6 = mf(mf_smallcharm, screenshot)
    screenshot = mf_screenshot() if found6 else screenshot
    boolean_array.append(found6)

    found7 = mf(mf_grandcharm, screenshot)
    screenshot = mf_screenshot() if found7 else screenshot
    boolean_array.append(found7)

    found8 = mf(mf_monarch_magic, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found8 else screenshot
    boolean_array.append(found8)

    found9 = mf(mf_amulet_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found9 else screenshot
    boolean_array.append(found9)

    found31 = mf(mf_amulet_green, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found31 else screenshot
    boolean_array.append(found31)

    found10 = mf(mf_vampire, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found10 else screenshot
    boolean_array.append(found10)

    found11 = mf(mf_glove, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found11 else screenshot
    boolean_array.append(found11)

    # found12 = mf(mf_belt, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    # screenshot = mf_screenshot() if found12 else screenshot
    # boolean_array.append(found12)

    found13 = mf(mf_boots_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found13 else screenshot
    boolean_array.append(found13)

    found14 = mf(mf_greaves_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found14 else screenshot
    boolean_array.append(found14)

    found15 = mf(mf_mitts_rare, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found15 else screenshot
    boolean_array.append(found15)

    found16 = mf(mf_gloves_rare, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found16 else screenshot
    boolean_array.append(found16)

    found17 = mf(mf_gauntlets_rare, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found17 else screenshot
    boolean_array.append(found17)

    found18 = mf(mf_orb_magic, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found18 else screenshot
    boolean_array.append(found18)

    found19 = mf(mf_javelin, screenshot)
    screenshot = mf_screenshot() if found19 else screenshot
    boolean_array.append(found19)

    # found20 = mf(mf_vortex, screenshot)
    # screenshot = mf_screenshot() if found20 else screenshot
    # boolean_array.append(found20)

    found21 = mf(mf_javelin2_magic, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found21 else screenshot
    boolean_array.append(found21)

    found22 = mf(mf_shako, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found22 else screenshot
    boolean_array.append(found22)

    found23 = mf(mf_wand_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found23 else screenshot
    boolean_array.append(found23)

    found25 = mf(mf_talrasha_armor, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found25 else screenshot
    boolean_array.append(found25)

    found26 = mf(mf_coronet, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found26 else screenshot
    boolean_array.append(found26)

    found27 = mf(mf_circlet, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found27 else screenshot
    boolean_array.append(found27)

    # found28 = mf(mf_dimentional_shard, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    # screenshot = mf_screenshot() if found28 else screenshot
    # boolean_array.append(found28)
    #
    # found29 = mf(mf_corona, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    # screenshot = mf_screenshot() if found29 else screenshot
    # boolean_array.append(found29)

    found30 = mf(mf_tiara, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    screenshot = mf_screenshot() if found30 else screenshot
    boolean_array.append(found30)

    found24 = mf(mf_diadem_unique, screenshot, color_format=cv2.COLOR_BGR2BGRA)
    boolean_array.append(found24)

    pyautogui.keyUp('alt')
    return any(boolean_array)


def mfrune(screenshot):
    loc_x, loc_y, try_count = 0, 0, 0
    found, check = False, False
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        buffer = screenshot if not check else take_screenshot(*convert_resolution(500, 0),
                                                              *convert_resolution(1500, 600))
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


def mfring(screenshot, color_format=cv2.COLOR_BGR2GRAY):
    loc_x, loc_y, try_count = 0, 0, 0
    found, check = False, False
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        buffer = screenshot if not check else take_screenshot(*convert_resolution(500, 0),
                                                              *convert_resolution(1500, 600))
        loc_x2, loc_y2 = detect_template_bin(mf_ring_mail, buffer)
        if loc_x2 == 0 and loc_y2 == 0:
            loc_x, loc_y = detect_template_bin(mf_ring if color_format == cv2.COLOR_BGR2GRAY else mf_ring_unique,
                                               buffer, color_format)
            if loc_x != 0 or loc_y != 0:
                found = True
                mimic_mouse_hold(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(510, 5))])
                try_count += 1
            else:
                break
        check = True
    return found


def mf(template, screenshot, color_format=cv2.COLOR_BGR2GRAY):
    loc_x, loc_y = 0, 0
    found, check = False, False
    try_count = 0
    while (not check or loc_x != 0 or loc_y != 0) and try_count < 3:
        loc_x, loc_y = detect_template_bin(template,
                                           screenshot if not check else take_screenshot(*convert_resolution(500, 0),
                                                                                        *convert_resolution(1500, 600)),
                                           color_format)
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
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(difficult,
                                           take_screenshot(*convert_resolution(1700, 0), *convert_resolution(220, 60)))
        pyautogui.sleep(0.1)
    pyautogui.sleep(0.1)


def to_pindle(cd=0.3):
    # mimic_keyboard_press(tele_key, duration=0.2)
    # pyautogui.sleep(0.1)
    # pyautogui.rightClick(*convert_resolution(1480, 100), duration=0.2)
    # pyautogui.sleep(0.3 if cd < 0.3 else cd)
    # pyautogui.rightClick(*convert_resolution(1480, 130), duration=0.2)
    # pyautogui.sleep(0.3 if cd < 0.3 else cd)
    # pyautogui.rightClick(*convert_resolution(1485, 105), duration=0.2)
    # pyautogui.sleep(cd)
    pyautogui.sleep(0.1)
    mimic_mouse_hold(*convert_resolution(1000, 350), 2)
    pyautogui.sleep(0.1)
    mimic_mouse_hold(*convert_resolution(1500, 350), 1.6)


def ice_gun(cd=0.3):
    count = 0
    with pyautogui.hold('shift'):
        pyautogui.rightClick(screen_width // 2, screen_height // 2, duration=0.1)
        while count < 8:
            pyautogui.leftClick(*convert_resolution(1450, 200), duration=0.1)
            pyautogui.sleep(cd)
            pyautogui.leftClick(*convert_resolution(1500, 250), duration=0.1)
            pyautogui.sleep(cd)
            count += 1
    print("shot done")


def in_temple():
    loc_x, loc_y = detect_template_bin(in_pindle_temple,
                                       take_screenshot(*convert_resolution(1000, 200), *convert_resolution(300, 300)))
    return loc_x != 0 and loc_y != 0


def click(x, y, mouse_click=Button.left, duration=0.05):
    # Move mouse to position
    mouse.position = (x, y)
    time.sleep(duration)

    # Immediately perform a click
    mouse.click(mouse_click)


def valkyrie_died():
    count = 0
    while count < 4:
        buffer = take_screenshot(*convert_resolution(0, 0), *convert_resolution(300, 100))

        # # Rewind the buffer to the beginning before reading
        # buffer.seek(0)
        #
        # # Load the image from the BytesIO buffer
        # img = Image.open(buffer)
        #
        # # Save the image to disk
        # img.save(f"screenshot_{count}.png")

        loc_x, loc_y = detect_template_bin(valkyrie_check, buffer, threshold=0.9)
        if loc_x != 0 and loc_y != 0:
            return False
        count += 1
    return True


def fight():
    # pyautogui.sleep(0.1)
    click(*convert_resolution(1270, 380), mouse_click=Button.right, duration=0.2)
    mimic_keyboard_press(fury, duration=0.1)
    fight_rounds = 0
    while fight_rounds < 10:
        click(*convert_resolution(1370, 360), mouse_click=Button.right, duration=0.2)
        if valkyrie_died():
            mimic_keyboard_press(valkyrie, duration=0.1)
            # pyautogui.sleep(0.1)
            click(*convert_resolution(1270, 380), mouse_click=Button.right, duration=0.2)
            mimic_keyboard_press(fury, duration=0.1)

        fight_rounds += 1

    # mimic_keyboard_press(fury, duration=0.1)
    # # print(fight_rounds * 5 + 1)
    # # pyautogui.sleep(0.1)
    # click(*convert_resolution(1590, 250), mouse_click=Button.right, duration=0.2)
    #
    # mimic_keyboard_press(valkyrie, duration=0.1)
    # # pyautogui.sleep(0.1)
    # click(*convert_resolution(1570, 250), mouse_click=Button.right, duration=0.2)
    #
    # mimic_keyboard_press(fury, duration=0.1)
    # # print(fight_rounds * 5 + 2)
    # # pyautogui.rightClick(*convert_resolution(1590, 250), duration=0.1)
    # # pyautogui.sleep(0.1)
    # click(*convert_resolution(1620, 250), mouse_click=Button.right, duration=0.2)
    # print(fight_rounds * 5 + 3)
    # pyautogui.rightClick(*convert_resolution(1620, 250), duration=0.1)
    # pyautogui.sleep(0.1)
    # click(*convert_resolution(1605, 250), mouse_click=Button.right, duration=0.2)
    # # print(fight_rounds * 5 + 4)
    # # pyautogui.rightClick(*convert_resolution(1605, 250), duration=0.1)
    # # pyautogui.sleep(0.1)
    # click(*convert_resolution(1605, 250), mouse_click=Button.right, duration=0.2)
    # print(fight_rounds * 5 + 5)
    # pyautogui.rightClick(*convert_resolution(1605, 250), duration=0.1)
    # pyautogui.sleep(0.1)
    # mimic_keyboard_press(foh_key, duration=0.1)
    # pyautogui.sleep(0.1)
    # pyautogui.rightClick(*convert_resolution(1420, 230), duration=0.1)
    # pyautogui.rightClick(*convert_resolution(1420, 230), duration=0.1)
    # pyautogui.sleep(0.4)
    # mimic_keyboard_press(conviction_key, duration=0.1)
    # pyautogui.sleep(0.1)
    # keyboard.press(Key.shift)
    # # mouse.position = (screen_width / 2 + 250, screen_height / 2 - 200)
    # mouse.position = (screen_width / 2 + 100, screen_height / 2 - 50)
    # mouse.press(Button.left)
    #
    # # Hold both for 4 seconds
    # # time.sleep(4)
    # time.sleep(1)
    #
    # # Release both
    # mouse.release(Button.left)
    # click(*convert_resolution(screen_width / 2 + 100, screen_height / 2 - 50), mouse_click=Button.left,
    #       duration=0.1)
    # keyboard.release(Key.shift)
    # time.sleep(0.1)
    # fight_rounds += 1
    # mimic_keyboard_press(holy_key, duration=0.1)
    # pyautogui.sleep(0.1)
    # pyautogui.rightClick(*convert_resolution(1590, 250), duration=0.1)
    # pyautogui.sleep(0.2)
    # pyautogui.rightClick(*convert_resolution(1620, 250), duration=0.1)
    # pyautogui.sleep(0.2)
    # pyautogui.rightClick(*convert_resolution(1605, 250), duration=0.1)
    # mimic_keyboard_press(conviction_key, duration=0.1)
    # pyautogui.sleep(0.1)

    # foh_rounds = 0
    # while foh_rounds < 5:
    #     keyboard.press(Key.shift)
    #     # # mouse.position = (screen_width / 2 + 250, screen_height / 2 - 200)
    #     # mouse.position = (screen_width / 2 + 100, screen_height / 2 - 50)
    #     # mouse.press(Button.left)
    #     #
    #     # # Hold both for 4 seconds
    #     # # time.sleep(4)
    #     # time.sleep(1)
    #     #
    #     # # Release both
    #     # mouse.release(Button.left)
    #     click(*convert_resolution(screen_width / 2 + 100, screen_height / 2 - 50), mouse_click=Button.left, duration=0.1)
    #     keyboard.release(Key.shift)
    #     time.sleep(0.2)
    #     foh_rounds += 1
    # print("done")

    # pyautogui.keyDown('shift')
    # # Press and hold right mouse button
    # # pyautogui.mouseDown(*convert_resolution(screen_width / 2 + 300, screen_height / 2 - 300), button='right')
    # pyautogui.mouseDown(*convert_resolution(screen_width / 2 + 300, screen_height / 2 - 300), button='left')
    #
    # # Hold for 4 seconds
    # time.sleep(3)
    #
    # # Release the right mouse button
    # # pyautogui.mouseUp(*convert_resolution(screen_width / 2 + 300, screen_height / 2 - 300), button='right')
    # pyautogui.mouseUp(*convert_resolution(screen_width / 2 + 300, screen_height / 2 - 300), button='left')
    # pyautogui.keyUp('shift')
    # pyautogui.rightClick(*convert_resolution(1420, 230), duration=4)

    return False


def leave():
    pyautogui.keyUp('alt')
    pyautogui.sleep(0.1)
    pyautogui.press('esc')
    pyautogui.sleep(0.1)
    mimic_mouse_click(*convert_resolution(880, 470), 0.1)


def wait_to_leave():
    loc_x, loc_y = detect_template_bin(play_button,
                                       take_screenshot(*convert_resolution(560, 900), *convert_resolution(600, 200)))
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(play_button, take_screenshot(*convert_resolution(560, 900),
                                                                        *convert_resolution(600, 200)))


def check_then_put(x, y, duration_in=0.2):
    pyautogui.moveTo(x, y, duration_in)
    pyautogui.sleep(0.1)
    loc_x, loc_y = detect_template_bin(unidentified,
                                       take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                       cv2.COLOR_BGR2GRAY)
    loc_x2, loc_y2 = detect_template_bin(mf_rune,
                                         take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                         cv2.COLOR_BGR2GRAY)
    loc_x3, loc_y3 = detect_template_bin(mf_flawless,
                                         take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                         cv2.COLOR_BGR2GRAY)
    if (loc_x != 0 and loc_y != 0) or (loc_x2 != 0 and loc_y2 != 0) or (loc_x3 != 0 and loc_y3 != 0):
        with pyautogui.hold('ctrl'):
            mimic_mouse_click(*convert_resolution(x, y))
            pyautogui.sleep(0.1)


def dump_gear(x, y, duration_in=0.2):
    pyautogui.moveTo(x, y, duration_in)
    pyautogui.sleep(0.1)
    loc_x, loc_y = detect_template_bin(unidentified,
                                       take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                       cv2.COLOR_BGR2GRAY)
    loc_x2, loc_y2 = detect_template_bin(mf_rune,
                                         take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                         cv2.COLOR_BGR2GRAY)
    loc_x3, loc_y3 = detect_template_bin(mf_flawless,
                                         take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                         cv2.COLOR_BGR2GRAY)
    if loc_x == 0 and loc_y == 0 and loc_x2 == 0 and loc_y2 == 0 and loc_x3 == 0 and loc_y3 == 0:
        with pyautogui.hold('ctrl'):
            mimic_mouse_click(*convert_resolution(x, y))
            pyautogui.sleep(0.1)


def put_into_chest():
    loc_x, loc_y = detect_template_bin(inventory,
                                       take_screenshot(*convert_resolution(960, 0),
                                                       *convert_resolution(960, 300)),
                                       cv2.COLOR_BGR2GRAY)
    if loc_x != 0 and loc_y != 0:

        if not_empty():
            check_then_put(1740, 720)
        if not_empty():
            check_then_put(1700, 585)
        if not_empty():
            check_then_put(1700, 720)
        if not_empty():
            check_then_put(1740, 585)
        if not_empty():
            check_then_put(1740, 675)
        if not_empty():
            check_then_put(1740, 630)
        if not_empty():
            check_then_put(1700, 675)
        if not_empty():
            check_then_put(1700, 630)

        pyautogui.press('esc')
        return True
    return False
    # mimic_mouse_click(*convert_resolution(900, 550))


def not_empty():
    loc_x, loc_y = detect_template_bin(empty,
                                       take_screenshot(*convert_resolution(1280, 300), *convert_resolution(640, 720)),
                                       cv2.COLOR_BGR2GRAY)
    return loc_x == 0 and loc_y == 0


def dump_garbage():
    mimic_keyboard_press("I", duration=0.1)
    if not_empty():
        dump_gear(1740, 720)
    if not_empty():
        dump_gear(1700, 585)
    if not_empty():
        dump_gear(1700, 720)
    if not_empty():
        dump_gear(1740, 585)
    if not_empty():
        dump_gear(1740, 675)
    if not_empty():
        dump_gear(1740, 630)
    if not_empty():
        dump_gear(1700, 675)
    if not_empty():
        dump_gear(1700, 630)

    pyautogui.press('esc')


def find_stash():
    stash_counter, loc_x, loc_y = 0, 0, 0
    while stash_counter < 3:
        loc_x, loc_y = detect_template_bin(stash,
                                           take_screenshot(*convert_resolution(1280, 300),
                                                           *convert_resolution(640, 300)),
                                           cv2.COLOR_BGR2GRAY)
        if loc_x != 0 and loc_y != 0:
            return 1280 + loc_x, 300 + loc_y
        stash_counter += 1
    return 1580, 570


def put_to_chest(count):
    mimic_mouse_hold(*convert_resolution(800, 700), 2)
    # mimic_mouse_hold(*convert_resolution(800, 700), 1.5)
    pyautogui.sleep(1)

    mimic_mouse_click(*convert_resolution(*find_stash()))

    pyautogui.sleep(1)
    chest = convert_resolution(550, 200)
    if count % 3 == 1:
        chest = convert_resolution(400, 200)
    elif count % 3 == 2:
        chest = convert_resolution(500, 200)
    mimic_mouse_click(*chest)
    pyautogui.sleep(0.1)
    stashed = put_into_chest()
    if stashed:
        dump_garbage()
        return False
    return True
    # with pyautogui.hold('ctrl'):
    #     mimic_mouse_click(*convert_resolution(1740, 720))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1740, 675))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1740, 630))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1740, 585))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1700, 720))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1700, 675))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1700, 630))
    #     pyautogui.sleep(0.1)
    #     mimic_mouse_click(*convert_resolution(1700, 585))
    #     pyautogui.sleep(0.1)
    # pyautogui.press('esc')
    # mimic_mouse_click(*convert_resolution(900, 350))
    # pyautogui.sleep(0.1)


def heal_malah():
    mimic_mouse_click(*convert_resolution(200, 400))
    pyautogui.sleep(1.5)
    loc_x = 0
    loc_y = 0
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        buffer = take_screenshot(*convert_resolution(560, 100), *convert_resolution(600, 600))
        loc_x, loc_y = detect_template_bin(malah2, buffer, threshold=0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah, buffer, threshold=0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah3, buffer, threshold=0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah4, buffer, threshold=0.8)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(malah5, buffer, threshold=0.8)
        if not (need_heal() or need_mana(0.25)):
            return
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(570, 130))])
    pyautogui.sleep(1.5)
    pyautogui.press('esc')


def need_heal(threshold=0.8):
    # return danger_may_need_heal()

    count = 0
    while count < 4:
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
            hp_left = 100

        if hp_left / hp_full < threshold:
            return True
        count += 1
    return False


def danger_merc():
    count = 0
    while count < 4:
        buffer = take_screenshot(*convert_resolution(0, 0), *convert_resolution(100, 100))

        # # Rewind the buffer to the beginning before reading
        # buffer.seek(0)
        #
        # # Load the image from the BytesIO buffer
        # img = Image.open(buffer)
        #
        # # Save the image to disk
        # img.save(f"screenshot_{count}.png")

        loc_x, loc_y = detect_template_bin(hp_merc_check, buffer, threshold=0.9)
        if loc_x != 0 and loc_y != 0:
            return False
        count += 1
    return True


def danger_may_need_heal():
    count = 0
    while count < 4:
        buffer = take_screenshot(*convert_resolution(320, 800), *convert_resolution(360, 280))

        # # Rewind the buffer to the beginning before reading
        # buffer.seek(0)
        #
        # # Load the image from the BytesIO buffer
        # img = Image.open(buffer)
        #
        # # Save the image to disk
        # img.save(f"screenshot_{count}.png")

        loc_x, loc_y = detect_template_bin(hp_check, buffer, threshold=0.9)
        if loc_x != 0 and loc_y != 0:
            return False
        count += 1
    return True


def danger_need_heal(threshold=0.8):
    count = 0
    danger_count = 0
    while count < 6:
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
            hp_left = 100

        if hp_left / hp_full < threshold:
            danger_count += 1
            # print(hp_left)
            if danger_count >= 3:
                return True
        count += 1
    return False


def need_mana(threshold=0.8):
    return False

    # count = 0
    # prev_mana = 0
    # while count < 4:
    #     buffer = take_screenshot(*convert_resolution(1430, 863), *convert_resolution(55, 30))
    #     # Convert the image to grayscale
    #
    #     gray_image = cv2.cvtColor(cv2.imdecode(np.frombuffer(buffer.getvalue(), np.uint8), cv2.IMREAD_COLOR),
    #                               cv2.COLOR_BGR2GRAY)
    #
    #     # Apply any necessary preprocessing steps (e.g., resizing, thresholding)
    #
    #     # Use Tesseract to perform OCR on the preprocessed image, specifying output as digits only
    #     custom_config = r'--oem 3 --psm 6 outputbase digits'
    #     try:
    #         mana_left = int(pytesseract.image_to_string(gray_image, config=custom_config))
    #     except ValueError as e:
    #         mana_left = 100
    #
    #     if mana_left / mana_full < threshold:
    #         print(mana_left)
    #         return True
    #     count += 1
    # return False


def heal_back(level=nightmare, wait=6):
    heal_malah()
    leave()
    wait_to_leave()
    pyautogui.sleep(wait)
    start_game(level)
    wait_to_load()


# def ice_armor():
#     mimic_keyboard_press(shield_key, duration=0.1)
#     pyautogui.sleep(0.1)
#     pyautogui.rightClick(920, 500, duration=0.1)
#     pyautogui.sleep(0.1)


def revive_merc():
    mimic_mouse_click(*convert_resolution(0, 400))
    pyautogui.sleep(1.5)
    mimic_mouse_hold(*convert_resolution(700, 700), 2.5)
    pyautogui.sleep(1)
    loc_x, loc_y = 0, 0
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        buffer = take_screenshot(*convert_resolution(260, 0), *convert_resolution(800, 800))
        loc_x, loc_y = detect_template_bin(qualx1, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx2, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx3, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx4, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx5, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx6, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx7, buffer, threshold=0.6)
        if loc_x == 0 and loc_y == 0:
            loc_x, loc_y = detect_template_bin(qualx8, buffer, threshold=0.6)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(280, 30))])
    pyautogui.sleep(1.5)
    loc_x, loc_y = detect_template_bin(resurrect,
                                       take_screenshot(*convert_resolution(500, 100), *convert_resolution(600, 600)),
                                       threshold=0.8)
    while loc_x == 0 and loc_y == 0:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(resurrect, take_screenshot(*convert_resolution(500, 100),
                                                                      *convert_resolution(600, 600)), threshold=0.8)
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(530, 105))])
    pyautogui.sleep(1.5)
    pyautogui.press('esc')
    pyautogui.sleep(0.5)


def merc_died():
    loc_x, loc_y = detect_template_bin(merc_aura,
                                       take_screenshot(*convert_resolution(0, 0), *convert_resolution(600, 600)),
                                       threshold=0.8)
    if loc_x == 0 and loc_y == 0:
        return True
    return False


def merc_back(level, wait=6):
    revive_merc()
    leave()
    wait_to_leave()
    pyautogui.sleep(wait)
    start_game(level)
    wait_to_load()


def fight_farm(result_queue: Queue):
    fight()
    result_queue.put(farm())


def start(update_time):
    # while not restart_event.is_set():
    global counter
    start_time = datetime.now()
    game_load_wait = 1
    level = nightmare
    if hell:
        level = hellgame
    try:

        found_counter = 0
        success_counter = 0
        found = False
        while True:
            keyboard.release(Key.shift)
            pyautogui.keyUp('alt')
            start_time_round = datetime.now()
            while found:
                start_game(level)
                wait_to_load()
                found = put_to_chest(found_counter)
                leave()
                wait_to_leave()
                pyautogui.sleep(game_load_wait)

            # pyautogui.sleep(5)

            start_game(level)
            wait_to_load()
            if merc_died():
                merc_back(level, game_load_wait)
            if need_heal() or need_mana(0.25):
                heal_back(level, game_load_wait)
            # ice_armor()
            mimic_keyboard_press(valkyrie, duration=0.1)
            get_portal()
            wait_to_load()
            to_pindle(0.2)
            pyautogui.sleep(0.5)
            # found = fight_farm()

            result_queue = Queue()
            fight_thread = multiprocessing.Process(target=fight_farm, args=(result_queue,))
            fight_thread.start()
            while True:
                try:
                    if not result_queue.empty():
                        found = result_queue.get()
                        break

                    # if danger_need_heal(0.6):
                    if danger_may_need_heal() or danger_merc():
                        print("Low HP, leave...")
                        fight_thread.terminate()
                        keyboard.release(Key.shift)
                        pyautogui.keyUp('alt')
                        break

                    time.sleep(0.2)  # Simulate periodic checking
                except KeyboardInterrupt:
                    print("\nCtrl+C detected! Stopping fight threads...")
                    fight_thread.terminate()
                    break

            if found:
                found_counter += 1
            success_counter += 1
            leave()
            wait_to_leave()
            with update_time.get_lock():
                counter += 1
                update_time.value = time.time()
            end_time_round = datetime.now()
            print("found drop rounds: {}".format(found_counter))
            print("total rounds: {}".format(counter))
            print("round time: {}\n".format(end_time_round - start_time_round))
            pyautogui.sleep(game_load_wait)
    except KeyboardInterrupt:
        end_time = datetime.now()
        print('Duration: {}'.format(end_time - start_time))
        print('Loop interrupted')


def check_rounds():
    last_update_time = multiprocessing.Value('d', time.time())
    updater_thread = multiprocessing.Process(target=start, args=(last_update_time,))
    updater_thread.start()
    start_diablo = False
    while True:
        try:
            with last_update_time.get_lock():
                time_since_update = time.time() - last_update_time.value

            # if time_since_update > 150:  # 2 minutes 30 seconds
            if time_since_update > 600:
                print("Value hasn't updated for 10 mins. Restarting game...")
                # restart_event.set()  # Signal the updater thread to stop
                time.sleep(5)  # Allow the updater thread to exit
                updater_thread.terminate()
                start_diablo = True

            if start_diablo:
                restart_game_from_battlenet()
                with last_update_time.get_lock():
                    last_update_time.value = time.time()
                updater_thread = multiprocessing.Process(target=start, args=(last_update_time,))
                updater_thread.start()
                start_diablo = False

            time.sleep(5)  # Simulate periodic checking
        except KeyboardInterrupt:
            print("\nCtrl+C detected! Stopping threads...")
            updater_thread.terminate()
            break


def restart_game_from_battlenet():
    pyautogui.hotkey('alt', 'f4')
    pyautogui.sleep(5)
    click_play()
    pyautogui.sleep(10)
    mimic_mouse_click(500, 500)
    pyautogui.sleep(10)
    mimic_mouse_click(500, 500)
    pyautogui.sleep(10)
    mimic_mouse_click(500, 500)


def click_play():
    pyautogui.sleep(1)
    retry, loc_x, loc_y = 0, 0, 0
    while loc_x == 0 and loc_y == 0 and retry <= 10:
        pyautogui.sleep(0.1)
        loc_x, loc_y = detect_template_bin(battlenet_play, take_screenshot())
        retry += 1
    mimic_mouse_click(*[x + y for x, y in zip((loc_x, loc_y), convert_resolution(30, 20))])


if __name__ == "__main__":
    # start()

    # event = multiprocessing.Event()

    check_rounds()

    # Create initial updater thread
    # updater_thread = multiprocessing.Process(target=start, args=(last_update_time, event))
    # reader_thread = multiprocessing.Process(target=check_rounds, args=(last_update_time, event))

    # Start threads
    # updater_thread.start()
    # reader_thread.start()
    #
    # try:
    #     # Keep the main thread alive to monitor the threads
    #     while True:
    #         time.sleep(0.1)
    # except KeyboardInterrupt:
    #     print("\nCtrl+C detected! Stopping threads...")
    #     event.set()
    #     updater_thread.terminate()
    #     reader_thread.terminate()
    #
    # print("All threads stopped. Program exiting.")
