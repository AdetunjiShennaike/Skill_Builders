var app = new Vue({
  // Options of the Vue instance
  el:'#app', //el = element property
  data: {
    product: 'Socks',
    image: './vmSocks-green-onWhite',
    inventory: 100,
    details: ['80% cotton', '20% polyester', 'gender-neutral'],
    variants: [
      {
        variantID: 2234,
        variantColor: 'green'
      },
      {
        variantID: 2235,
        variantColor: 'blue'
      }
    ]
  }
})