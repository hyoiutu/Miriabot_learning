import MeCab
from collections import defaultdict

base_dict_from_size=120000
base_dict_to_size=120000
extract_size=1000
fine_tuning_size=60000

inputs_path = "/home/fujiwalatex/tensorflowTutorial/translate/my_data_dir/fine_tuning/no_split_input.dat"
outputs_path = "/home/fujiwalatex/tensorflowTutorial/translate/my_data_dir/fine_tuning/no_split_output.dat"

base_inputs_path = f"/home/fujiwalatex/tensorflowTutorial/translate/my_data_dir/fine_tuning/vocab{base_dict_from_size}.from"
base_outputs_path = f"/home/fujiwalatex/tensorflowTutorial/translate/my_data_dir/fine_tuning/vocab{base_dict_to_size}.to"

tagger = MeCab.Tagger("-Owakati -d /home/fujiwalatex/mylex")


def count_words(file_name, isSplited=False):
    word_count_list = defaultdict(lambda: 0)
    with open(file_name, "r") as f:
        sentences = f.readlines()
    for i, sentence in enumerate(sentences):
        if isSplited:
            m = sentence
        else:
            m = tagger.parse(sentence)
        for j, word in enumerate(m.split(" ")):
            word_count_list[word] += 1
    return word_count_list


def extract_frequent_words(limit_num, file_name, base_file_name):
    word_count_list = count_words(file_name)
    if "\n" in word_count_list.keys():
        del word_count_list["\n"]
    with open(base_file_name, "r") as f:
        base_words = [line.replace("\n", "") for line in f.readlines()[:fine_tuning_size]]
    unique_word_count_list = {word: count for word, count in word_count_list.items() if word not in base_words}
    sorted_word_count_pair = sorted(unique_word_count_list.items(), key=lambda x:x[1], reverse=True)[:limit_num]
    return sorted_word_count_pair

input_target_words = [input_word[0] for input_word in extract_frequent_words(extract_size, inputs_path, base_inputs_path)]
output_target_words = [output_word[0] for output_word in extract_frequent_words(extract_size, outputs_path, base_outputs_path)]

with open(base_inputs_path, "r") as f:
    with open(base_outputs_path, "r") as g:
        base_inputs = [line.replace("\n", "") for line in f.readlines()][:fine_tuning_size - extract_size]
        base_outputs = [line.replace("\n", "") for line in g.readlines()][:fine_tuning_size - extract_size]

with open(f"vocab{fine_tuning_size}.from", "w") as f:
    with open(f"vocab{fine_tuning_size}.to", "w") as g:
        for input_word, output_word in zip(base_inputs + input_target_words, base_outputs + output_target_words):
            f.write(input_word + "\n")
            g.write(output_word + "\n")
