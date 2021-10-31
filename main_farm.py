import raking, planting, harvesting, wait_to_harvest

#important game settings:
# game size 1.75x
# toggle dark interface
# farming queue options: stop movement while queuing "ON"

start_pos_click_coords = [(1473,668), (1526,641)]
start_pos = [(18,12), (18,21)]
end_pos = [(10,18), (10,27)]
bed_segments = 2 #related to all above variables
rounds_to_run = 2 # need 200 seeds per round

#seed type specifics:
#seed_name = "wheat_seed" #defined in all_functions.py
rgb = (184,152,99)
pixel_coords = (1315,332)

# ----MAIN program-------------
for i in range(rounds_to_run): # run 
  raking.rakingMain(start_pos_click_coords, start_pos, end_pos, bed_segments)
  planting.plantingMain(start_pos_click_coords, start_pos, end_pos, bed_segments)
  wait_to_harvest.waitToHarvestMain(rgb, pixel_coords)
  harvesting.harvestingMain(start_pos_click_coords, start_pos, end_pos, bed_segments)
#---end------------------------