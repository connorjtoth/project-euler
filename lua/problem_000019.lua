function isLeapYear(year)
  if year % 400 == 0 then
    return true;
  elseif year % 100 == 0 then
    return false;
  elseif year % 4 == 0 then
    return true;
  else
    return false;
  end
end

function daysInMonth(month, year)
  if month == 4 or month == 6 or month == 9 or month == 11 then
    return 30;
  elseif month == 2 then
    if not isLeapYear(year) then
      return 28;
    else
      return 29;
    end
  else
    return 31;
  end
end



local firstDay = 2; -- 1 = sunday, 7 = sat
local currentMonth = 1; -- 1 = jan, 12 = dec
local currentYear = 1900;

local numFirst = 0;

repeat
  if currentYear >= 1901 and currentYear <= 2000 then
    if firstDay == 1 then
      numFirst = numFirst + 1;
    end
  end

  -- incrementing step
  if currentMonth == 12 then
    firstDay = ((firstDay + daysInMonth(currentMonth, currentYear)) % 7) + 1;
    currentYear = currentYear + 1;
    currentMonth = 1;
  else
    firstDay = ((firstDay + daysInMonth(currentMonth, currentYear)) % 7) + 1;
    currentMonth = currentMonth + 1;
  end

until currentYear == 2001

print(numFirst);