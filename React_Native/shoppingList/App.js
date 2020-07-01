// Import dependencies
import React, { useState } from 'react';

// Import Native Mobile components that replace HTML
import { View, Text, Image, StyleSheet } from 'react-native';

// Functional Component

const App = () => {
  return(
    <View style={styles.container}>
      <Text style={styles.text}>Hi!</Text>
      <Image source={{uri: 'https://i.pinimg.com/originals/88/be/89/88be897e9e200295c93149867a35d45f.jpg'}} style={styles.img} />
    </View>
  )
}

export default App;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  text: {
    color: 'skyblue',
    fontSize: 30
  },
  img: {
    width: 100,
    height: 100,
    borderRadius: 100/2, // Can't use percentages
  }

})