def seed_generator(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    number_str=str(number);
    return {
        8: int(number_str[2:-2]),
        7: int(number_str[1:-2]),
        **dict.fromkeys(range(3, 7), int(number_str[0:-2])),
    }.get(len(number_str), 0)
    
def mid_square(seed:int ,num_iterations:int):
  if(len(str(seed)) <4 ):
    raise ValueError("Seed value must have at least 4 digits.");
  values = [0 for _ in range(num_iterations)]
  seeds = [0 for _ in range(num_iterations)]
  values[0] = pow(seed,2)
  seeds[0]= seed_generator(values[0]);
  for i in range(num_iterations-1):
    if(values[i]==0):break;
    values[i+1]= pow(seeds[i],2);
    seeds[i+1]=seed_generator(values[i+1]);  
  return seed,values,seeds

print(mid_square(1221,100))    

  