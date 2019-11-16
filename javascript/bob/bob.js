/* eslint-disable no-unused-vars */
//
// This is only a SKELETON file for the 'Bob' exercise. It's been provided as a
// convenience to get you started writing code faster.
//

function isUpperCase(str) {
  if (str.match(/[a-z]/i)) {
    // alphabet letters found
    return str === str.toUpperCase();
  } else {
    return false;
  }
}

export const hey = message => {
  message = message.trim();
  const question = message.slice(-1) == "?";
  const upper = isUpperCase(message);

  if (question && upper) {
    return "Calm down, I know what I'm doing!";
  } else if (upper) {
    return "Whoa, chill out!";
  } else if (question) {
    return "Sure.";
  } else if (message.length == 0) {
    return "Fine. Be that way!";
  } else {
    return "Whatever.";
  }
};