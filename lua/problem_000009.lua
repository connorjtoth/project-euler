local product = -1;

for a = 1, 998 do
  for b = 2, 1000 - a do
    for c = 3, 1000 - a - b do
      if a + b + c == 1000 then
        if a*a + b*b == c*c then
          product = a * b * c;
          return print(product);
        end
      end
    end
  end
end
