squared_sum = 0;
squares_summed = 0;
for i = 1, 100 do
  squares_summed = squares_summed + i * i;
  for j = 1, i do
    if j == i then
      squared_sum = squared_sum + i * j;
    else
      squared_sum = squared_sum + 2 * i * j;
    end
  end
end

print(squared_sum - squares_summed);