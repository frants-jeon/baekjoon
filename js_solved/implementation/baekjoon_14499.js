// 주사위 굴리기
// https://www.acmicpc.net/problem/14499

const fs = require('fs')
const input = fs.readFileSync('dev/stdin').toString().split('\n')

function main() {
  const [N, M, x, y] = readlineToNumArray()
  const board = getBoard(N)
  const orders = readlineToNumArray() // 명령 리스트
  const dice = [[0,0,0,0],[0,0,0,0]] // 0행이 주사위의 가로, 1행이 주사위의 세로
  let curPos = [x, y]
  const dr = [null, 0, 0, -1, 1]
  const dc = [null, 1, -1, 0, 0]
  for (const order of orders) {
    const nr = curPos[0] + dr[order]
    const nc = curPos[1] + dc[order]
    if (nr < 0 || nr >= N || nc < 0 || nc >= M) continue
    moveDice(dice, order)
    curPos = [nr, nc]
    if (board[nr][nc] === 0) board[nr][nc] = dice[0][0]
    else {
      changeBottomOfDice(dice, board[nr][nc])
      board[nr][nc] = 0
    }
    console.log(dice[0][2])
  }
}

function changeBottomOfDice(dice, num) {
  dice[0][0] = num
  dice[1][0] = num
}

function moveDice(dice, direction) {
  switch (direction) {
    case 1:
      dice[0].push(dice[0].shift())
      break
    case 2:
      dice[0].unshift(dice[0].pop())
      break
    case 3:
      dice[1].push(dice[1].shift())
      break
    case 4:
      dice[1].unshift(dice[1].pop())
      break
  }
  let moveDir = 0
  let staticDir = 1
  if (direction > 2) {
    moveDir = 1
    staticDir = 0
  }
  const bottom = dice[moveDir][0]
  const top = dice[moveDir][2]
  dice[staticDir][0] = bottom
  dice[staticDir][2] = top
  return dice
}
function getBoard(row) {
  const arr = Array(row)
  for (let i = 0; i < row; i += 1) {
    arr[i] = readlineToNumArray()
  }
  return arr
}

function readlineToNumArray() {
  const result = input.shift().split(' ').map(num => Number(num))
  return result
}

main()