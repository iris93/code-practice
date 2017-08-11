#!/bin/bash

echo hello world

if [ $1 -gt 90 ]
then
echo "good,$1"
elif [ $1 -gt 70 ]
then
echo "ok,$1"
else
echo "bad,$1"
fi

for day in Mon Tue Wed Thu Fri Sat Sun
do
echo $day
done
day=0
while [ $day -lt 5 ]
do
  let "day = $day + 1"
  echo $day
done

echo "Hit a key ,then hit return"
read Keypress

case "$Keypress" in
  [a-z] ) echo "Lowercase letter";;
  [A-Z] ) echo "Uppercase letter";;
  [0-9] ) echo "Digit";;
  * ) echo "Punctuation,whitespace,or other";;
esac

square(){
  let "res = $1 * $1"
  return $res
}
square 9
result=$?
echo $result

a=$RANDOM
echo $a
# echo ${var?there is an error}

select car in benchi baoma aodi
do
  echo $car
done
