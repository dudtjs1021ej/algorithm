// 10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 
// 단 재귀함수를 이용해서 출력해야 합니다.
var answer = ""
func dfs(_ n: Int) {
    if n == 0 {
        return 
    }
    else {
        answer += "\(n%2)"
        dfs(n%2)
    }
}

let value = readLine()
dfs(value)