function solution(s) {
  const arr = [];
  for (let i = 0; i < s.length; i++) {
    arr[arr.length - 1] !== s[i] ? arr.push(s[i]) : arr.pop();
  }
  return arr.length > 0 ? 0 : 1;
}
