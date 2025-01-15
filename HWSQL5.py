"""
1. The PARTITION BY function groups the data by employee_id, and the SUM() function with ORDER BY calculates
   the running total for each sale within the group.

2. '->' used to access nested objects or arrays in JSON data:
   details -> 'features' = {"RAM": "16GB", "Storage": "512GB"}
   '->>' used to get a text value for further processing:
   details ->> 'name' = "Laptop".

3. 1) The code creates table "array_example"
   2) Inserts arrays as values
   3) Shows a specific array element, according to our query
   4) Shows the rows containing a specific number, according to our query

4. GENERATED ALWAYS sets a condition for the column and will automatically calculate input values.
"""
