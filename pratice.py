import numpy as np
import matplotlib.pyplot as plt

import os


def get_ngrams(wordlist, n):
    ngrams = []
    ######################################################################
    #            wordlist로부터 n-gram(들)을 ngrams에 입력하기             #
    ######################################################################
    a = list(zip(*[wordlist[i:] for i in range(n)]))
    for i in a:
        ngrams.append(i)

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################
    return ngrams


def get_score_from_ngrams(ngrams1, ngrams2):
    count = 0
    ######################################################################
    #         ngrams2의 원소 개수가 ngrams1의 원소 개수보다 많으면,         #
    #                     ngrams1과 ngrams2를 교환하기                    #
    ######################################################################

    if len(ngrams2) > len(ngrams1):
        temp = []

        temp = ngrams2
        ngrams2 = ngrams1
        ngrams1 = temp

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################

    ######################################################################
    #          ngrams1의 각 원소별로 ngrams2의 모든 원소와 비교하여         #
    #                      같으면, count 1 증가하기                       #
    ######################################################################
    if np.array(ngrams1 == ngrams2):
        count = count + 1

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################
    return count / len(ngrams1)


def get_wordlist_from_file(filename):
    wordlist = []
    ######################################################################
    #  filename 파일의 모든 내용을 공백 단위로 분리하여 wordlist에 입력하기  #
    ######################################################################
    with open('txt_dir', 'r', encoding='utf-8') as f:
        for line in f:
            line = line[2:-1].split()
            wordlist.extend(line)

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################
    return wordlist


def get_filelist_from_directory():
    filelist = []
    ######################################################################
    #            이 파일이 있는 현재 위치의 txt_dir 폴더에 있는             #
    #            .txt 파일(들)의 파일명을 filelist에 입력하기              #
    ######################################################################
    filelist.append("reference.txt")
    filelist.append("submission1.txt")
    filelist.append("submission5.txt")
    filelist.append("submitted.txt")
    filelist.append("submitted2.txt")

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################
    return filelist


def main():
    n = None
    wordlists = []
    ngrams_list = []
    ######################################################################
    #                        정수 n 입력 받기(n: )                        #
    ######################################################################
    n = int(input("n: "))

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################

    filelist = get_filelist_from_directory()
    num_of_files = len(filelist)

    ######################################################################
    #     filelist를 이용하여 각 파일에 대한 get_word_list_from_file()     #
    #                    결과를 wordlists에 입력하기                      #
    ######################################################################
    wordlists.append(get_wordlist_from_file(filelist))

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################

    ######################################################################
    #          wordlists를 이용하여 각 원소에 대한 get_ngrams()            #
    #                    결과를 ngrams_list에 입력하기                    #
    ######################################################################
    ngrams_list.append(get_ngrams(wordlists))

    ######################################################################
    #                            코드 작성 끝                             #
    ######################################################################

    score_matrix = get_score_from_ngrams(ngrams_list)

    if (len(score_matrix) == 0):
        return

    for row in score_matrix:
        print(row)

    fig = plt.figure()
    ax = plt.gca()
    im = ax.matshow(np.array(score_matrix), interpolation='none')
    fig.colorbar(im)

    ax.set_xticks(np.arange(num_of_files))
    ax.set_xticklabels(filelist)
    ax.set_yticks(np.arange(num_of_files))
    ax.set_yticklabels(filelist)

    # Rotate and align top ticklabels
    plt.setp([tick.label2 for tick in ax.xaxis.get_major_ticks()], rotation=45,
             ha="left", va="center", rotation_mode="anchor")

    fig.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
