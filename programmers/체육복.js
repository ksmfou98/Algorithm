function solution(n, lost, reserve) {
  lost.sort();
  reserve.sort();
  let _lost = lost.filter((l) => !reserve.includes(l));
  let _reserve = reserve.filter((r) => !lost.includes(r));
  let store = [];

  _lost.forEach((l) => {
    if (_reserve.includes(l - 1)) {
      const idx = _reserve.indexOf(l - 1);
      _reserve.splice(idx, 1);
      store.push(l);
    } else if (_reserve.includes(l + 1)) {
      const idx = _reserve.indexOf(l + 1);
      _reserve.splice(idx, 1);
      store.push(l);
    }
  });

  let result = _lost.filter((item) => !store.includes(item));

  return n - result.length;
}
