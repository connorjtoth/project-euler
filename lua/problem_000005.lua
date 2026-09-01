primes = {};
for i = 2, 20 do
  local temp = i;
  for _, prime in ipairs(primes) do
    if (temp % prime == 0) then
      temp = temp / prime;
    end
  end
  if temp ~= 1 then
    table.insert(primes,temp);
  end
end

local count = 1;

for _, prime in ipairs(primes) do
  count = count * prime;
end

print(count);