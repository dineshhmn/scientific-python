import requests as rq
import matplotlib.pyplot as plt

def letter_freq(words):
    ret_val = {}
    for x in words:
        for c in x:
            if c in ret_val.keys():
                ret_val[c] += 1
            else:
                ret_val[c] = 1
    fig = plt.figure()
    fig.set_figwidth(15)
    tot = sum(ret_val.values())
    ret_prob = [x/tot for x in ret_val.values()]
    plt.bar(ret_val.keys(), ret_val.values(), color="red")
    plt.show()
    fig2 = plt.figure()
    fig2.set_figwidth(15)
    plt.bar(ret_val.keys(), ret_prob, color="green")
    plt.show()

def start_job():
    rq_obj = rq.get('http://www.gutenberg.org/files/35/35-0.txt')
    print(rq_obj.status_code)
    data = rq_obj.text
    words = data.split()
    letter_freq(words)
    # word_len = [len(x) for x in words]
    # plt.hist(word_len, bins=30)
    # plt.show()

if __name__ == "__main__":
    start_job()