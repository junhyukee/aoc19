from part1 import inputs

acc = 0;

for datum in inputs:
  module_fuel = 0;
  current_fuel = datum;
  while current_fuel > 0:
    current_fuel = current_fuel // 3 - 2
    if current_fuel > 0:
      module_fuel += current_fuel
  acc += module_fuel

print(acc);