const options = {
bottom: '15px', // default: '32px'
  right: 'unset', // default: '32px'
  left: 'unset', // default: 'unset'
  time: '0.5s', // default: '0.3s'
  mixColor: '#fff', // default: '#fff'
  backgroundColor: '#fff',  // default: '#fff'
  buttonColorDark: '#100f2c',  // default: '#100f2c'
  buttonColorLight: '#fff', // default: '#fff'
  label: '🌓',  // default: ''
  autoMatchOsTheme: true // default: true

}
const darkmode = new Darkmode(options);
darkmode.showWidget();
