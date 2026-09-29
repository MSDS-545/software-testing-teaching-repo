const express = require('express');
const { shippingCost } = require('./math');

function createApp() {
  const app = express();

  app.get('/health', (req, res) => res.json({ status: 'ok' }));

  app.get('/api/shipping', (req, res) => {
    const subtotal = Number(req.query.subtotal);
    const expedited = req.query.expedited === 'true';
    if (!Number.isFinite(subtotal)) {
      return res.status(400).json({ error: 'subtotal must be a number' });
    }
    try {
      return res.json({ subtotal, expedited, cost: shippingCost(subtotal, expedited) });
    } catch (err) {
      return res.status(400).json({ error: err.message });
    }
  });

  return app;
}

module.exports = { createApp };
