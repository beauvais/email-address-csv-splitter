# email-address-csv-splitter

## Splitting columns for email address CSVs

This is a quick and dirty hack to quickly split email address columns in a csv. I use it to split out the first and last names of people in a list – when moving from one email service to another, for example.

The premise is that some lists use:

```csv
"Name","Email Address"
```

This gives you:

| Name      | Email Address          |
|:--------- |:---------------------- |
|Joe Bloggs | Joe.bloggs@example.com |

Others use:

```csv
"First Name","Last Name","Email Address"
```

This lets you use first and last names.

| First Name | Last Name | Email Address          |
|:---------- |:--------- | :----------------------|
|Joe         | Bloggs    | Joe.bloggs@example.com |

## Python file

The python file is called column_split.py, and lives in the /docs directory.

It's short, and doesn't require any specified modules. It opens, iterates, and writes to a new csv file.

```python
with open('list.csv') as original_list:
    with open('new_list.csv', 'w') as new_list:
        for row in original_list:
            new_list.write('","'.join(row.split(' ')))
original_list.close()
new_list.close()
```

That's it. Just modify the variables to change your original and new files.

```python
with open('list.csv') as original_list: #change list.csv to your existing csv
    with open('new_list.csv', 'w') as new_list:
        for row in original_list:
            new_list.write('","'.join(row.split(' ')))
original_list.close()
new_list.close()
```


