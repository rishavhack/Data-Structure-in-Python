angular.module('PubNubAngularApp', ["pubnub.angular.service"])
  .controller('MySpeechCtrl', function($rootScope, $scope, Pubnub) {

  $scope.nextElementId="item1";
  $scope.fullDetail={};
  $scope.detailItem;
  $scope.obj = {};
  $scope.obj.theText = '';
  // On Click of a button
  $scope.dictateIt = function () {
    // Construct the api function..
      var recognition = new webkitSpeechRecognition();
       //onresult property
       recognition.onresult = function (event) {
        $scope.$apply(function() {
           // resultIndex read-only property      
          for (var i = event.resultIndex; i < event.results.length; i++) {
            if (event.results[i].isFinal) {
              // result event
              $scope.obj.theText  += event.results[i][0].transcript;
              if($scope.obj.theText == 'next' || $scope.obj.theText == 'tab')
              {
              	$scope.detailItem = document.getElementById($scope.nextElementId).nextElementSibling;
	              $scope.nextElementId = $scope.detailItem.id;
	              $scope.detailItem.focus();
	              $scope.fullDetail = $scope.detailItem;
	              $scope.dictateIt();
                $scope.obj.theText='';
                console.log($scope.detailItem);
              }
              if($scope.obj.theText == 'hi')
              {
                $scope.obj.theText='';
              	$scope.writeSomething($scope.detailItem);
              }
              
            }
          }
        });
      };
      recognition.start();
   };
   $scope.writeSomething = function()
   {
   	var recognition = new webkitSpeechRecognition();
       //onresult property
       console.log($scope.detailItem);
       var modelName = $scope.fullDetail.attributes[1].nodeValue.split('.')[1];
       console.log($scope.obj);
       recognition.onresult = function (event) {
        $scope.$apply(function() {
          for (var i = event.resultIndex; i < event.results.length; i++) {
            if (event.results[i].isFinal)
             {
              // result event
               $scope.obj[modelName] = event.results[i][0].transcript;
              }
          }
        });
      };
      recognition.start();
   };
});
  