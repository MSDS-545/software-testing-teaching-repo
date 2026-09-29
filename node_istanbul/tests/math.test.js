const { expect } = require('chai');
const { shippingCost } = require('../src/math');

describe('unit: shippingCost', () => {
  it('gives free standard shipping at the threshold', () => {
    expect(shippingCost(75)).to.equal(0);
  });

  it('adds the expedited fee', () => {
    expect(shippingCost(75, true)).to.equal(10);
  });

  it('rejects negative subtotal', () => {
    expect(() => shippingCost(-1)).to.throw('subtotal cannot be negative');
  });
});
