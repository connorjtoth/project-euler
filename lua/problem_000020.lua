local digits = {};
digits[1] = 1;

function multiply(digits, amt)
  for i = 1, #digits do
    digits[i] = digits[i] * amt;
  end

  local i = 1;
  while digits[i+1] or digits[i] >= 10 do
    if digits[i] >= 10 then
      if digits[i+1] then
        digits[i+1] = digits[i+1] + math.floor(digits[i] / 10);
      else
        digits[i+1] = math.floor(digits[i] / 10);
      end
      digits[i] = digits[i] % 10;
    end
    i = i + 1;
  end
end

for i = 1, 100 do
  multiply(digits, i);
end

local sum = 0;
for i = 1, #digits do
  sum = sum + digits[i];
end

print(sum);