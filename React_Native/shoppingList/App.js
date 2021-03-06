// Import dependencies
import React, { useState } from 'react';
import uuid from 'uuid'

// Import Native Mobile components that replace HTML
import { View, Alert, Image, StyleSheet, FlatList } from 'react-native';

// Import components
import Header from './components/Header'
import ListItem from './components/ListItem'
import AddItem from './components/AddItem'

// Functional Component

const App = () => {
  const [items, setItems] = useState([
    {id: uuid(), text: 'Veggies' },
    {id: uuid(), text: 'Cereal' },
    {id: uuid(), text: 'Milk' },
    {id: uuid(), text: 'Chocolate' }
  ])

  const delItem = id => {
    setItems(prevItems => {
      return prevItems.filter(item => item.id != id)
    })
  }

  const add = item => {
    if(!item) {
      Alert.alert('Error', 'Please Enter an Item!', [{text: 'Ok'}], {cancelable: false}) 
      // First string is the title and second string is the message and the third value is what the button(s) should display <-- has to be an array
    }
    else {
      setItems(prevItems => {
        return [{id: uuid(), text: item}, ...prevItems]
      })
    }
  } 

  return(
    <View style={styles.container}>
      <Header title='Shopping List' />
      <AddItem add={add} />
      <FlatList data={items} renderItem={({item}) => <ListItem item={item} del={delItem} />} />
      {/* <Image source={{uri: 'https://i.pinimg.com/originals/88/be/89/88be897e9e200295c93149867a35d45f.jpg'}} style={styles.img} /> */}
    </View>
  )
}

export default App;

// Styling for Mobile components, similar to styled components
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 60,

  },
  img: {
    width: 100,
    height: 100,
    borderRadius: 100/2, // Can't use percentages
  }

})
