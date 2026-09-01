local counter = 0;
for i = 1, 999 do
  if i % 3 == 0 or i % 5 == 0 then
    counter = counter + i;
  end
end

print(counter);