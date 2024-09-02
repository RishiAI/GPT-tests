import React from 'react';
import { View, Text, Button } from 'react-native';
import * as ImagePicker from 'expo-image-picker';

export default function HomeworkScanner() {
  const [image, setImage] = React.useState(null);

  const pickImage = async () => {
    let result = await ImagePicker.launchCameraAsync();
    if (!result.canceled) {
      setImage(result.uri);
      // Send the image to the back-end for OCR processing
    }
  };

  return (
    <View>
      <Button title="Scan Homework" onPress={pickImage} />
      {image && <Text>Image selected!</Text>}
    </View>
  );
}
