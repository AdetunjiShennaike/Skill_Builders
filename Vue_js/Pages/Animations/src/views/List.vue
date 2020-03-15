<template>
  <div class="list">
    <input type="text" v-model="newContact" placeholder="Name" />
    <button @click="addContact">Add Contact</button>
    <button @click="sortContacts">Sort</button>

    <!-- Allows for multiple elements to inheret the transition stylign you want to add -->
    <!-- Appear applys a transistion on the initial render -->
    <transition-group tag="ul" name="slide-up" appear>
      <li v-for="element in contacts" :key="element">
        {{ element }}
      </li>
    </transition-group>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        newContact: '',
        contacts: ['Jose Consaico', 'Thomas Carver', 'John Wick']
      }
    },
    methods: {
      addContact() {
        this.contacts.push(this.newContact)
        this.newContact = ''
      },
      sortContacts() {
        this.contacts.sort()
      }
    }
  }
</script>