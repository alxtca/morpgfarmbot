import all_functions as funcs

# All clicking coordinates depend on screen resolution.
#start_pos_click_coords = [(1473,668), (1526,641)] #second click from where?
#start_pos = [(18,12), (18,21)] # ok ok 
#end_pos = [(10,18), (10,27)]

def plantingMain(start_pos_click_coords, start_pos, end_pos, rounds):
  funcs.randomWaitTime(3)
  funcs.withdrawSeeds()
  for round in range(rounds):
  #because he has seeds in inventory, he can go to new start position and keep sowing after round #1
      funcs.goToStartPos(start_pos_click_coords[round], start_pos[round]) #start pos to start click on beds
      funcs.clickAllCoords()
      funcs.switchAction2()
      funcs.activeVerificationPlanting() #this will run until action is Paused and queue > 0
      while(funcs.farmingQueNotEpty()): #inside here plant to all locations that were added to the queue.
          funcs.unloadSeedFromPet()
          funcs.switchAction1()
          if (funcs.activeVerificationPlanting() == 10):
            break
          funcs.returnToChest() #to get more seeds
          funcs.withdrawSeeds()
          funcs.switchAction1()
          if (funcs.activeVerificationPlanting() == 10):
            break
      # assuming farming queue is empty and at least one seed left in inventory
      while (funcs.verifyGameCoords(end_pos[round])!=True): #if coords are not as expected
          print("end position is not achieved yet")
          funcs.randomWaitTime(8)
          # note for future development: make character move to desired position
  #end for
  # now all planting is done. Go clean up.
  funcs.returnToChest()
  funcs.unloadSeedsToChest() #unequip seed?