# Lab: Exploring Higher Order Functions in Python

This lab is designed to deepen your understanding of higher order functions in Python. You'll apply `map` and `filter` functions on various datasets, focusing on real-world examples to grasp these concepts effectively.

1. **Temperature Conversion:**

   - Begin with a list of temperatures in Celsius: `temperatures = [12.5, 18.1, 15.6, 17.8, 20.1, 22.6, 18.9]`.
   - Your first task is to convert these temperatures to Fahrenheit.
   - Use the `map` function with either a named function or a lambda function for this conversion. For example:
     ```python
     def celsius_to_fahrenheit(celsius):
         return (celsius * 9 / 5) + 32
     ```
   - Apply this function to the list of Celsius temperatures and print the converted Fahrenheit temperatures.

2. **Filtering Temperatures:**

   - Use the `filter` function to select temperatures.
   - First, filter out all temperatures below 18.0°C. This can be achieved using either a lambda function or a named function.
   - Then, experiment by adjusting the criteria to select temperatures below 18.0°C.

3. **Combining Filter and Map:**

   - Combine `filter` and `map` functions to convert only the temperatures above 14.0°C to Fahrenheit.
   - You can achieve this in a single line of code using function chaining.
   - Observe and analyze the output to understand how these two functions work together.

4. **Filter Function with Integers:**

   - Apply the `filter` function to a list of integers: `data = [1, 3, 5, 2, 7, 4, 10]`.
   - First, filter for even numbers using a lambda function, and then using a named function.
   - Compare the outputs to understand how lambda and named functions differ in readability and functionality.

5. **Map Function Applications:**
   - Use the `map` function on the same list of integers to apply a transformation.
   - Apply a function that adds one to each number in the list, again using both a lambda and a named function.
   - Analyze the outputs to understand how the `map` function applies a given operation to each item in a list.

Further Reading:

1. [Python Tips - Map, Filter, Reduce](http://book.pythontips.com/en/latest/map_filter.html)
2. [W3Schools - map() Function Tutorial](https://www.w3schools.com/python/ref_func_map.asp)
3. [W3Schools - filter() Function Tutorial](https://www.w3schools.com/python/ref_func_filter.asp)
