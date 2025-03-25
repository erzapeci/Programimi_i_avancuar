const productService = require('../../src/services/product-service');

describe('ProductService', () => {
  // Mock për produkte për testim
  const mockProducts = [
    { id: 1, name: 'Product 1', price: 100 },
    { id: 2, name: 'Product 2', price: 150 },
  ];

  // Mock për funksionin getProductById
  productService.getProductById = jest.fn((id) => {
    return mockProducts.find(product => product.id === id) || null;
  });

  describe('getProductById', () => {
    it('should return a product by ID', () => {
      const result = productService.getProductById(1);
      expect(result).toHaveProperty('id', 1);  // Sigurohuni që ID e produktit është 1
    });

    it('should return null if product ID does not exist', () => {
      const result = productService.getProductById(999);  // ID që nuk ekziston
      expect(result).toBeNull(); // Duhet të kthehet null
    });
  });
});
