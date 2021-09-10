function solution(record) {
  let users = {};
  let result = [];

  for (let i = 0; i < record.length; i++) {
    let [command, userId, nickname] = record[i].split(" ");
    if (command === "Enter" || command === "Change") {
      users[userId] = nickname;
    }
  }

  for (let i = 0; i < record.length; i++) {
    let [command, userId, nickname] = record[i].split(" ");
    if (command === "Enter") {
      result.push(`${users[userId]}님이 들어왔습니다.`);
    } else if (command === "Leave") {
      result.push(`${users[userId]}님이 나갔습니다.`);
    }
  }

  return result;
}

const record = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];

console.log(solution(record));
