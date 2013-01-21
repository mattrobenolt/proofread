# Proofread
**Proofread** will allow you to add a quick layer of tests for your web project without actually writing any tests.

*Currently compatible with Django*

## Why do I need this?
A very common approach to testing is a layer of tests that just make sure your site is working by accessing the public urls. Proofread allows you to configure a list of urls that need to work and Proofread will do the rest.

Proofread is great and simple to get into your project without needing to fully understand how to write your own tests. It **Just Works™**.

This layer of testing yields a few immediate benefits:

 * It will surface a lot of missing `import` statements.
 * Will usually pick up general `SyntaxError`s.
 * Asserts that your public URLs are correct and will always be correct.

Proofread pairs well as a [`pre-commit`](#the-pre-commit-hook) hook to try and prevent some obvious mistakes.

## Installation
```
$ pip install proofread
```

Then add to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    # ...
    'proofread.contrib.django_proofread',
    # ...
)
```

## Configuration
The only configuration that needs to be done is telling Proofread which urls to test inside if your `settings.py`.

**PROOFREAD_SUCCESS**: List of paths that should return successfully. These should cover all of your public URLs

**PROOFREAD_FAILURES**: List of paths that should return `404 Not Found`. Good for testing a 404 page or a page that was explicitly removed.

**PROOFREAD_ENDPOINTS** *(advanced)*: A list of tuples that represent a raw request. All fields are optional except `path`: `(path, status, method, post_data)`

This configuration goes right inside your `settings.py`.

### Example:
```python
PROOFREAD_SUCCESS = (
    '/',  # Home page
    '/about/',  # Out About Us page
)

PROOFREAD_FAILURES = (
    '/404/', # Our 404 page should return a 404
)

PROOFREAD_ENDPOINTS = (
    ('/post/', 405, 'GET'),  # This should return a 405 on a GET request
    ('/secured', 403),  # Should return a 403
    ('/post/', 200, 'POST', {'foo': 'bar'}),  # Should handle some POST data
)
```

## Usage
After configuring which urls Proofread needs to check, you're ready to run your tests. Proofread acts just like normal Django tests, so you can just run:

```
$ python manage.py test
```

If you **only** want to run the tests that Proofread generates, you can run:

```
$ python manage.py proofread
```

### The `pre-commit` Hook
Proofread is designed to assist in preventing simple errors from getting caught before the code is even committed.

A git `pre-commit` hook is provided to try and help automate this process. A `pre-commit` hook is executed on your computer before the commit lands. If a test fails, git will reject your commit and you'll have to fix the broken code.

To install, run this snippet in the root of your git repository:

```
$ curl https://raw.github.com/mattrobenolt/proofread/master/hooks/pre-commit.example > .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit
```

**Note**: This will overwrite any existing `pre-commit` hook, if one exists.

## Other information
Proofread generates a dynamic test for each url. What that means, is that each url will product it's own success/failure separate from the rest with a name that indicates which endpoint was run and what the success code should have been.

## Example failure output
![](http://i.imgur.com/3p0747k.png)

## Questions or problems?
 * [Issue Tracker](https://github.com/mattrobenolt/proofread/issues)
 * [Yell at me on Twitter @mattrobenolt](https://twitter.com/mattrobenolt)
