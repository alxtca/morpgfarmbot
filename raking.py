import all_functions as funcs

#start_pos_click_coords = [(1473,668), (1526,641)]
#start_pos = [(18,12), (18,21)]
#end_pos = [(10,18), (10,27)]

def rakingMain(start_pos_click_coords, start_pos, end_pos, rounds):
  funcs.randomWaitTime(3)
  funcs.withdrawRake()
  for round in range(rounds):
    funcs.goToStartPos(start_pos_click_coords[round], start_pos[round]) #start pos to start click on beds
    funcs.clickAllCoords()
    funcs.switchAction2()
    funcs.activeVerificationRaking()
    while (funcs.verifyGameCoords(end_pos[round])!=True): #if coords are not as expected
      print("end position is not achieved yet")
      funcs.randomWaitTime(8)
  funcs.returnToChest()
  funcs.unequipRake()
  funcs.unloadHarvestToChest()
