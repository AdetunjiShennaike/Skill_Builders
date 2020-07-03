// Import dependencies
import React, { useState } from 'react';

// Import Native Mobile components that replace HTML
import { View, Text, Image, StyleSheet } from 'react-native';

// Functional Component

const Header = () => {
  return(
    <View style={styles.header}>
      <Text style={styles.text}>Shopping List!</Text>
    </View>
  )
}

export default Header;

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
