divisorSums = {};
amicable = {};

function divisorSum(n)
  if divisorSums[n] then
    return divisorSums[n];
  end
  local sum = 1;
  for i = 2, math.sqrt(n) do
    if n % i == 0 then
      sum = sum + i;
      if i ~= n / i then
        sum = sum + (n / i);
      end
    end
  end
  divisorSums[n] = sum;
  return sum;
end


function checkAmicable(a,b)
  return a ~= b and
    divisorSum(a) == b and
    divisorSum(b) == a;
end

local sum = 0;
for i = 1, 10000 do
  for j = i+1, 10000 do
    if checkAmicable(i,j) then
      if not amicable[i] then
        amicable[i] = true;
        sum = sum + i;
      end
      if not amicable[j] then
        amicable[j] = true;
        sum = sum + j;
      end
    end
  end
end

print(sum);