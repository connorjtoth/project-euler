local current = -1;
for a = 1, 9 do
  for b = 0, 9 do
    for c = 0, 9 do
      local temp = (9091 * a + 910 * b + 100 * c);
      for divisor = 10, 90 do
        if temp % divisor == 0 then
          if temp / divisor <= 999 then
            if temp > current then
              current = temp;
            end
          end
        end
      end
    end
  end
end

print(current * 11);