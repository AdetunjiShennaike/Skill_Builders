var app = new Vue({
  // Options of the Vue instance
  el:'#app', //el = element property
  // Data are things that can be put into the html file via referencing
  data: {
    brand: 'Naughty',
    product: 'Socks',
    selectedVariant: 0,
    details: ['80% cotton', '20% polyester', 'gender-neutral'],
    variants: [
      {
        variantID: 2234,
        variantColor: 'green',
        variantImage: './vmSocks-green-onWhite',
        variantQuantity: 20
      },
      {
        variantID: 2235,
        variantColor: 'blue',
        variantImage: './vmSocks-blue-onWhite',
        variantQuantity: 0
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
    updateProduct: function(index) {
      this.selectedVariant = index
    }
  },
  // Cached value after the computation is done
  computed: {
    title() {
      return this.brand + '' + this.product
    },
    image() {
      return this.variants[this.selectedVariant].variantImage
    },
    inStock() {
      return this.variants[this.selectedVariant].variantQuantity
    }
    
  }

})