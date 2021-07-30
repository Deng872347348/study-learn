import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
class net(object):

    def __init__(self, iris, epoch, learn_rate, split):
        self.iris = iris
        self.data_split(split)
        self.learn_rate = learn_rate
        self.epoch = epoch
        self.hidden_weight = np.random.uniform(low=0, high=1, size=(5, 4))
        self.output_weight = np.random.uniform(low=0, high=1, size=(3, 5))
        self.hidden_bias = np.random.random(5)  # np.random.uniform(low=0, high=1, size=(1))
        self.output_bias = np.random.random(3)
        self.error = 0
        self.hit = 0
        self.accuracy = 0
        self.all_error = []
        self.all_accuracy = []

    def sigmoid(self, result):
        sigmoid = []
        for sum in result:
            sigmoid.append(1 / (1 + np.exp(-sum)))
        return sigmoid

    def prediction(self, sigmoid):
        self.output = []
        for x in sigmoid:
            if x < 0.5:
                o = 0
            else:
                o = 1
            self.output.append(o)
        return self.output

    def update_weights(self, iris, hidden_sigmoid, output_sigmoid):
        old_weights = self.output_weight.copy()
        for x, value in enumerate(self.output_weight):
            for y, _ in enumerate(value):
                self.output_weight[x][y] -= (output_sigmoid[x] - iris[4 + x]) * output_sigmoid[x] * (
                            1 - output_sigmoid[x]) * hidden_sigmoid[y] * self.learn_rate

        for x, value in enumerate(self.hidden_weight):
            for y, _ in enumerate(value):
                sum = 0
                for z in range(3):
                    sum += (output_sigmoid[z] - iris[4 + z]) * output_sigmoid[z] * (1 - output_sigmoid[z]) * \
                           old_weights[z][x]
                self.hidden_weight[x][y] -= sum * hidden_sigmoid[x] * (1 - hidden_sigmoid[x]) * iris[
                    y] * self.learn_rate

    def update_bias(self, iris, hidden_sigmoid, output_sigmoid):
        old_weights = self.output_weight.copy()
        for x, value in enumerate(self.output_bias):
            self.output_bias[x] -= (output_sigmoid[x] - iris[4 + x]) * output_sigmoid[x] * (
                        1 - output_sigmoid[x]) * self.learn_rate
        for x, value in enumerate(self.hidden_bias):
            sum = 0
            for z in range(3):
                sum += (output_sigmoid[z] - iris[4 + z]) * output_sigmoid[z] * (1 - output_sigmoid[z]) * old_weights[z][
                    x]
            self.hidden_bias[x] -= sum * hidden_sigmoid[x] * (1 - hidden_sigmoid[x]) * self.learn_rate

    def data_split(self, percentage):
        np.random.shuffle(self.iris)
        self.train_data = self.iris[:int((len(self.iris)) * percentage / 100)]
        self.test_data = self.iris[int((len(self.iris)) * percentage / 100):]

    def train(self, iris):
        self.error = 0
        for data in iris:
            summation = []
            for x, layer in enumerate(self.hidden_weight):
                summation.append(np.dot(data[:4], layer) + self.hidden_bias[x])
            hidden_sigmoid = self.sigmoid(summation)
            summation.clear()
            for x, layer in enumerate(self.output_weight):
                summation.append(np.dot(hidden_sigmoid, layer) + self.output_bias[x])
            output_sigmoid = self.sigmoid(summation)
            # print(output_sigmoid)
            for key, value in enumerate(output_sigmoid):
                self.error += pow(data[(4 + key)] - value, 2)
            # self.update_bias(data,  hidden_sigmoid, output_sigmoid)
            self.update_weights(data, hidden_sigmoid, output_sigmoid)
        self.all_error.append(self.error / 6)
        return self.error / 6

    def test(self, iris):
        self.hit = 0
        for data in iris:
            summation = []
            for x, layer in enumerate(self.hidden_weight):
                summation.append(np.dot(data[:4], layer) + self.hidden_bias[x])
            hidden_sigmoid = self.sigmoid(summation)
            summation.clear()
            for x, layer in enumerate(self.output_weight):
                summation.append(np.dot(hidden_sigmoid, layer) + self.output_bias[x])
            output_sigmoid = self.sigmoid(summation)
            # print(output_sigmoid)
            pred = [self.prediction(output_sigmoid)] + [data[-3:]]
            if np.all(pred[0] == pred[1]):
                self.hit += 1
        self.all_accuracy.append(self.hit / 30)
        return self.hit / 30

    def test_iris(self, data):
        self.hit = 0
        name = ["setosa","versicolor","virginica"]
        summation = []
        for x, layer in enumerate(self.hidden_weight):
            summation.append(np.dot(data[:4], layer) + self.hidden_bias[x])
        hidden_sigmoid = self.sigmoid(summation)
        summation.clear()
        for x, layer in enumerate(self.output_weight):
            summation.append(np.dot(hidden_sigmoid, layer) + self.output_bias[x])
        output_sigmoid = self.sigmoid(summation)
        # print(output_sigmoid)
        pred = [self.prediction(output_sigmoid)] + [data[-3:]]
        if pred[0][0]-pred[1][0]<0.1:
            print('the prediction is {}'.format(name[pred[0].index(max(pred[0]))]))
            print('the pred is correct')
        print(pred)

    def single_run(self):
        cur_error = self.train(self.train_data)
        cur_acc = self.test(self.test_data)
        return cur_error, cur_acc

    def run(self, data):
        np.random.shuffle(self.iris)
        for _ in range(self.epoch):
            self.cur_epoch = _
            cur_error, cur_acc = self.single_run()
            # print("current error is {}, and current accuracy is {}\n".format(cur_error, cur_acc))
        export = []
        self.plot(self.all_error, self.all_accuracy)
        export.append(self.all_error)
        export.append(self.all_accuracy)
        np.savetxt("log_training.csv", np.transpose(export), delimiter=",", header="Error, Accuracy")
        self.test_iris(data)

    def plot(self, error, accuracy):
        scale_error = np.log10(error)
        plt.figure(1)
        plt.plot(scale_error, color='blue', linewidth=2, label='error')
        plt.plot(accuracy, color='red', linewidth=2, label='accuracy')
        plt.title('Learning Rate ' + str(self.learn_rate))
        plt.xlabel('Epoch')
        plt.ylabel('Quantity')
        plt.legend()
        plt.savefig('result.png')

if __name__ == '__main__':
    path = Path(__file__).parents[0]
    file = "Iris3.csv"

    data = np.genfromtxt(file, skip_header=True, delimiter=',')

    mlp1 = net(data, 1000, 0.8, 80)  # data, epoch, k-fold, learning rate 0.1
    input = np.asarray([4.8,3,1.4,0.1,2,3,4])
    # uncomment one only
    mlp1.run(input)
