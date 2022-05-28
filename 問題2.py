# -*- coding: utf-8 -*-
"""
Created on Sun May 29 02:47:34 2022

@author: syuny
"""

def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    n=len(sorted_array)
    left = 0
    right = n-1  #探索範囲の初期値
    
    while left <= right:
        mid = (left + right) // 2   #配列の中間のindex(整数値)を求める
        
        if sorted_array[mid] == target_number:
            return mid  #中央の値と一致した場合にindexを返す
        
        elif sorted_array[mid] < target_number:
            left = mid + 1  #中央の値より大きい場合は探索範囲の左を変える
            
        else:
            right = mid - 1  #中央の値より小さい場合は探索範囲の右を変える

    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()