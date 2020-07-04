// Import dependencies
import React, { useState } from 'react';
import Icon from 'react-native-vector-icons/dist/FontAwesome'

// Import Native Mobile components that replace HTML
import { View, Text, StyleSheet, TextInput, TouchableOpacity } from 'react-native';

// Functional Component

const AddItem = ({add}) => {
  const [text, setText] = useState('');

  const inputHandler = value => {
    setText(value)
  }

  return(
    <View style={styles.AddItem}>
      <TextInput placeholder='Add Item...' style={styles.input} onChangeText={inputHandler}/>
      <TouchableOpacity style={styles.btn} onPress={() => add(text)}>
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
