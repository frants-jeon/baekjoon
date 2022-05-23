// 아기상어
// https://www.acmicpc.net/problem/16236

const fs = require('fs')
const input = fs.readFileSync('dev/stdin').toString().split('\n')

function main() {
  const N = readlineToNumArray()[0]
  const board = getBoard(N)
  let sharkPos = getSharkPos(board, N)
  board[sharkPos[0]][sharkPos[1]] = 0
  let sharkSize = 2
  let eatCount = 0
  let timer = 0
  while (true) {
    // 가장 가까운 물고기 찾기.
    const bfsResult = findEatableFish(board, N, sharkPos, sharkSize)
    if (!bfsResult) break // 먹을 수 있는 물고기가 없을 경우 탐색 중단
    const [r, c, t] = bfsResult // 가장 가까운 물고기의 행, 열, 시간
    sharkPos = [r, c] // 상어 위치 수정
    eatCount += 1 // 한 마리 섭취
    // 몸집만큼 먹었으면 사이즈 키우고 먹은 갯수 초기화
    if (sharkSize === eatCount) {
      sharkSize += 1
      eatCount = 0
    }
    timer += t // 움직인 시간 더하기
    board[r][c] = 0 // 상어가 먹은 자리는 빈칸
  }
  return timer
}

function findEatableFish(board, boardSize, sharkPos, sharkSize) {
  const que = []
  que.push([...sharkPos, 0])
  const eatableList = []
  const visited = Array.from(Array(boardSize), () => Array(boardSize).fill(0))
  visited[sharkPos[0]][sharkPos[1]] = 1
  const dr = [-1, 0, 0, 1]
  const dc = [0, -1, 1, 0]
  while (que.length > 0) {
    const [r, c, time] = que.shift()
    for (let i = 0; i < 4; i += 1) {
      const nr = r + dr[i]
      const nc = c + dc[i]
      if (nr < 0 || nr >= boardSize || nc < 0 || nc >= boardSize) continue // 보드 크기 넘어가면 패스
      if (board[nr][nc] > sharkSize) continue // 상어보다 큰 물고기는 못지나감
      if (visited[nr][nc] === 1) continue // 이미 방문한 자리도 패스
      if (eatableList.length > 0 && eatableList[0][2] < time + 1) break // 이미 가장 가까운 물고기들을 다 찾았으면 중단
      // 먹을 수 있는 물고기라면 후보군에 추가
      if (board[nr][nc] < sharkSize && board[nr][nc] > 0) {
        eatableList.push([nr, nc, time + 1])
      }
      visited[nr][nc] = 1 // 중복으로 탐색하지 않기 위해 미리 방문 체크
      que.push([nr, nc, time + 1])
    }
  }
  if (eatableList.length === 0) return false // 먹을 수 있는 물고기가 없으면 탐색 중단을 위해 false 리턴
  let result = [boardSize, boardSize, 0] // [r, c, t] 저장. 위치 갱신을 위해 최댓값으로 저장
  for (const eatable of eatableList) {
    if (eatable[0] < result[0]) result = eatable // 먹을 수 있는 물고기 중에 단독으로 가장 위에 있으면 갱신 
    else if (eatable[0] === result[0] && eatable[1] < result[1]) result = eatable // r좌표가 동일하면 왼쪽에 있는 좌표로 갱신
  }
  return result
}

function readlineToNumArray() {
  const result = input.shift().split(' ').map(num => Number(num))
  return result
}

function getBoard(size) {
  const board = []
  for (let i = 0; i < size; i += 1) {
    board.push(readlineToNumArray())
  }
  return board
}

function getSharkPos(board, size) {
  for (let i = 0; i < size; i += 1) {
    for (let j = 0; j < size; j += 1) {
      if (board[i][j] == 9) return [i, j]
    }
  }
}

console.log(main())