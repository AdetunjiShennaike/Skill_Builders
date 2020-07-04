// Import dependencies
import React from 'react';
import Icon from 'react-native-vector-icons/dist/FontAwesome'

// Import Native Mobile components that replace HTML
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';

// Functional Component

const AddItem = (props) => {
  return(
    <View style={styles.AddItem}>
      <TextInput placeholder='Add Item..' style={styles.input} />
      <TouchableOpacity style={styles.btn}>
        <Text style={styles.btnText}>Add Item</Text>
      </TouchableOpacity>
    </View>
  )
}

export default AddItem;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  header: {
    height: 60,
    padding: 15,
    backgroundColor: 'skyblue'
  },
  text: {
    color: 'white',
    fontSize: 23,
    textAlign: 'center',
  }
})
