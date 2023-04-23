import numpy as np

def seed_generator(number:int)->int:
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    number_str=str(number);
    if(len(number_str)==8):
        return int(number_str[2:-2])
    elif(len(number_str)==7):
        return int(number_str[1:-2])
    elif(len(number_str)<=6 and len(number_str)>=3):
      return int(number_str[0:-2])
    else:
      return 0

def mid_square(initial_seed:int ,num_iterations:int):
  if(len(str(initial_seed)) <4 ):
    raise ValueError("Seed value must have at least 4 digits.");
  values = [0 for _ in range(num_iterations)]
  seeds = [0 for _ in range(num_iterations)]
  values[0] = pow(initial_seed,2)
  seeds[0]= seed_generator(values[0]);
  for i in range(num_iterations-1):
    if(values[i]==0):break;
    values[i+1]=pow(seeds[i],2);
    seeds[i+1]=seed_generator(values[i+1]);  
  return np.divide(values,100_000_000)

def mid_square_no_div(initial_seed:int ,num_iterations:int):
  if(len(str(initial_seed)) <4 ):
    raise ValueError("Seed value must have at least 4 digits.");
  values = [0 for _ in range(num_iterations)]
  seeds = [0 for _ in range(num_iterations)]
  values[0] = pow(initial_seed,2)
  seeds[0]= seed_generator(values[0]);
  for i in range(num_iterations-1):
    if(values[i]==0):break;
    values[i+1]=pow(seeds[i],2);
    seeds[i+1]=seed_generator(values[i+1]);  
  return values

# print(mid_square(1232,1000))


  