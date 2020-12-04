###Convolutional Neural Network

I perfromed experiments on CNN to get the best possible parrameters

CNN design using Keras

Python provides us with the TensorFlow and Keras library
which has many inbuilt algorithms. In this project, we will be
using the Conv2D model in Keras library.
First, a sequential model of alternating convolution layer
and pooling layer is defined. In this project, we will use 3
Convolutional layers and 2 maxpooling layers. The parameters
of 1st Convolution layer will be the number of filters, size
of the convolution window, activation function(ReLU will
be used in this project) and size of the input image. The
maxpooling layer will have parameters like the size of the
window and the activation function. The later convolution
layer will have parameters: number of Filters, and activation
function.
Two Dense layers are added at the end of which the last
layer will be having softmax activation function for classification.
Afterward, the model is compiled using compile
function which takes up three parameters: optimizer, loss, and
metrics. The optimizer controls the learning rate. To measure
the accuracy, we use metric as accuracy.
The model is then trained using images and labels. The fit
function is called for this purpose, which takes up parameters:
images, labels, epochs, batch size, etc.
And finally, the model is evaluated using the evaluate
function, whose output is classification loss and accuracy.
