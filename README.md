# CNN_Minecraft_Trees
Creator: Ruangyot Nanchiang  
Lecturer: Dr.Suradet Tantrairatn  

This project is to study about "Convolutional Neural Network".  
for ANN model coding: [Click here!](https://github.com/Rayato159/Minecraft_Tree)  

## Create Datasets
My inspriation is from "Minecraft". Then I pick types of tree to create datasets because they are random shape for each and easy to create a picture of tree by coding without drawing.  

Two types of tree I pick
1. [Oak](https://minecraft.fandom.com/wiki/Oak)  
2. [Spruce](https://minecraft.fandom.com/wiki/Spruce)  

I generate all images of tree by drawing and try some random by each types pattern with OpenCV and saved all images in ".npy" files.  
Left is "Oak" and Right is "Spruce". Sample here.  
![Sample](https://github.com/Rayato159/Minecraft_Tree/blob/main/sample.png)  

## Model
As I mention before, I used Convolutional Neural Network model. 
And I create a class "My model" to pack all layer of model stick together.  

```python
class MyModel:
    def __init__(self, X_train, X_test, y_train, y_test):
        ...
        #Layer_1
        self.CNN_model.add(Conv2D(16, (3,3), input_shape=(16,16,1)))
        self.CNN_model.add(Activation("relu"))
        self.CNN_model.add(MaxPooling2D(pool_size=(2,2)))
        
        #Layer_2
        self.CNN_model.add(Conv2D(16, (3,3)))
        self.CNN_model.add(Activation("relu"))
        self.CNN_model.add(MaxPooling2D(pool_size=(2,2)))
        
        #Layer_3
        self.CNN_model.add(Flatten())
        self.CNN_model.add(Dense(16))
        
        #Layer_4_output
        self.CNN_model.add(Dense(2))
        self.CNN_model.add(Activation("softmax"))
```
***This model is generate by trial and error.
## Fitting Model  
```python
CNN_model.fit(X_train, y_train, batch_size=20, epochs=5)
```
## Result
Accuracy score of this model = 1.0 (Score from test and unseen data).
