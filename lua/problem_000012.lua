function count_divisors(num)
  if num == 1 then return 1 end
  local divisors = 2;
  for i = 2, math.sqrt(num) do
    if num % i == 0 then
      divisors = divisors + 2;
    end
  end
  return divisors;
end

local current = 1;
local triangle = 1;


while count_divisors(triangle) <= 500 do
  current = current + 1;
  triangle = triangle + current;
end

print(triangle);