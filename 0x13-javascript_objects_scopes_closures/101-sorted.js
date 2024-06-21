#!/usr/bin/node
/*
This module contains a script that imports a dictionary of occurrences by user id and computes a dictionary
of user ids by occurrence.
  * it imports dict from the file 101-data.js *
 In the new dictionary: A key is a number of occurrences
                        A value is the list of user ids
*/
const olddict = require('./101-data').dict;

function occurrences (olddict) {
  const userIds = {};
  for (const [userId, occurrence] of Object.entries(olddict)) {
    if (!userIds[occurrence]) {
      userIds[occurrence] = [];
    }
    userIds[occurrence].push(userId);
  }
  return userIds;
}
const userOccurrence = occurrences(olddict);

console.log(`{ ${Object.keys(userOccurrence).map(occurrence => `'${occurrence}': [ ${userOccurrence[occurrence].map(id => `'${id}'`).join(', ')} ]`).join(', ')} }`);
