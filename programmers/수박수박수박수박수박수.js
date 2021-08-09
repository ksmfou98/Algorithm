function solution(n) {
  const str = "수박";
  let result = "";
  for (let i = 1; i <= parseInt(n / 2); i++) {
    result += str;
  }

  n % 2 === 1 && (result += str[0]);
  return result;
}
