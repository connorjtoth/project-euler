local arr = {0,1,2,3,4,5,6,7,8,9};
for count = 2, 1e6 do
  for i = #arr, 2, -1 do
    if arr[i-1] < arr[i] then
      for j = #arr, i, -1 do
        if arr[j] > arr[i-1] then
          arr[j],arr[i-1]=arr[i-1],arr[j];
          break;
        end
      end
      for j = 0, (#arr - i)/2 do
        arr[i+j],arr[#arr-j]=arr[#arr-j],arr[i+j];
      end
      break;
    end
  end
end


print(table.concat(arr, ''));
