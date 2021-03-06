
var eventBus = new Vue()

Vue.component('product', {
  // Options for a vue component
  // Can pass props as an array or as an object to instill prop validation
  props: {
    premium: {
      type: Boolean,
      required: true
    }
  }, 
  // Template is written like a styled component, but used similar to python view templates
  template: `
    <div class="product">
      <div class="product-image">
        <!-- vbind: allows you to connect the attribute to data from the vue file-->
        <!-- shorthand for vbind since it is used so frequently is just : -->
        <img v-bind:src="image" > 
      </div>

      <div class="product-info">
        <!-- double brackets is an expression, just like django views -->
        <!-- computed properties can combine data to for a single reference -->
        <h1>{{ title }}</h1> 
        <!-- if-else statement using v-if/v-else. the if is linked to the data from the vue file -->
        <!-- else if also works -->
        <p v-if='inStock > 10'>In Stock</p>
        <p v-else-if='inStock <= 10 && inStock > 0'>Almost out of Stock</p>
        <p v-else>Out of Stock</p>
        <p>Shipping: {{ shipping }}</p>


        <ul>
          <!--  for loops are done with v-for and typed similar to python -->
          <li v-for='element in details'>{{ element }}</li>
        </ul>

        <!-- shorthand for event listeners/v-on is to use the @ -->
        <div v-for='(element, index) in variants' 
          :key='element.variantID'
          class="color-box"
          :style='{ backgroundColor: element.variantColor }'
          @mouseover='updateProduct(index)'
          >
        </div>

        <!--  event listeners can be made using v-on -->
        <button v-on:click='addToCart' 
          :disabled='inStock == 0'
          :class='{ disabledButton: inStock == 0 }'
          >Add to Cart</button>
      </div>

      <product-tabs :reviews='reviews'></product-tabs>

    </div>
  `,
  // Data are things that can be put into the html file via referencing
  data() {
    return {
      brand: 'Naughty',
      product: 'Socks',
      selectedVariant: 0,
      details: ['80% cotton', '20% polyester', 'gender-neutral'],
      variants: [
        {
          variantID: 2234,
          variantColor: 'green',
          variantImage: './vmSocks-green-onWhite.jpg',
          variantQuantity: 2
        },
        {
          variantID: 2235,
          variantColor: 'blue',
          variantImage: './vmSocks-blue-onWhite.jpg',
          variantQuantity: 0
        }
      ],
      reviews: []
    }
  },
  // Methods are used similar to class methods
  methods: {
    // Some browsers don't accept the add to cart format
    addToCart() {
      // Emitters allow for functions/methods to be used and have their values passed up to the parent
      // This can be done with $emit, you can pass data with a second value
      this.$emit('add-to-cart', this.variants[this.selectedVariant].variantID)
    },
    updateProduct: function(index) {
      this.selectedVariant = index
    },
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
    },
    shipping() {
      if(this.premium) {
        return 'Free'
      }
      return '$2.99'
    }
  },
  // Life Cycle Hook, init runtime once the component is mounted to the DOM
  mounted() {
    eventBus.$on('review-submitted', productReview => {
      this.reviews.push(productReview)
    })
  }

})


Vue.component('product-review', {
  template: `
    // The .prevent acts the same as preventDefault
    <form class='review-form' @submit.prevent='onSubmit'>

      <p v-if='errors.length'>
        <b>Please correct the following error(s):</b>
        <ul>
          <li v-for='error in errors'>{{ error }}</li>
        </ul>
      </p>

      <!-- Create a 2 way access to data by using v-model -->
      <!-- 2-way Data Binding -->
      <p>
        <label for='name'>Name: </label>
        <input v-model='name' id='name'>
      </p>

      <p>
        <label for='review'>Review: </label>
        <textarea v-model='review' id='review'></textarea>
      </p>

      <p>
        <label for='rating'>Rating: </label>
        <select v-model='rating' id='rating'>
          <option>5</option>
          <option>4</option>
          <option>3</option>
          <option>2</option>
          <option>1</option>
        </select>
      </p>

      <p>
        <input type='submit' value='Submit'>
      </p>

    </form>
  `,
  data() {
    return{
      name: null,
      review: null,
      rating: null,
      errors: []
    }
  },
  methods: {
    onSubmit() {
      if(this.name && this.review && this.rating){
        let productReview = {
          name: this.name,
          review: this.review,
          rating: this.rating
        }
        eventBus.$emit('review-submitted', productReview)
        this.name = null
        this.review = null
        this.rating = null
      }
      else{
        if(!this.name) this.errors.push('Name Required.')
        if(!this.review) this.errors.push('Review Required.')
        if(!this.rating) this.errors.push('rating Required.')
      }
    }
  }
})

Vue.component('product-tabs', {
  props: {
    reviews: {
      type: Array,
      required: true
    }
  },
  template:`
    <div>
      <span class='tab'
        :class='{ activeTab: selectedTab === tab }' 
        v-for='(tab, index) in tabs' 
        :key='index'
        @click='selectedTab = tab'>
        {{ tab }}
      </span>

      <div v-show="selectedTab == 'Reviews'">
        <p v-if='!reviews.length'>There are no reviews yet.</p>
        <ul>
          <li v-for='review in reviews'> 
            <p>{{ review.name }}</p>
            <p>Rating:{{ review.rating }}</p>
            <p>{{ review.review }}</p>
          </li>
        </ul>
      </div>

      <product-review v-show="selectedTab === 'Make a Review'"></product-review>
    </div>
  `,
  data() {
    return {
      tabs: ['Reviews', 'Make a Review'],
      selectedTab: 'Reviews'
    }
  }
})


var app = new Vue({
  // Options of the Vue instance
  el:'#app', //el = element property
  // Data are things that can be put into the html file via referencing
  data: {
    premium: true,
    cart: []
  },
  // Methods are used similar to class methods
  methods: {
    updateCart(id) {
      this.cart.push(id)
    }
  }
})