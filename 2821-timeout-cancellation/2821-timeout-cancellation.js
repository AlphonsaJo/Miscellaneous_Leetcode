/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function(fn, args, t) {
    // Schedule the function to run after 't' milliseconds
    const timerId = setTimeout(() => {
        fn(...args);
    }, t);

    // Return a cancel function that clears the timeout
    return function cancelFn() {
        clearTimeout(timerId);
    };
};
