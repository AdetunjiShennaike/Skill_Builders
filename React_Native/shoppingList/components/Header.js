// Import dependencies
import React from 'react';

// Import Native Mobile components that replace HTML
import { View, Text, StyleSheet } from 'react-native';

// Functional Component

const Header = (props) => {
  return(
    <View style={styles.header}>
      <Text style={styles.text}>{props.title}!</Text>
    </View>
  )
}

export default Header;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  header: {
    height: 60,
    padding: 15,
    backgroundColor: 'grey'
  },
  text: {
    color: 'white',
    fontSize: 23,
    textAlign: 'center',
  }
})
