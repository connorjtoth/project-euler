local last = 1;
local current = 1;
local sum = 0;

while current <= 4e6 do
  current, last = current + last, current;
  if current % 2 == 0 then
    sum = sum + current;
  end
end

print(sum);