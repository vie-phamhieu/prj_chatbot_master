function sendRequest() {
  var userInput = $("#textInput").val(); // Lấy giá trị từ input field
  var userHtml = '<p class="userText"><span>' + userInput + '</span></p>';
  $("#textInput").val("");
  $("#chatbox").append(userHtml);
  scrollToUserInput();

  // Gửi yêu cầu POST tới API Flask
  $.ajax({
      url: '/ask',
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({ 'question': userInput }),
      success: function(data) {
          var botHtml = '<p class="botText"><span>' + data.response + '</span></p>';
          $("#chatbox").append(botHtml);
          scrollToUserInput();
      },
      error: function(xhr, status, error) {
          var errorMessage = "Error: " + xhr.responseText;
          var errorHtml = '<p class="botText"><span>' + errorMessage + '</span></p>';
          $("#chatbox").append(errorHtml);
          scrollToUserInput();
      }
  });
}

function scrollToUserInput() {
  document.getElementById('userInput').scrollIntoView({block: 'start', behavior: 'smooth'});
}

$("#textInput").keypress(function(e) {
  if(e.which == 13) {
      sendRequest();
  }
});

$("#buttonInput").click(function() {
  sendRequest();
});
