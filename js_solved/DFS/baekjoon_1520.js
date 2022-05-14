// 내리막 길
// https://www.acmicpc.net/problem/1520

'use strict'
const fs = require('fs')
const input = fs.readFileSync('data').toString().split('\n')

function main() {
  const [M, N] = readlineToNumArray()
  const board = getBoard(M)
  const dp = Array.from(Array(M), () => Array(N).fill(-1))

  function dfs(r, c) {
    if (r === M - 1 && c === N - 1) {
      return 1
    }
    const dr = [-1, 0, 1, 0]
    const dc = [0, 1, 0, -1]
    let result = 0
    for (let i = 0; i < 4; i += 1) {
      const nr = r + dr[i]
      const nc = c + dc[i]
      if (nr < 0 || nr >= M || nc < 0 || nc >= N) continue // 보드 범위를 벗어나는 경우
      if (board[nr][nc] >= board[r][c]) continue // 내리막길이 아닌 경우
      if (dp[nr][nc] >= 0) result += dp[nr][nc]
      else result += dfs(nr, nc)
    }
    dp[r][c] = result
    return result
  }

  console.log(dfs(0, 0))
}

function readlineToNumArray() {
  return input.shift().split(' ').map(num => Number(num))
}

function getBoard(row) {
  const result = Array(row)
  for (let i = 0; i < row; i += 1) {
    result[i] = readlineToNumArray()
  }
  return result
}

main()


