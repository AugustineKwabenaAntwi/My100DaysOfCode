## Exercise: Numbers in python
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
is its length. If tiles cost 500 rs per square feet, how much will be the total
cost to replace all tiles. Calculate and print the cost using python
(Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17

## Exercise: String in Python

1. Create 3 variables to store street, city and country, now create address variable to
store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
Now Print the address in such a way that the street, city and country prints in a separate line
2. Create a variable to store the string "Earth revolves around the sun"
    1. Print "revolves" using slice operator
    2. Print "sun" using negative index
3. Create two variables to store how many fruits and vegetables you eat in a day.
Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
4. I have a string variable called s='maine 200 banana khaye'. This of course is a
wrong statement, the correct statement is 'maine 10 samosa khaye'.
Replace incorrect words in original strong with new ones and print the new string.
Also try to do this in one line.

## Exercise: Python Lists
1. Let us say your expense for every month are listed below,
	1. January -  2200
 	2. February - 2350
    3. March - 2600
    4. April - 2130
    5. May - 2190

Create a list to store these monthly expenses and using that find out,

    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and
    got a refund of 200$. Make a correction to your monthly expense list
    based on this

2. You have a list of your favourite marvel super heros.
```
heros=['spider man','thor','hulk','iron man','captain america']
```

Using this find out,

    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk',
       so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily :)
       So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
       Do that with one line of code.
    5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)

    ## Exercise: Python If Condition
1. Using following list of cities per country,
    ```
    india = ["mumbai", "banglore", "chennai", "delhi"]
    pakistan = ["lahore","karachi","islamabad"]
    bangladesh = ["dhaka", "khulna", "rangpur"]
    ```
    1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
    2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
    1. Ask user to enter his fasting sugar level
    2. If it is below 80 to 100 range then print that sugar is low
    3. If it is above 100 then print that it is high otherwise print that it is normal