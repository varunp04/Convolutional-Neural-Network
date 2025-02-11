from mlxtend.data import loadlocal_mnist
from tensorflow.keras.utils import to_categorical
import numpy as np
import classifier as algs

def s_cross_validate(K, x, y, Algorithm, parameters):
    all_acc = np.zeros((len(parameters), K))
    
    num_val_sam =len(x) // K

    xblock0 = np.zeros((num_val_sam,28,28,1)); xblock2 = np.zeros((num_val_sam,28,28,1)); 
    xblock3 = np.zeros((num_val_sam,28,28,1)); xblock4 = np.zeros((num_val_sam,28,28,1));
    xblock5 = np.zeros((num_val_sam,28,28,1)); xblock6 = np.zeros((num_val_sam,28,28,1)); 
    xblock7 = np.zeros((num_val_sam,28,28,1)); xblock8 = np.zeros((num_val_sam,28,28,1));
    xblock9 = np.zeros((num_val_sam,28,28,1)); xblock1 = np.zeros((num_val_sam,28,28,1));

    yblock0 = np.zeros((num_val_sam,10)); yblock2 = np.zeros((num_val_sam,10)); 
    yblock3 = np.zeros((num_val_sam,10)); yblock4 = np.zeros((num_val_sam,10));
    yblock5 = np.zeros((num_val_sam,10)); yblock6 = np.zeros((num_val_sam,10)); 
    yblock7 = np.zeros((num_val_sam,10)); yblock8 = np.zeros((num_val_sam,10));
    yblock9 = np.zeros((num_val_sam,10)); yblock1 = np.zeros((num_val_sam,10));

    xblock0=xblock0.astype('float32')/255;xblock1=xblock1.astype('float32')/255;
    xblock2=xblock2.astype('float32')/255;xblock3=xblock3.astype('float32')/255;
    xblock4=xblock4.astype('float32')/255;xblock5=xblock5.astype('float32')/255;
    xblock6=xblock6.astype('float32')/255;xblock7=xblock7.astype('float32')/255;
    xblock8=xblock8.astype('float32')/255;xblock9=xblock9.astype('float32')/255;
    arrx = np.zeros(10)   ##block counter
    countx = np.zeros(10)     ##6000 counter

    x0=0;x1=0;x2=0;x3=0;
    x4=0;x5=0;x6=0;x7=0;
    x8=0;x9=0;
    #s = np.arange(x.shape[0])
    #np.random.shuffle(s)
    #x = x[s];
    #y = y[s];
    for i in range(len(x)):

        indx =np.where(y[i]==1)

        if(arrx[indx[0][0]] == 10):
            arrx[indx[0][0]] = 0
        z = int(arrx[indx[0][0]])
        if(countx[z] == 6000):
            while(countx[z] == 6000):
                arrx[indx[0][0]] = arrx[indx[0][0]] + 1
                if(arrx[indx[0][0]] == 10):
                    arrx[indx[0][0]] = 0
                z = int(arrx[indx[0][0]])
                if(countx[z] < 6000):
                    break;
        


        if(arrx[indx[0][0]] == 0):
            xblock0[x0] = x[i]
            yblock0[x0] = y[i]
            countx[0] = countx[0] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x0 = x0 + 1

        elif(arrx[indx[0][0]] ==1):
            xblock1[x1] = x[i]
            yblock1[x1] = y[i]
            countx[1] = countx[1] + 1 
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x1 = x1 + 1

        elif(arrx[indx[0][0]] == 2):
            xblock2[x2] = x[i]
            yblock2[x2] = y[i]
            countx[2] = countx[2] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x2 = x2 + 1

        elif(arrx[indx[0][0]] == 3):
            xblock3[x3] = x[i]
            yblock3[x3] = y[i]
            countx[3] = countx[3] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x3 = x3 + 1

        elif(arrx[indx[0][0]] == 4):
            xblock4[x4] = x[i]
            yblock4[x4] = y[i]
            countx[4] = countx[4] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x4 = x4 + 1

        elif(arrx[indx[0][0]] == 5):
            xblock5[x5] = x[i]
            countx[5] = countx[5] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x5 = x5 + 1

        elif(arrx[indx[0][0]] == 6):
            xblock6[x6] = x[i]
            yblock6[x6] = y[i]
            countx[6] = countx[6] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x6 = x6 + 1

        elif(arrx[indx[0][0]] == 7):
            xblock7[x7] = x[i]
            yblock7[x7] = y[i]
            countx[7] = countx[7] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x7 = x7 + 1

        elif(arrx[indx[0][0]] == 8):
            xblock8[x8] = x[i]
            yblock8[x8] = y[i]
            countx[8] = countx[8] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x8 = x8 + 1

        elif(arrx[indx[0][0]] == 9):
            xblock9[x9] = x[i]
            yblock9[x9] = y[i]
            countx[9] = countx[9] + 1
            arrx[indx[0][0]] = arrx[indx[0][0]] + 1
            x9 = x9 + 1   

    for k in range(K):
        if(k==0):
            val_data = xblock0
            val_label = yblock0

            train_data = np.concatenate((xblock1,xblock2,xblock3,xblock4,xblock5,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock1,yblock2,yblock3,yblock4,yblock5,yblock6,yblock7,yblock8,yblock9))
        elif(k==1):
            val_data = xblock1
            val_label = yblock1

            train_data = np.concatenate((xblock0,xblock2,xblock3,xblock4,xblock5,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock2,yblock3,yblock4,yblock5,yblock6,yblock7,yblock8,yblock9))
        elif(k==2):
            val_data = xblock2
            val_label = yblock2

            train_data = np.concatenate((xblock0,xblock1,xblock3,xblock4,xblock5,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock3,yblock4,yblock5,yblock6,yblock7,yblock8,yblock9))
        elif(k==3):
            val_data = xblock3
            val_label = yblock3

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock4,xblock5,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock4,yblock5,yblock6,yblock7,yblock8,yblock9))
        elif(k==4):
            val_data = xblock4
            val_label = yblock4

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock5,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock5,yblock6,yblock7,yblock8,yblock9))
        elif(k==5):
            val_data = xblock5
            val_label = yblock5

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock4,xblock6,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock4,yblock6,yblock7,yblock8,yblock9))
        elif(k==6):
            val_data = xblock6
            val_label = yblock6

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock4,xblock5,xblock7,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock4,yblock5,yblock7,yblock8,yblock9))
        elif(k==7):
            val_data = xblock7
            val_label = yblock7

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock4,xblock5,xblock6,xblock8,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock4,yblock5,yblock6,yblock8,yblock9))
        elif(k==8):
            val_data = xblock8
            val_label = yblock8

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock4,xblock5,xblock6,xblock7,xblock9))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock4,yblock5,yblock6,yblock7,yblock9))
        elif(k==9):
            val_data = xblock9
            val_label = yblock9

            train_data = np.concatenate((xblock0,xblock1,xblock2,xblock3,xblock4,xblock5,xblock6,xblock7,xblock8))
            train_label = np.concatenate((yblock0,yblock1,yblock2,yblock3,yblock4,yblock5,yblock6,yblock7,yblock8))
        print('Fold number: ',k)
        strain = np.arange(train_data.shape[0])
        np.random.shuffle(strain)
        train_data = x[strain];
        train_label = y[strain];

        stest = np.arange(val_data.shape[0])
        np.random.shuffle(stest)
        val_data = x[stest];

        val_label = y[stest];
        
        for i, params in enumerate(parameters):
            l = Algorithm(params)
            l.learn(train_data,train_label)
            acc = l.predict(val_data,val_label)
            print(acc)
            all_acc[i,k] = acc

    avg_acc = np.mean(all_acc, axis=1)
    std_acc = np.std(all_acc, axis=1)

    print('............avg_acc..........')
    print(avg_acc)
    print('............std_acc..........')
    print(std_acc)

    for i in range(all_acc.shape[0]):
        param = 'HP' + str(i+1) 
        plt.plot(x[i],label = param)
    plt.xticks(range(0,9))

    plt.title('Accuracy plot of different parameters vs each fold(0-9)')
    plt.xlabel('Folds')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()


    best_parameters = parameters[0]
    bestacc = avg_acc[0]
    for i, params in enumerate(parameters):
        if(avg_acc[i] > bestacc):
            bestacc = avg_acc[i]
            best_parameters = parameters[i]
    print(best_parameters)
    return best_parameters



if __name__ == '__main__':


    #data
    (x_train, y_train) = loadlocal_mnist(
        images_path ='E:/uofa/SEM2/ECE626/P#1/FMNIST/train-images-idx3-ubyte',
        labels_path ='E:/uofa/SEM2/ECE626/P#1/FMNIST/train-labels-idx1-ubyte'
        )
    (x_test, y_test) = loadlocal_mnist(
        images_path ='E:/uofa/SEM2/ECE626/P#1/FMNIST/t10k-images-idx3-ubyte',
        labels_path ='E:/uofa/SEM2/ECE626/P#1/FMNIST/t10k-labels-idx1-ubyte'
        )
    
    print(x_train.shape)
    
    classalgs = {
        'ConvNNet': algs.convnet
        }

    ## hyper-parameters
    parameters = {
        'ConvNNet' : [
                {'epochs':5,'batch_size':64,'filter1':64,'filter2':128,'filter3':128,'filter4':128},     
                {'epochs':5,'batch_size':128,'filter1':64,'filter2':128,'filter3':128,'filter4':128},
                {'epochs':10,'batch_size':128,'filter1':64,'filter2':128,'filter3':128,'filter4':128},
                {'epochs':10,'batch_size':64,'filter1':64,'filter2':128,'filter3':128,'filter4':128}
        ]
        }

    x_train = x_train.reshape((60000,28,28,1))
    x_train = x_train.astype('float32')/255
    x_test = x_test.reshape((10000,28,28,1))
    x_test = x_test.astype('float32')/255

    y_train = to_categorical(y_train)
    y_test = to_categorical(y_test)


    best_parameters = {}
    for learnername, learner in classalgs.items():
        print('running learner = ' + learnername)
        params = parameters.get(learnername)
        #best_parameters[learnername] = test_s(10, x_train, y_train, learner, params)
        best_parameters[learnername] = s_cross_validate(10, x_train, y_train, learner, params)   

    for learnername, Learner in classalgs.items():
        params = best_parameters[learnername]
        learner = Learner(params)
        #Training the model with best hyper parameters
        learner.learn(x_train, y_train)
        # Test model
        best_acc = learner.predict(x_test,y_test)
    print("BEST ACCURACY:",best_acc)

                