local primes = {2};
local current = 3;
local compflag = false;
while #primes < 10001 do
  compflag = false;
  for _, prime in ipairs(primes) do
    if (current % prime) == 0 then
      current = current + 2;
      compflag = true;
    end
  end
  if not compflag then
    table.insert(primes, current);
  end
end

print(primes[10001]);