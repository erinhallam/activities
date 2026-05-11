
# Question 1

Table: Question1

| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |

id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.
 

Write a solution to find the employees who earn more than their managers.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Question1 table:
|----|-------|--------|-----------|
| id | name  | salary | managerId |
|----|-------|--------|-----------|
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |

Output: 
| Employee |
|----------|
| Joe      |

Explanation: Joe is the only employee who earns more than his manager.

```SQL
select * 
FROM Question1
where salary > 80000
ORDER by salary DESC
-- place answer here 
id	name	salary	managerId
4	Max	90000	None

```
--Question 1 Answer
SELECT emp.name AS AnswerQ1
FROM Question1 AS emp 
INNER JOIN Question1 AS mgr
  ON emp.managerId = mgr.id
WHERE emp.salary > mgr.salary

# Question 2

Table: Question2


| Column Name | Type |
|-------------|------|
| id          | int  |
| salary      | int  |

id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an Salary.
 

Write a solution to find the second highest salary from the Salary table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

**Example 1:**

Input: 
Question2 table:

| id | salary |
|----|--------|
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |

Output: 

| SecondHighestSalary |
|---------------------|
| 200                 |

**Example 2:**

Input: 
Question2 table:

| id | salary |
|----|--------|
| 1  | 100    |

Output: 

| SecondHighestSalary |
|---------------------|
| null                |

```SQL
select DISTINCT salary
FROM Question2
ORDER by salary DESC
LIMIT 1
OFFSET 1
-- place answer here
salary
200
```
--Question 2 Answer
SELECT MAX(salary) AS SecondHighestSalary
  FROM Question2 a
 WHERE Salary < (SELECT MAX(salary) FROM Question2 b WHERE b.salary > a.salary)


# Question 3

Table: Question3 


| Column Name | Type    |
|-------------|---------|
| id          | int     |
| email       | varchar |

id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Question3  table:

| id | email   |
|----|---------|
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |

Output: 

| Email   |
|---------|
| a@b.com |

Explanation: a@b.com is repeated two times.

```SQL
select count (DISTINCT email), email
FROM Question3

-- place answer here 
count (DISTINCT email)	email
2	john@example.com

```
--Question 3 Answer
select email
from Question3
group by email
having count(email)>1

# Question4

Table: Question4


| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |


id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.

If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Question4 table:

| id  | name  | department | managerId |
|-----|-------|------------|-----------|
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |

Output: 

| name |
|------|
| John |

```SQL
select count (*), managerId
FROM Question4
GROUP by managerId
HAVING COUNT(*)>4

select *
FROM Question4
WHERE managerId = 101
-- place answer here 
count (*)	managerId
5	101

id	name	department	managerId
102	Dan	A	101
103	James	A	101
104	Amy	A	101
105	Anne	A	101
106	Ron	B	101

```
--Question 4 Answer
SELECT name 
FROM Question4 
WHERE id IN (
    SELECT managerId 
    FROM Question4 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5);
	
SELECT name 
FROM Question4 
WHERE id =(
    SELECT managerId 
    FROM Question4 
    GROUP BY managerId 
    HAVING COUNT(*) >= 5);

# Question 5


Table: Question5_1 &  Question5_2

|-------------|---------|
| Column Name | Type    |
|-------------|---------|
| id          | int     |
| name        | varchar |
|-------------|---------|
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 

Table: Question5_2

|-------------|------|
| Column Name | Type |
|-------------|------|
| id          | int  |
| customerId  | int  |
|-------------|------|

id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Question5_1 table:

| id | name  |
|----|-------|
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |

Question5_2 table:

| id | customerId |
|----|------------|
| 1  | 3          |
| 2  | 1          |

Output: 

| Question5_1 |
|-----------|
| Henry     |
| Max       |


```SQL
select a.*
FROM Question5_1 a
LEFT JOIN Question5_2 b
on a.id = b.customerId
WHERE b.customerId is NULL

-- place answer here 
id	name
2	Henry
4	Max

```
--Question 5 Answer
SELECT name as 'Never_Order'
from Question5_1 as a
Left Join Question5_2 as b
ON a.id = b.customerId
Where b.customerId is NULL

SELECT name as Customers
from Question5_1
where id not in (
    select customerId
    from Question5_2
);

# Question 6

Table: Question6


| Column Name    | Type     |
|----------------|----------|
| id             | int      |
| movie          | varchar  |
| description    | varchar  |
| rating         | float    |


id is the primary key (column with unique values) for this table.
Each row contains information about the name of a movie, its genre, and its rating.
rating is a 2 decimal places float in the range [0, 10]
 

Write a solution to report the movies with an odd-numbered ID and a description that is not "boring".

Return the result table ordered by rating in descending order.

The result format is in the following example.

 

Example 1:

Input: 
Question6 table:

| id | movie      | description | rating |
|----|------------|-------------|--------|
| 1  | War        | great 3D    | 8.9    |
| 2  | Science    | fiction     | 8.5    |
| 3  | irish      | boring      | 6.2    |
| 4  | Ice song   | Fantacy     | 8.6    |
| 5  | House card | Interesting | 9.1    |

Output: 

| id | movie      | description | rating |
|----|------------|-------------|--------|
| 5  | House card | Interesting | 9.1    |
| 1  | War        | great 3D    | 8.9    |

Explanation: 
We have three movies with odd-numbered IDs: 1, 3, and 5. The movie with ID = 3 is boring so we do not include it in the answer.

```SQL
select *
FROM Question6 
WHERE description <> 'boring' and id % 2 <> 0
ORDER by rating DESC

-- place answer here 
id	movie	description	rating
5	House card	Interesting	9.1
1	War	great 3D	8.9

```
--Question 6 Answer
SELECT id, movie, description, rating
FROM Question6
WHERE description <> 'boring'
AND id % 2 <> 0
ORDER by rating DESC

Select * 
from Question6
where  id  %2 <> 0  And  description <> 'boring'
order by rating desc