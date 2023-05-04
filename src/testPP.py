from audioop import mul
import multiprocessing
import time

class Process(multiprocessing.Process):
  def __init__(self, id):
    super(Process, self).__init__()
    self.id = id

  def run(self):
    time.sleep(1)
    print("I'm the process with id: {}".format(self.id))


def square(x: int):
  return x*x


if __name__ == '__main__':
  # p = Process(0)
  # p.start()
  # p.join()
  pool = multiprocessing.Pool()
  inputs = [0,1,2,3,4]
  outputs = pool.map(square, inputs)

  