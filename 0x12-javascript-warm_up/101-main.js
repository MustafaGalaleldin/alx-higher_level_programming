#!/usr/bin/env node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(-1, function () {
  console.log('C is fun');
});
