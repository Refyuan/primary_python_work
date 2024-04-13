sum_=0
for i in range(12345678,98765433):
    str_=str(i)
    index=str_.find('2')
    if index != -1:
        str_ = str_[index + 1:]
        index = str_.find('0')
        if index !=-1:
            str_=str_[index+1:]
            index= str_.find('2')
            if index != -1:
                str_ = str_[index + 1:]
                index = str_.find('3')
                if index != -1:
                    sum_+=1
                else:
                    continue
            else:
                continue
        else:
            continue
    else:
        continue
print(98765433-12345678-sum_)