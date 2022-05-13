// 섬의 개수
// https://www.acmicpc.net/problem/4963

'use strict'
const fs = require('fs');
// const N = fs.readFileSync('/dev/stdin').toString().split(' ');
const input = fs.readFileSync('data').toString().split('\n')

function main() {
  while (true) {
    const [column, row] = readlineToNumArray()
    if (row === 0 && column === 0) break
    const board = getBoard(row)
    console.log(landCounter(board, row, column))
  }
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

function dfs(board, visited, r, c, size) {
  const dr = [-1, -1, 0, 1, 1, 1, 0, -1]
  const dc = [0, 1, 1, 1, 0, -1, -1, -1]
  const [row, column] = size
  if (visited[r][c] === 1) return board
  board[r][c] = 0
  visited[r][c] = 1
  for (let i = 0; i < 8; i += 1) {
    const nr = dr[i] + r
    const nc = dc[i] + c
    if (nr < 0 || nr >= row || nc < 0 || nc >= column) continue
    if (board[nr][nc] === 0 || visited[nr][nc] === 1) continue
    dfs(board, visited, nr, nc, size)
  }
  return board
}

function landCounter(board, row, column) {
  let result = 0
  const visited = Array.from(Array(row), () => Array(column).fill(0))
  for (let i = 0; i < row; i += 1) {
    for (let j = 0; j < column; j += 1) {
      if (board[i][j] === 0) continue 
      dfs(board, visited, i, j, [row, column])
      result += 1
    }
  }
  return result
}

main()