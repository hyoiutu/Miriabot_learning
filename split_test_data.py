print("type input data name")
input_name = input()
print("type output data name")
output_name = input()
with open(input_name, "r") as f:
    with open(output_name, "r") as g:
        input_data = f.readlines()
        output_data = g.readlines()
input_test_name = f"{input_name.split('.')[0]}_test.{input_name.split('.')[1]}"
output_test_name = f"{output_name.split('.')[0]}_test.{output_name.split('.')[1]}"
input_train_name = f"{input_name.split('.')[0]}_train.{input_name.split('.')[1]}"
output_train_name = f"{output_name.split('.')[0]}_train.{output_name.split('.')[1]}"
with open(input_test_name,"w") as f_test:
    with open(output_test_name,"w") as g_test:
        with open(input_train_name,"w") as f_train:
            with open(output_train_name, "w") as g_train:
                for i in input_data[:int(len(input_data)/10)]:
                    f_test.write(i)
                for i in output_data[:int(len(output_data)/10)]:
                    g_test.write(i)
                for i in input_data[int(len(input_data)/10):]:
                    f_train.write(i)
                for i in output_data[int(len(output_data)/10):]:
                    g_train.write(i)

