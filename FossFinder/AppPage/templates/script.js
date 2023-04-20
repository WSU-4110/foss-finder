const options = {
  bottom: 'unset', // default: '32px'
  right: '20px', // default: '32px'
  left: 'unset', // default: 'unset'
  time: '5.0s', // default: '0.3s'
  mixColor: '##5A5A5A', // default: '#fff'
  backgroundColor: '##5A5A5A',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  saveInCookies: true, // default: true,
  label: '<span class="darkmode-label">🌓</span>',  // add class to label
  autoMatchOsTheme: true // default: true
}
const darkmode = new Darkmode(options);
darkmode.showWidget();
