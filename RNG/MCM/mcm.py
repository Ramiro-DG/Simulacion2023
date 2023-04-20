def initial_seed_generator(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    number_str=str(number);
    return {
        8: int(number_str[2:-2]),
        7: int(number_str[1:-2]),
        **dict.fromkeys(range(3, 7), int(number_str[0:-2])),
    }.get(len(number_str), 0)
    
def mid_square(initial_seed:int ,num_iterations:int):
  if(len(str(initial_seed)) !=4 ):
    raise ValueError("initial_seed value must have at least 4 digits.");
  values = [0 for _ in range(num_iterations)]
  initial_seeds = [0 for _ in range(num_iterations)]
  values[0] = pow(initial_seed,2)
  initial_seeds[0]= initial_seed_generator(values[0]);
  for i in range(num_iterations-1):
    if(values[i]==0):break;
    values[i+1]= pow(initial_seeds[i],2);
    initial_seeds[i+1]=initial_seed_generator(values[i+1]);  
  return initial_seed,values,initial_seeds

print(mid_square(1232,100))    

  