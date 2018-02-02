#!/bin/zsh
script_name=fine_tuning.py
screen_name=fine_tuning_for_Miria
data_dir=../my_data_dir/fine_tuning
train_dir=../my_model_dir/fine_tuning
from_train_data=${data_dir}/unique_input.dat
to_train_data=${data_dir}/unique_output.dat
from_dev_data=${data_dir}/unique_input.dat
to_dev_data=${data_dir}/unique_output.dat
from_vocab_size=120000
to_vocab_size=120000
fine_tuning_from_vocab_size=60000
fine_tuning_to_vocab_size=60000
layer_size=1024
decode_flag="FALSE"
save_graph_glag="TRUE"
num_layers=3
batch_size=64
use_half_fp="FALSE"
command_options="--data_dir=${data_dir} --train_dir=${train_dir} --from_train_data=${from_train_data} --to_train_data=${to_train_data} --from_dev_data=${from_dev_data} --to_dev_data=${to_dev_data}  --from_vocab_size=${from_vocab_size} --to_vocab_size=${to_vocab_size} --fine_tuning_from_vocab_size=${fine_tuning_from_vocab_size} --fine_tuning_to_vocab_size=${fine_tuning_to_vocab_size} --size=${layer_size} --num_layers=${num_layers} --batch_size=${batch_size} --use_fp16=${use_half_fp}"
while getopts ds opt
do
  case $opt in
    "d" ) decode_flag="TRUE";;
    "s" ) save_graph_flag="TRUE";;
    "*" ) echo "options error";;
  esac
done
if [ $decode_flag = "TRUE" ]; then
  echo python $script_name --decode $command_options
elif [ $save_graph_flag = "TRUE" ]; then
  echo python $sript_name --save_graph $command_options
else
  echo screen -S ${screen_name} python $script_name $command_options
fi
