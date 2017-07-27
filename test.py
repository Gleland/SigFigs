import sigfigs


test_list=['100.0','-100.0','1000','01000.','01000.0','0.002','0.0020','0.00203','1203450','5420','-0.006700','0.06540','009009','90090']

for test in test_list: 
    print(test,"should be: ",sigfigs.count_sigfigs(test))



