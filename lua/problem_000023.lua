local divisorSums = {};

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


function abundant(n)
  return divisorSum(n) > n;
end


local sum = 0;
local abundantSum = false;
for i = 1, 28124 do
  abundantSum = false;
  for j = 1, i-1 do
    if abundant(j) and abundant(i-j) then
      abundantSum = true;
      break;
    end
  end

  if not abundantSum then
    sum = sum + i;
  end
end

print(sum);