Convolutional Neural Network
Convolutional neural networks are used most of the time
in computer vision applications because of the high accuracy
in performance when compared to other machine learning
or Artificial Intelligence algorithms. CNNs takes an image
as input, then assign weights to the pixels for meaningful
information. CNNs have some parameters that can be handengineered
such as filters, pooling layers, activation function
on each layer, etc.
The connectivity pattern of CNNs are inspired by the
neurons of the human brain. Individual neurons respond to
stimuli only in a restricted region of the visual field. A
collection of such fields overlaps to cover the entire visual
area. 
CNNs were first used on the MNIST dataset by Lacun et
al. MNIST is the most widely used dataset for image
recognition applications. Lucan designed a CNN known as
LeNet-5 which consists of convolution layers with sigmoid
activation function and pooling layers as arithmetic mean.
At the convolution layer, the filtering process takes place.
An image can be divided into small pixels and each pixel
contains some information that will be useful for recognition.
Filtering is the process where a convolutional window of small
size(usually 3X3 pixel) moves from the top left corner of the
image towards the right, till it strides through complete width.
Then the window shifts down by 1 pixel and again strides
the image from left to right. Images are padded like a border
is added to the image, these paddings are helpful when the
pixels at the corner or edge are being dealt. This process is
repeated throughout the image. The filtering process is taking
a weighted sum of the neighboring pixels, this means one
window is assigned to one node of the neural net with all
the pixels in that window acting as inputs to the node and a
weighted sum is obtained as output.

where k is the feature map, l is the pixel location, w is
weight associated with that feature map, and A are the pixel
surrounding the pixel (i,j).
Using the filtering operation high level features such edges,
slants, etc. are extracted. The filtered image for a given
convolution window is called a feature map.
Then comes the pooling layer, which basically takes a
window (usually 2X2) and collapse all the pixels in it to one
pixel. Hence shrinking the image. In LeNet-5,[3] Lacun used
mean pooling layer.

After a consecutive layer of alternating Convolution and
pooling layers, finally, a fully connected Dense layer is added
to the network. This is a way of learning a non-linear combination
of high-level convolutional layers. Afterward, the image
is flattened to a column vector and fed to the feed-forward
neural network. And finally, the classification is done using
softmax classification.

A. Backpropogation Algorithm
The backpropagation algorithm is a gradient descent on a
non-convex objective, with a careful ordering of computation
to avoid repeating computation. In particular, one first propagates
forward and computes the activation function. Then the
error between the prediction and the actual error is calculated.
The gradient of this error(loss) to parameters is taken; in this
case, for efficient computation, the best ordering is to compute
the gradient to the last parameter first, i.e weight vector of the
last layer and then the weight vector of the layer before that.
This is the reason for the term backpropagation since the error
is propagated backward from the last layer first.
The weight vector associated with each convolutional window
in the convolution layer is updated using Backpropagation.
The Weighted sum is then calculated for each convolutional
window.
