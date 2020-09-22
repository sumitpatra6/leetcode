import mmh
class BloomFilter:
    def __init__(self, file_path, probability):
        self.probability = probability
        self.file_path = file_path
        self.words = None
        self.count = None
        self.bit_array_size  = self.get_bit_array_size()
        self.get_hash_count = self.get_hash_count()
        self.filter = [0]*self.bit_array_size
    
    def add_word_to_filter(self):
        for word in self.words:
            print("Adding word {}".format(word))
            for 

    @classmethod
    def get_words_from_file(self):
        fp = open(self.file_path, 'r')
        lines = fp.readlines()
        self.words = [line.strip('\n').strip('\r') for line in lines]
        self.count = len(self.words)


    @classmethod
    def get_bit_array_size(self):
        """
        Formula to get the bit array size
        m = -(n * lg(p)) / (lg(2)^2) 
        """
        size = -((self.count * math.log(self.probability)) / (math.log(2)**2))
        size = int(size)
        print("Bit array size {}".format(size))
        return size

    @classmethod
    def get_hash_count(self):
        """
        k = (m/n) * lg(2)
        """
        k = (self.bit_array_size / self.count) * math.log(2)
        k = int(k)
        print("Hash count {}".format(k))