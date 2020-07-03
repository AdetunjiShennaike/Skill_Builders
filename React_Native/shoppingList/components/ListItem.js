// Import dependencies
import React from 'react';

// Import Native Mobile components that replace HTML
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

// Functional Component

const ListItem = ({item}) => {
  return(
    <TouchableOpacity style={styles.listItem}>
      <View style={styles.viewStyle}>
        <Text style={styles.text}>{item}</Text>
      </View>
    </TouchableOpacity>
  )
}

export default ListItem;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  listItem: {
    padding: 15,
    backgroundColor: 'grey',
    borderRadius: 5,
    borderColor: 'black',
    borderBottomWidth: 1,
    marginTop: 3,
    marginBottom: 3
  },
  viewStyle: {
    flexDirection: 'column',
    justifyContent: "center",
    alignItems: "center"
  },
  text: {
    color: 'white',
    fontSize: 18
  }
})
