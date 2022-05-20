@post
Feature: 게시글 작성
  Scenario: 나는 게시글을 작성한다
    When 나는 클래스홈으로 이동한다
    And 글쓰기를 선택한다
    And 텍스트를 입력하고 완료를 클릭한다
    Then 글쓰기가 완료되면 작성한 게시글이 게시된다

