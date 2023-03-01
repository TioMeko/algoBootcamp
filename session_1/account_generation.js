const algosdk = require('algosdk');
const uint8ToBase64 = (arr) => Buffer.from(arr).toString('base64');

async function generateAlgorandKeypair() {
  const { sk, addr } = algosdk.generateAccount();
  console.log(`My address: ${addr}`);
  // Base 64 encoding
  console.log(`My private key: ${uint8ToBase64(sk)}`);
  console.log(`My passphrase: ${algosdk.secretKeyToMnemonic(sk)}`);
}

generateAlgorandKeypair();