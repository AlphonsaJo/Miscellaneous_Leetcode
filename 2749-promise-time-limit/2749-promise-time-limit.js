/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
function timeLimit(fn, t) {
  return async function(...args) {
    const timeout = new Promise((_, reject) =>
      setTimeout(() => reject("Time Limit Exceeded"), t)
    );

    // Race between the real function and the timeout
    return Promise.race([fn(...args), timeout]);
  };
}


/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */