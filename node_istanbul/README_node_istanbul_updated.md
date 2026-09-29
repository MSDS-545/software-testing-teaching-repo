# Node.js + Istanbul Testing Scenario

This example demonstrates **unit testing, integration testing,
acceptance testing, and code coverage** for a small Node.js/Express
application.

The testing stack uses:

-   **Mocha** as the test runner;
-   **Chai** for assertions;
-   **Supertest** for Express integration and acceptance tests;
-   **nyc**, Istanbul's command-line interface, for JavaScript code
    coverage.

------------------------------------------------------------------------

## 1. Install the Dependencies

From this example's directory, run:

``` bash
npm install
```

This installs the dependencies listed in `package.json`.

------------------------------------------------------------------------

## 2. Run the Tests

Run the complete JavaScript test suite:

``` bash
npm test
```

Mocha executes the tests and reports which tests passed or failed.

Depending on the scripts defined in `package.json`, the terminal output
may look similar to:

``` text
passing
failing
```

The important question at this stage is:

> **Did the expected application behavior pass the automated tests?**

------------------------------------------------------------------------

## 3. Understanding the Test Levels

### Unit Testing

A **unit test** checks one small piece of JavaScript behavior
independently.

Examples include:

-   testing a single function;
-   testing a calculation;
-   testing validation logic;
-   testing normal and edge-case inputs.

The main question is:

> **Does this individual unit of code work correctly?**

------------------------------------------------------------------------

### Integration Testing

An **integration test** checks whether multiple application components
work together.

For an Express application, Supertest can send requests to the Express
application without requiring students to manually start a separate
server.

Examples include:

-   sending a request to an Express route;
-   checking the returned HTTP status code;
-   checking the returned JSON;
-   verifying that a route and its application logic work together.

The main question is:

> **Do the connected components work correctly together?**

------------------------------------------------------------------------

### Acceptance Testing

An **acceptance test** verifies observable behavior from the perspective
of a user, client, or stakeholder.

For an API, this may include:

``` text
Given an API endpoint exists
When a client sends a valid request
Then the expected response is returned
```

The main question is:

> **Does the application satisfy the expected externally visible
> behavior?**

------------------------------------------------------------------------

## 4. Run Code Coverage with Istanbul/NYC

Run:

``` bash
npm run coverage
```

`nyc` instruments the application while the tests run and reports which
portions of the source code were executed.

A typical coverage summary contains:

  -----------------------------------------------------------------------
  Coverage measurement                Meaning
  ----------------------------------- -----------------------------------
  **Statements**                      Percentage of executable JavaScript
                                      statements executed

  **Branches**                        Percentage of alternative decision
                                      paths executed

  **Functions**                       Percentage of functions called by
                                      the tests

  **Lines**                           Percentage of source-code lines
                                      executed
  -----------------------------------------------------------------------

Coverage is useful for finding application logic that the current test
suite does not exercise.

> **Coverage measures execution, not correctness.** A high coverage
> percentage does not automatically mean that the tests contain
> meaningful assertions or that all requirements have been tested.

------------------------------------------------------------------------

## 5. View the HTML Coverage Report

After running:

``` bash
npm run coverage
```

Istanbul/NYC generates an HTML report under:

``` text
coverage/
└── index.html
```

Open the report on macOS:

``` bash
open coverage/index.html
```

Open the report on Windows:

``` powershell
start coverage/index.html
```

The HTML report provides a visual view of:

-   statement coverage;
-   branch coverage;
-   function coverage;
-   line coverage;
-   individual source files;
-   covered code;
-   uncovered code.

Students can click an individual source file to see which parts of the
implementation were executed by the tests.

------------------------------------------------------------------------

## 6. Why Branch Coverage Matters

Consider:

``` javascript
function getStatus(score) {
  if (score >= 70) {
    return "on-track";
  }

  return "needs-support";
}
```

A test using only:

``` javascript
getStatus(80);
```

executes the function, but it does not test the `"needs-support"`
branch.

A second test using a score below `70` would exercise the alternative
path.

This is why students should look beyond the overall coverage percentage
and inspect **branch coverage** and the uncovered code shown in the HTML
report.

------------------------------------------------------------------------

## 7. Recommended Testing and Reporting Workflow

Use this sequence when working with the example:

``` bash
npm install
npm test
npm run coverage
```

Then open:

``` text
coverage/index.html
```

On macOS:

``` bash
open coverage/index.html
```

The workflow can be interpreted as:

``` text
Source Code
    |
    v
Automated Tests
    |
    v
Mocha Test Results
    |
    v
Istanbul / NYC Coverage
    |
    +--> Terminal Coverage Summary
    |
    +--> coverage/index.html
          |
          +--> Statements
          +--> Branches
          +--> Functions
          +--> Lines
          +--> Uncovered Code
```

------------------------------------------------------------------------

## 8. Dependency and Security Checks

You can inspect the installed testing dependencies with:

``` bash
npm ls mocha diff serialize-javascript
```

Check whether packages have newer versions:

``` bash
npm outdated
```

Run the npm security audit:

``` bash
npm audit
```

If Mocha needs to be updated:

``` bash
npm install --save-dev mocha@latest
```

Then verify the application again:

``` bash
npm audit
npm test
npm run coverage
```

### About `npm audit fix --force`

Avoid using this as the first response to an audit warning:

``` bash
npm audit fix --force
```

The `--force` option can install dependency versions containing breaking
changes.

A better teaching workflow is:

``` text
npm audit
    |
    v
Identify the vulnerable dependency
    |
    v
Determine whether it is direct or transitive
    |
    v
Update the parent/direct dependency when appropriate
    |
    v
npm test
    |
    v
npm run coverage
    |
    v
npm audit
```

Students should verify that dependency updates do not break the
application or its tests.

------------------------------------------------------------------------

## 9. Classroom Coverage Challenge

1.  Run the complete test suite:

    ``` bash
    npm test
    ```

2.  Generate coverage:

    ``` bash
    npm run coverage
    ```

3.  Open:

    ``` text
    coverage/index.html
    ```

4.  Select one source file.

5.  Identify an uncovered statement or branch.

6.  Determine what behavior is missing from the current tests.

7.  Add **exactly one meaningful test** that exercises that behavior.

8.  Re-run:

    ``` bash
    npm test
    npm run coverage
    ```

9.  Reopen or refresh `coverage/index.html`.

10. Compare the before-and-after coverage.

11. Explain whether the new test:

-   improved confidence in the application's behavior;
-   only increased the coverage percentage; or
-   did both.

------------------------------------------------------------------------

## 10. What Students Should Be Able to Explain

After completing this example, students should be able to explain:

-   the difference between unit, integration, and acceptance testing;
-   why Supertest is useful for testing Express applications;
-   the role of Mocha as a test runner;
-   the role of Chai assertions;
-   the role of Istanbul/NYC in measuring code coverage;
-   the difference between statement, branch, function, and line
    coverage;
-   why 100% coverage does not necessarily mean the application is
    correct;
-   how an uncovered branch can identify a missing test scenario;
-   why dependency updates should be followed by another test and
    coverage run.

------------------------------------------------------------------------

## 11. Quick Command Reference

  ------------------------------------------------------------------------------
  Goal                                Command
  ----------------------------------- ------------------------------------------
  Install dependencies                `npm install`

  Run all tests                       `npm test`

  Generate coverage                   `npm run coverage`

  Open HTML coverage on macOS         `open coverage/index.html`

  Open HTML coverage on Windows       `start coverage/index.html`

  Check dependency vulnerabilities    `npm audit`

  Check outdated packages             `npm outdated`

  Inspect selected dependency         `npm ls mocha diff serialize-javascript`
  versions                            

  Update Mocha                        `npm install --save-dev mocha@latest`
  ------------------------------------------------------------------------------

------------------------------------------------------------------------

## Instructor Notes

The HTML coverage report is particularly useful during instruction
because students can move from an abstract coverage percentage to the
actual source code that was or was not executed.

When reviewing the report, ask:

1.  Did all tests pass?
2.  What percentage of statements was executed?
3.  What percentage of branches was executed?
4.  Which functions or lines were missed?
5.  Why was that code not reached?
6.  What test would exercise the missing behavior?
7.  Would adding that test improve confidence, or merely increase the
    coverage percentage?

The goal is not simply to maximize coverage. The goal is to use coverage
information to identify meaningful gaps in the test suite.
