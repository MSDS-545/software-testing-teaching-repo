const { expect } = require('chai');
const request = require('supertest');
const { createApp } = require('../src/app');

describe('integration/acceptance: shipping API', () => {
  it('returns a shipping quote through the HTTP interface', async () => {
    const response = await request(createApp())
      .get('/api/shipping')
      .query({ subtotal: 50, expedited: 'false' })
      .expect(200);

    expect(response.body).to.deep.equal({
      subtotal: 50,
      expedited: false,
      cost: 7.99,
    });
  });

  it('explains invalid input to the client', async () => {
    const response = await request(createApp())
      .get('/api/shipping')
      .query({ subtotal: 'abc' })
      .expect(400);

    expect(response.body.error).to.equal('subtotal must be a number');
  });
});
