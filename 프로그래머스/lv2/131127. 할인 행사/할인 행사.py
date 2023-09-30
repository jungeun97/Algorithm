def solution(want, number, discount):
    answer = 0
    n = len(discount)
    for i in range(n-9):
        cart = {}
        for k in range(len(want)):
            cart[want[k]] = number[k]
        for j in range(i, i + 10):
            if discount[j] in cart:
                if cart[discount[j]] > 0:
                    cart[discount[j]] -= 1
        if sum(cart.values()) == 0:
            answer += 1
    return answer