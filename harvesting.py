import all_functions as funcs

# All clicking coordinates depend on screen resolution.
#start_pos_click_coords = [(1473,668), (1526,641)]
#start_pos = [(18,12), (18,21)]
#end_pos = [(10,18), (10,27)]

def harvestingMain(start_pos_click_coords, start_pos, end_pos, rounds):
  funcs.randomWaitTime(3)
  for round in range(rounds): # 2 cycles of coords clicking
      funcs.goToStartPos(start_pos_click_coords[round], start_pos[round]) #start pos to start click on beds
      funcs.clickAllCoords()
      funcs.switchAction2()
      funcs.activeVerificationPlanting()
      while(funcs.farmingQueNotEpty()): #inside here plant to all locations that were added to the queue.
          funcs.moveHarvestToPet()
          funcs.switchAction1()
          if (funcs.activeVerificationPlanting() == 10):
            break
          funcs.returnToChest() #to unload
          funcs.unloadHarvestToChest()
          funcs.switchAction1()
          if (funcs.activeVerificationPlanting() == 10):
            break
      # assuming farming queue is empty and at least one seed left in inventory
      while (funcs.verifyGameCoords(end_pos[round])!=True): #if coords are not as expected
          print("end position is not achieved yet")
          funcs.randomWaitTime(8)
          # note for future development: make character move to desired position
  #end for
  funcs.returnToChest()
  funcs.unloadHarvestToChest()