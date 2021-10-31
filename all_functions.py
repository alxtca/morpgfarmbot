import time
import pyautogui
import random
from collections import namedtuple
import csv
import pytesseract as tess
from PIL import Image, ImageFilter
#from main_farm import seed_name

filename_w_garden_bed_coords = 'rc1.csv'
seed_name = "wheat seed"
close_captcha = False
captchas_left = 5

def buildCoordsList(csvfile):
  Mob = namedtuple('Mob', ["x", "y"])
  cl = []
  reader = csv.reader(open(csvfile))
  for x,y in reader:
    cl.append(Mob(x=int(x), y=int(y)))
  return cl

def myrandomClickCoords():
  return random.randrange(-3,1) + random.random()*2
def randomWaitTime(t):
  time.sleep(t+random.random()/2)

def captchaCheck():
  print("checking captcha")
  local_counter = captchas_left
  # pyautogui.pixelMatchesColor(pixtocheck[0], pixtocheck[1], (correct)))
  #pixtocheck1 = (842,502)
  #pixtocheck2 = (842,559)
  pixtocheck3 = (1065,503)
  pixtocheck4 = (1065,564)
  rgb = (53,53,53)
  #sample1 = pyautogui.pixel(pixtocheck1[0], pixtocheck1[1])
  #sample2 = pyautogui.pixel(pixtocheck2[0], pixtocheck2[1])
  sample3 = pyautogui.pixel(pixtocheck3[0], pixtocheck3[1])
  sample4 = pyautogui.pixel(pixtocheck4[0], pixtocheck4[1])
  #sample = pyautogui.pixel(x, y)
  if (sample3 == rgb or sample4 == rgb):#sample1 == rgb or sample2 == rgb or 
    #second check:
    text = tessReading((747, 386, 134, 45))
    if ("bot" in text):
      print("captcha is DETECTED")
      if (close_captcha and local_counter > 0): #close captha and loose 1 point
        clickWrap((1148,407))
        clickWrap((941,645))
        clickWrap((1155,489))
        local_counter = local_counter - 1
      else:
        input("solve captcha and press enter.")
      randomWaitTime(3)
  else:
    print("no captcha detected")

def clickWrap(coords, t=1.7):
  x = coords[0]+myrandomClickCoords()
  y = coords[1]+myrandomClickCoords()
  captchaCheck()
  pyautogui.click(x,y)
  randomWaitTime(t)
def clickWrapFast(coords, t=0):
  x = coords[0]+myrandomClickCoords()
  y = coords[1]+myrandomClickCoords()
  captchaCheck()
  pyautogui.click(x,y)
  randomWaitTime(0)
def pressWrap(button, t=0):
    pyautogui.keyDown(button)
    randomWaitTime(t)
    pyautogui.keyUp(button)
    randomWaitTime(t)

def tessReading(region_coords): # takes screen coordinates and returns text in this area
  im = pyautogui.screenshot(region=region_coords) # OBS TESSESRACT NEED BIG SPACE ARROUND TEXT!!!
  #im = im.convert(mode="L")
  im = im.filter(ImageFilter.GaussianBlur(0.3)) #this is needed to read all Queued numbers
  #im = im.filter(ImageFilter.SMOOTH_MORE)
  #im = im.filter(ImageFilter.GaussianBlur(0.5))
  #im = im.filter(ImageFilter.SMOOTH)
  #im.save('tess_test_sample.png')
  tess.pytesseract.tesseract_cmd = r"C:\Tesseract-OCR\tesseract.exe"
  text = tess.image_to_string(im, lang='eng', config='--psm 13 --oem 3') # config='--psm 13 --oem 3 -c tessedit_char_whitelist=(),0123456789'
  #print("extracted text:", text) #function that call shall print to know what could not read
  return text
def verifyGameCoords(coords_to_verify): #this will verify (x,y)
  # if requested coords are the same as current_position_in_game_coords return True
  text = tessReading((1314, 88, 115, 36)) #all island coordinates are tested, no failure detected
  print("game coords extracted:", text)
  x = ''
  y = ''
  x_is_done = False
  y_is_done = False

  i = 1 #skip checking first character because it is cutted and can be seen as a digit 1
  while i < len(text): #for i in range(0, len(text)): does not alloud i to be changed inside loop code
    if(text[i].isdigit()):
      if(x_is_done == False):
        x += text[i]
        if (text[i+1].isdigit()): #check digit after
          x += text[i+1]
          x_is_done = True
          i += 1
        else:
          x_is_done = True
          i += 1
      
      elif (y_is_done == False): # when x is done digits add to y
        y += text[i]
        if (text[i+1].isdigit()): #check digit after
          y += text[i+1]
          y_is_done = True
          i += 1
        else:
          y_is_done = True
          i += 1
    i += 1
  #end while
  try:
    x = int(x)
    y = int(y)
  except ValueError:
    print("value error")
    return 10
  except:
    print("something else is wrong")
    input("press enter to continue...")

  #print(x,y)
  #print(coords_to_verify[0], coords_to_verify[1])
  return (coords_to_verify[0]==x and coords_to_verify[1]==y)
def verifyGameCoordX(coordX_to_verify): #this will verify x coord only.
  text = tessReading((1314, 88, 115, 36))
  print("game coordsX extracted:", text)
  x = ''
  x_is_done = False

  i = 1 #skip checking first character because it is cutted and can be seen as a digit 1
  while i < len(text): #for i in range(0, len(text)): does not alloud i to be changed inside loop code
    if(text[i].isdigit()):
      if(x_is_done == False):
        x += text[i]
        if (text[i+1].isdigit()): #check digit after
          x += text[i+1]
          x_is_done = True
          i += 1
        else:
          x_is_done = True
          i += 1
    i += 1
  #end while
  try:
    x = int(x)
  except ValueError:
    print("value error")
    return 10
  except:
    print("something else is wrong")
    input("press enter to continue...")
  #print(x)
  #print(coordX_to_verify)
  #print(coordX_to_verify == x)
  return (coordX_to_verify==x)
#---CLICK TYPE FUNCTIONS---- these corresponds to clicking one existing button inside a game.
def openCloseInventory():
  clickWrap((1623,164))
def loadPetInventory():
  clickWrap((1517,446))
def equipItem3d():
  clickWrap((1536,225))
def closeChest():
  clickWrap((1202,362))
def withdrawAll():
  clickWrap((819,800))
def withdrawOne():
  clickWrap((812,742))
def clickSearch():
  clickWrap((843,363))
def unloadPetInventory():
  clickWrap((1554,447))
def loadPetInventory():
  clickWrap((1519,448))
def depositInventoryItems():
  clickWrap((1166,711))
def depositPetInventory():
  clickWrap((1165,753))
def selectSearchedItem():
  clickWrap((753,478))
def closeInventorySecure():
  pyautogui.moveTo(1202,362, 0.6)
#---END CLICK TYPE FUNCTIONS----
def withdrawSeeds():
    if (verifyGameCoords((10,10))==True):
      pressWrap('w', 2)
      clickSearch()
      pyautogui.write(seed_name, interval = 0.28)
      selectSearchedItem()
      withdrawAll()
      openCloseInventory()
      loadPetInventory()
      withdrawAll()
      equipItem3d()
      openCloseInventory()
      closeInventorySecure()
      closeChest()
      print("Seeds have been withdrawn.")
    else:
      input("Something went wrong. Should stay on (10,10) now")
def withdrawRake():
  if (verifyGameCoords((10,10))==True):
    pressWrap('w', 2)
    clickSearch()
    pyautogui.write('rake', interval = 0.28)
    selectSearchedItem()
    withdrawOne()
    openCloseInventory()
    equipItem3d()
    openCloseInventory()
    closeInventorySecure()
    closeChest()
    print("Rake has been withdrawn.")
  else:
    input("Something went wrong. Should stay on (10,10) now")

def goToStartPos(click_coords, game_coords): #coords are tuples(x,y)
  clickWrap(click_coords)
  while (True): # run this check loop until character will come to correct position
    if (verifyGameCoords(game_coords) == True):
      print("in start position")
      return

def switchAction1():
  # dumb or smart function? 
  # smart: locate window on screen, and click in bottom right corner.
  # dumb: clickWrap(coords)
  # option: include text verification at clicking coordinated

  #dumb
  clickWrap((299,604))
def switchAction2():
  clickWrap((299,604))
  clickWrap((299,604))

def clickAllCoords():
  coords = buildCoordsList(filename_w_garden_bed_coords)
  #start clicking on beds only when Action is Queuing
  while (True):
    if (actionIs("Queuing")):
      for coord in coords:
        clickWrapFast((coord.x, coord.y))
      return
    switchAction1()
    print("Switching action")
    randomWaitTime(1)

def activeVerification(): #only notes here
  # lets assume 5 seconds lag
  # if lag, active verification will return True(means, action is compleete) which is a problem - seed unload / returnToChest() will not work
  # I think the STATUS should be verifyed
  """
  3 types of status
  Action: Queuing    (pause)
    is when all coords are clicked and need switchAction2() to enable action
  Action: Active     (queue)
    is 1. when char is in movement doing harvest/raking
       2. when queue is 0
  Action: Paused     (resume)
    is when more coords requires action, but inventory is full or no more seeds
  
  """
  #
  pass
def activeVerificationPlanting(): #this will run until action is Paused and queue > 0
  while (True):
    captchaCheck()
    if (actionIs("Active") and farmingQueNotEpty()!=True): # end of one cycle
      return 10
    if (actionIs("Pause") and farmingQueNotEpty()): # need more seeds
      return 1
    randomWaitTime(5)
def activeVerificationRaking():
  while True:
    captchaCheck()
    if farmingQueNotEpty() != True: #if queue is empty
      break
    randomWaitTime(5)

def farmingQueNotEpty(): #returns True if not empty
  # read Queued: 'number'.     if > 0 queue is not empty.
  text = tessReading((134,569, 95, 25)) #((184,569, 65, 25)) was
  print("Farming queued # extracted:", text)
  #extract numbers from that text
  digits = ""
  for char in text:
    if (char.isdigit()):
      digits += char
  
  try:
    text = int(digits)
  except ValueError: #how to give it another try?
    #may be pack into while True and break/continue here?
    print("value error")
    input("Value error, programm going to fail.")
  except:
    print("something else is wrong")
    input("press enter to continue...")
  
  print(text>0)
  return (text > 0)
def actionIs(status):
  text = tessReading((136,593, 129, 25))
  print("Action Is extracted:", text)
  return (status in text)

def unloadSeedFromPet():
  openCloseInventory()
  unloadPetInventory()
  equipItem3d()
  openCloseInventory()
def moveHarvestToPet():
  openCloseInventory()
  loadPetInventory()
  openCloseInventory()
def unloadHarvestToChest():
  if (verifyGameCoords((10,10))==True):
    pressWrap('w', 2)
    depositInventoryItems()
    depositPetInventory()
    closeChest()
def unloadSeedsToChest():
  if (verifyGameCoords((10,10))==True):
    pressWrap('w', 2)
    openCloseInventory()
    equipItem3d()
    depositInventoryItems()
    depositPetInventory()
    openCloseInventory()
    closeInventorySecure()
    closeChest()

def returnToChest():
  while (True):
    pressWrap('a', 1)
    if (verifyGameCoordX(8)): #verify coordinates on the edge of map
      print("edge confirmed")
      break
  while (True):
    pressWrap('s', 1)
    if (verifyGameCoords((8,9))): #verify coordinates of bottom left corner
      print("corner confirmed")
      break
  clickWrap((1101,530)) #click on tile in front of chest
def unequipRake():
  openCloseInventory()
  equipItem3d()
  openCloseInventory()
  closeInventorySecure()

def sufficientSeed():
  #right click
  #new offer
  #max
  # read
  # click "chest" to close offer
  text = tessReading((715,451,50,24))
  print("text extracted:", text)
  x = ''
  i = 1 #skip checking first character because it is cutted and can be seen as a digit 1
  while i < len(text):
    if(text[i].isdigit()):
      x += text[i]
    i += 1
  try:
    x = int(x)
  except ValueError:
    print("value error")
    return 10
  except:
    print("something else is wrong")
    input("press enter to continue...")
  return (x>200)