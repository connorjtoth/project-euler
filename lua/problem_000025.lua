local fib1 = {1};
local fib2 = {1};
local sum = {1};
local index = 2;

function add()
  sum = {};
  for i = 1, math.max(#fib1, #fib2) do
    sum[i] = (fib1[i] or 0) + (fib2[i] or 0);
  end

  local i = 1;
  while sum[i+1] or sum[i] >= 10 do
    if sum[i] >= 10 then
      if sum[i+1] then
        sum[i+1] = sum[i+1] + math.floor(sum[i] / 10);
      else
        sum[i+1] = math.floor(sum[i] / 10);
      end
      sum[i] = sum[i] % 10;
    end
    i = i + 1;
  end


  fib1 = fib2;
  fib2 = sum;
  index = index + 1;
end

while #sum < 1000 do
  add();
end

print(index);