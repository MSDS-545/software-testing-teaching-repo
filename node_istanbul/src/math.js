function shippingCost(subtotal, expedited = false) {
  if (subtotal < 0) throw new Error('subtotal cannot be negative');
  let cost = subtotal >= 75 ? 0 : 7.99;
  if (expedited) cost += 10;
  return Number(cost.toFixed(2));
}

module.exports = { shippingCost };
