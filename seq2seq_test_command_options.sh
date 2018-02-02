#!/bin/zsh

screen_name=streaming_tweets_training_for_Miria
data_dir=../my_data_dir/streaming
train_dir=../my_model_dir/streaming/fortest
from_train_data=${data_dir}/input_quarter_train.txt
to_train_data=${data_dir}/output_quarter_train.txt
from_dev_data=${data_dir}/input_quarter_test.txt
to_dev_data=${data_dir}/output_quarter_test.txt
from_vocab_size=2000
to_vocab_size=2000
layer_size=256
decode_flag="FALSE"
num_layers=2
batch_size=64
use_half_fp="FALSE"
command_options="--data_dir=${data_dir} --train_dir=${train_dir} --from_train_data=${from_train_data} --to_train_data=${to_train_data} --from_dev_data=${from_dev_data} --to_dev_data=${to_dev_data}  --from_vocab_size=${from_vocab_size} --to_vocab_size=${to_vocab_size} --size=${layer_size} --num_layers=${num_layers} --batch_size=${batch_size} --use_fp16=${use_half_fp}"
while getopts d opt
do
  case $opt in
    "d" ) decode_flag="TRUE";;
    "*" ) echo "options error";;
  esac
done
if [ $decode_flag = "TRUE" ]; then
  echo python translate.py --decode $command_options
else
  echo screen -S ${screen_name} python translate.py $command_options
fi
