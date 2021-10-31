from all_functions import randomWaitTime
import pyautogui

def waitToHarvestMain(rgb, pixel_coords):
  while True:
    sample = pyautogui.pixel(pixel_coords[0],pixel_coords[1])
    if (sample == rgb):
      break
  randomWaitTime(20) #correction