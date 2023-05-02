print('직원: 맥도날드입니다 주문하시겠습니까?')
answer_order = input()

if(answer_order == '네'):
    print('직원: 메뉴는 뭘로 해드릴까요?')
    while(True):
        print('\t<<MENU>>')
        print('빅맥\t\t\t5200원')
        print('맥스파이시상하이버거\t5900원')
        print('1955버거\t\t6500원')
        answer_menu = input()
        if(answer_menu == '빅맥' or answer_menu == '맥스파이시상하이버거' or answer_menu == '1955버거'):
            break
        else:
            print('직원: 다시 말씀해 주시겠습니까?')
    
    while(True):
        print('직원: 몇 개를 주문하시겠습니까?')
        how_many = int(input())
        if(1 <= how_many <= 5):
            break
        else:
            print('직원: 다시 한번 수량을 확인해 주세요')
    
    if(answer_menu == '빅맥'):
        cost = 5200
        time = 3
    elif(answer_menu == '맥스파이시상하이버거'):
        cost = 5900
        time = 4
    elif(answer_menu == '1955버거'):
        cost = 6500
        time = 5

    cost *= how_many
    time *= how_many
    print('직원: 총 {}원입니다. 예상 대기시간은 {}분 입니다.'.format(cost, time))

else:
    print('직원: 안녕히 가세요~~')

