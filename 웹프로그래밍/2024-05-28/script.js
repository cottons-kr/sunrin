class Program {
  /**
   * @type {string | null}
   */
  currentUser = null
  /**
   * @description key: username, value: to-do list
   * @type {Map<string, string[]>}
   */
  users = new Map()

  constructor() {}

  login() {
    const input = prompt("Username을 입력해 주세요!");
    if (input === null) return;

    if (Object.keys(this.users).includes(input)) {
      this.currentUser = input;
      alert(`${input}님 다시 접속 하신 것을 환영합니다.`);
    } else {
      this.currentUser = input;
      this.users.set(input, []);
      alert(`${input}님 처음 접속 하신 것을 환영합니다.`);
    }

    this.startShell();
  }

  logout() {
    if (this.currentUser === null) {
      return alert('로그인이 되어있지 않습니다.');
    }
    this.currentUser = null;
    alert('로그아웃 되었습니다.');
    return { request: 'exit' }
  }

  list() {

  }

  startShell() {
    while (true) {
      const command = prompt("무엇을 도와드릴까요? (press: Q to exit)");
      if (['Q', 'q'].includes(command)) {
        alert('프로그램을 종료합니다.');
        break;
      }
      const [cmd, ...args] = command.split(' ');
      const func = this[cmd];

      if (!func) continue;
      if (this.currentUser === null) {
        alert('로그인이 되어있지 않습니다.');
        break;
      }

      const { request } = func.call(this, ...args);
      if (request === 'exit') {
        break;
      }
    }
  }
}

const program = new Program();
program.login();
