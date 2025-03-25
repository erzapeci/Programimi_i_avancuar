const request = require('supertest');
const app = require('../../src/app');

describe('Product API Routes', () => {
  const validApiKey = 'test-api-key';

  describe('GET /api/products', () => {
    it('should return 401 if no API key is provided', async () => {
      const res = await request(app).get('/api/products');
      expect(res.statusCode).toBe(401);
    });

    it('should return a list of products with valid API key', async () => {
      const res = await request(app)
        .get('/api/products')
        .set('X-API-Key', validApiKey);
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('products');
      expect(Array.isArray(res.body.products)).toBe(true);
    });

    it('should return 401 if an invalid API key is provided', async () => {
      const res = await request(app)
        .get('/api/products')
        .set('X-API-Key', 'invalid-key');
      expect(res.statusCode).toBe(401);
    });

    it('should return products with pagination parameters', async () => {
      const res = await request(app)
        .get('/api/products')
        .set('X-API-Key', validApiKey)
        .query({ limit: 10, offset: 0 });
      expect(res.statusCode).toBe(200);
      expect(res.body).toHaveProperty('products');
      expect(Array.isArray(res.body.products)).toBe(true);
      expect(res.body.products.length).toBeLessThanOrEqual(10);
    });

    it('should update a product with valid API key', async () => {
      const updatedProduct = { price: 89.99, stockCount: 25 };
      
      const res = await request(app)
        .put('/api/products/1')
        .set('X-API-Key', validApiKey)
        .send(updatedProduct);
        
      expect(res.statusCode).toBe(200);
      expect(Number.parseInt(res.body.id, 10)).toBe(1);
      expect(res.body.price).toBe(updatedProduct.price);
      expect(res.body.stockCount).toBe(updatedProduct.stockCount);
    });

    it('should return 404 for updating a non-existing product', async () => {
      const updatedProduct = { price: 99.99, stockCount: 30 };
      
      const res = await request(app)
        .put('/api/products/999')  // Product ID does not exist
        .set('X-API-Key', validApiKey)
        .send(updatedProduct);
        
      expect(res.statusCode).toBe(404);
    });

    it('should return products filtered by price range', async () => {
      const res = await request(app)
        .get('/api/products')
        .set('X-API-Key', validApiKey)
        .query({ minPrice: 100, maxPrice: 150 });
        
      expect(res.statusCode).toBe(200);
      expect(Array.isArray(res.body.products)).toBe(true);
      expect(res.body.products.every(product => product.price >= 100 && product.price <= 150)).toBe(true);
    });

    it('should return products filtered by category', async () => {
      const res = await request(app)
        .get('/api/products')
        .set('X-API-Key', validApiKey)
        .query({ category: 'electronics' });
        
      expect(res.statusCode).toBe(200);
      expect(Array.isArray(res.body.products)).toBe(true);
      expect(res.body.products.every(product => product.category === 'electronics')).toBe(true);
    });

    it('should create a new product with all required fields', async () => {
      const newProduct = {
        name: "Smart Watch",
        price: 199.99,
        category: "electronics",
        stockCount: 15
      };

      const res = await request(app)
        .post('/api/products')
        .set('X-API-Key', validApiKey)
        .send(newProduct);

      expect(res.statusCode).toBe(201);
      expect(res.body).toHaveProperty('id');
      expect(res.body.name).toBe(newProduct.name);
      expect(res.body.price).toBe(newProduct.price);
    });

    it('should delete a product with valid API key', async () => {
      const res = await request(app)
        .delete('/api/products/1')
        .set('X-API-Key', validApiKey);

      expect(res.statusCode).toBe(200);
      expect(res.body.message).toBe('Product deleted successfully');
    });
  });
});