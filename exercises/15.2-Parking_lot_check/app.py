parking_state = [
  [1,0,1,1,0,1],
  [2,0,1,1,0,1],
  [1,0,2,1,0,1],
  [1,0,1,1,0,1],
  [1,0,1,1,0,2],
  [1,0,1,1,0,1],
]

def get_parking_lot(parking_state):
  


  state1 = {
    # "total_slots":0,
    # "available_slots":0,
    # "occupied_slots":0
  }
  for lists in parking_state:
    for elements in lists:
      
      
      state1.setdefault('total_slots',0)
      state1['total_slots']  += 1
      if elements == 1:
        state1.setdefault('occupied_slots',0)
        state1['occupied_slots']  += 1
      if elements == 2:
        state1.setdefault('available_slots',0)
        state1['available_slots']  += 1
  return state1    
        
      
      
print(get_parking_lot(parking_state))