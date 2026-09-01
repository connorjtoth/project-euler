local prime_sum = 2;
local current = 3;
local primes= {2};
local compflag = false;
while current < 2e6 do
  compflag = false;
  for _,prime in ipairs(primes) do
    if (current % prime) == 0 then
      compflag = true;
      break;
    end
    if (prime > math.sqrt(current)) then
      break;
    end
  end

  if not compflag then
    table.insert(primes, current);
    prime_sum = prime_sum + current;
  end

  current = current + 2;
end

print(prime_sum);


