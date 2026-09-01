function wordize(num)
  if num == 0 then return "" end

  local oneDict = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
  local tenDict = {"ten","twenty", "thirty","forty","fifty","sixty","seventy","eighty","ninety"};

  local ones = num % 10;
  local tens = math.floor((num % 100) / 10);
  local huns = math.floor(num / 100);

  local word = "";
  if num < 20 then
    word = word .. oneDict[num];
  elseif num < 100 then
    word = word .. tenDict[tens] .. wordize(num % 10);
  else
    word = word .. oneDict[huns] .. "hundred";
    if num % 100 ~= 0 then
      word = word .. "and" .. wordize(num % 100);
    end
  end
  return word;
end

local count = #"onethousand";
for i = 1, 999 do
  count = count + #wordize(i);
  print(wordize(i))
end

print(count);