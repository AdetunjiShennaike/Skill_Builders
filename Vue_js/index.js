var app = new Vue({
  // Options of the Vue instance
  el:'#app', //el = element property
  // Data are things that can be put into the html file via referencing
  data: {
    product: 'Socks',
    image: './vmSocks-green-onWhite',
    inStock:true,
    inventory: 100,
    details: ['80% cotton', '20% polyester', 'gender-neutral'],
    variants: [
      {
        variantID: 2234,
        variantColor: 'green',
        variantImage: './vmSocks-green-onWhite'
      },
      {
        variantID: 2235,
        variantColor: 'blue',
        variantImage: './vmSocks-blue-onWhite'
      }
    ],
    cart: 0
  },
  // Methods are used similar to class methods
  methods: {
    // Some browsers don't accept the add to cart format
    addToCart() {
      this.cart += 1
    },
    updateProduct: function(variantImage) {
      this.image = variantImage
    }
  }
})