
import math

def cal_location_and_bandwith(lab, out_list):
    n_size=275
    c = math.ceil(n_size/2)
    for s in range(0,n_size+1):
        for l in range(1,n_size+1):
            if l>= n_size - s:
                break
            if l-1 <= c:
                riv = n_size*(l-1) + s
            else:
                riv = n_size*(n_size-l+1) + (n_size -1-s)
            if riv == lab:
                out_list[0]=s
                out_list[1]=l
                break


def cal_sliv(sliv, out_list):
    for s in range(0,14):
        for l in range(1,15):
            if l<= 14 - s:
                if l-1 <= 7:
                    sliv_tmp = 14*(l-1) + s
                else:
                    sliv_tmp = 14*(14-l+1) + (14-1-s)
                if sliv == sliv_tmp:
                    if out_list[2] == 0:
                        if s in (0,1,2,3):
                            if l >=3 and l <= 14:
                                out_list[0]=s
                                out_list[1]=l
                                break
                    else:
                        if s>=0 and s <= 12:
                            if l in (2,4,7):
                                out_list[0]=s
                                out_list[1]=l
                                break


def cal_dmrs_pos(input_para):
    l = 0
    l0 = 0
    if input_para['alloc_type'] == 0:
        l = input_para['start_symbol']
        if input_para['dmrs_typeA_pos'] == 2:
            l0 = 3
        else:
            l0 = 2
    if input_para['alloc_type'] == 1:
        l = input_para['start_symbol']
        l0 = 0
    #single symbol
    if input_para['dmrs_length'] == 0:
        #type a
        if input_para['alloc_type'] == 0:
            if input_para['add_dmrs_pos'] == 0:
                 input_para['dmrs_pos_list'].append(l0)
            if input_para['add_dmrs_pos'] == 1:
                input_para['dmrs_pos_list'].append(l0)
                if input_para['symbol_length'] >= 7:
                    if input_para['symbol_length']  in (8,9):
                        input_para['dmrs_pos_list'].append(7)
                    if input_para['symbol_length']  in (10,11,12):
                        input_para['dmrs_pos_list'].append(9)
                    if input_para['symbol_length']  in (13,14):
                        input_para['dmrs_pos_list'].append(11)
            if input_para['add_dmrs_pos'] == 2:
               input_para['dmrs_pos_list'].append(l0)
               if input_para['symbol_length'] >= 7:
                   if input_para['symbol_length']  in (8,9):
                       input_para['dmrs_pos_list'].append(7)
                   if input_para['symbol_length']  in (10,11,12):
                       input_para['dmrs_pos_list'].append(6)
                       input_para['dmrs_pos_list'].append(9)
                   if input_para['symbol_length']  in (13,14):
                       input_para['dmrs_pos_list'].append(7)
                       input_para['dmrs_pos_list'].append(11)
            if input_para['add_dmrs_pos'] == 3:
               input_para['dmrs_pos_list'].append(l0)
               if input_para['symbol_length'] >= 7:
                   if input_para['symbol_length']  in (8,9):
                       input_para['dmrs_pos_list'].append(7)
                   if input_para['symbol_length']  in (10,11):
                       input_para['dmrs_pos_list'].append(6)
                       input_para['dmrs_pos_list'].append(9)
                   if input_para['symbol_length']  in (12,13,14):
                       input_para['dmrs_pos_list'].append(5)
                       input_para['dmrs_pos_list'].append(8)
                       input_para['dmrs_pos_list'].append(11)
        #type b
        if input_para['alloc_type'] == 1:
            if input_para['add_dmrs_pos'] == 0:
                 input_para['dmrs_pos_list'].append(l0)
            if input_para['add_dmrs_pos'] == 1:
                input_para['dmrs_pos_list'].append(l0)
                if input_para['symbol_length'] in (6,7):
                    input_para['dmrs_pos_list'].append(4)

    #dmrs length =2
    if input_para['dmrs_length'] == 1:
        #type a
        if input_para['alloc_type'] == 0:
            if input_para['add_dmrs_pos'] == 0:
                input_para['dmrs_pos_list'].append(l0)
                input_para['dmrs_pos_list'].append(l0+1)
            if input_para['add_dmrs_pos'] == 1:
                input_para['dmrs_pos_list'].append(l0)
                input_para['dmrs_pos_list'].append(l0+1)
                if input_para['symbol_length'] >= 10:
                    if input_para['symbol_length']  in (10,11,12):
                        input_para['dmrs_pos_list'].append(8)
                        input_para['dmrs_pos_list'].append(9)
                    if input_para['symbol_length']  in (13,14):
                        input_para['dmrs_pos_list'].append(10)
                        input_para['dmrs_pos_list'].append(11)

out_warning_str_list = [
    "",
    "SLIV is wrong Number or not match allocation type!",
    "Alloction Type B not allowed add dmrs pos2 and pos3!",
    "Double symbol dmrs not allowed with add dmrs pos2 and pos3!",
    "Symbol length little than 4,not allowed with 2 symbol dmrs! ",
    "PUSCH slot PDCCH symbol should be zero!",
    "PDSCH overlap with PDCCH symbol!",
]



def cal_input_grid_valid(input_para):

    if input_para['start_symbol'] == "Invalid Input" or input_para['symbol_length'] == "Invalid Input":
        return 1

    if input_para['alloc_type'] == 1 and input_para['add_dmrs_pos'] in (2,3):
        return 2

    if input_para['dmrs_length'] == 1 and input_para['add_dmrs_pos'] in (2,3):
        return 3

    if input_para['dmrs_length'] == 1 and input_para['symbol_length'] < 4:
        return 4

    if input_para['pxsch'] == 1 and input_para['pdcch_symbol'] != 0:
        return 5

    if input_para['pxsch'] == 0 and input_para['pdcch_symbol'] != 0:
        if input_para['start_symbol'] < input_para['pdcch_symbol']:
            return 6

    return 0
