// Import dependencies
import React from 'react';
import Icon from 'react-native-vector-icons/dist/FontAwesome'

// Import Native Mobile components that replace HTML
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';

// Functional Component

const AddItem = (props) => {
  return(
    <View style={styles.AddItem}>
      <TextInput placeholder='Add Item...' style={styles.input} />
      <TouchableOpacity style={styles.btn}>
        <Text style={styles.btnText}> <Icon name='plus' size={20} /> Add Item</Text>
      </TouchableOpacity>
    </View>
  )
}

export default AddItem;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  input: {
    height: 60,
    padding: 15,
    fontSize: 16
  },
  btn: {
    backgroundColor: 'green',
    padding: 9,
    margin: 5
  }, 
  btnText: {
    color: 'white',
    fontSize: 20,
    textAlign: 'center',
  }
})
