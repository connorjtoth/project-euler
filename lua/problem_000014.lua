local L = {};
local max = 1;
L[1] = 1;

function collatz(num)
  if num % 2 == 0 then
    return num / 2;
  else
    return num * 3 + 1;
  end
end

function setCollatzLength(num)
  local temp = collatz(num);
  if not L[temp] then
    setCollatzLength(temp);
  end
  L[num] = L[temp] + 1;
end

for i = 2, 1e6 do
  if not L[i] then
    setCollatzLength(i);
  end
  if L[i] > L[max] then
    max = i;
  end
end

print(max);