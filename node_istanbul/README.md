# Node.js + Istanbul Testing Scenario

This example uses:

- **Mocha** as the test runner;
- **Chai** for assertions;
- **Supertest** for Express integration/acceptance tests;
- **nyc**, Istanbul's CLI, for code coverage.

Run:

```bash
npm install
npm test
npm run coverage
```

After `npm run coverage`, open `coverage/index.html` to inspect statement, branch, function, and line coverage.

### Classroom challenge

1. Run coverage.
2. Identify an uncovered branch.
3. Add exactly one test that covers it.
4. Re-run coverage.
5. Explain whether the new test improves confidence or only improves the percentage.
