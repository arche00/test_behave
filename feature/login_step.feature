Feature: 로그인
  Scenario: 이메일로 로그인 한다
    Given teacher04@sharklasers.com 계정으로 로그인 한다
    When 메인화면에서 로그인을 클릭한다
    When 이메일로 로그인을 클릭한다
    When 이메일을 입력한다
    When 비밀번호를 입력한다
    When 이메일로 로그인을 클릭한다
    Then 로그인이 완료되고 소식탭으로 포커스가 된다