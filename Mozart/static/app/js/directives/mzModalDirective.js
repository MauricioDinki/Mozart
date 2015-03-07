'use strict';
/**
* @ngdoc function
* @name mozArtApp.directive:mzModal
* @description
* # mzModal
*
* Directive of the mozArtApp.
*/

app.directive('mzModal', [function(){
  return {
    restrict: 'E',
    scope: {
			show: '=',
			modalTitle: '@'
    },
    transclude: true,
    link: function(scope, elem, attrs){
      scope.hideModal = function() {
				scope.show = false;
			};
    },
    template: '<div class="modal-dialog-shadow" ng-show="show">' +
  '<div class="modal-dialog-container">' +
    '<h2 ng-bind="modalTitle"></h2><hr/>' +
    '<div ng-transclude></div>' +
  '</div>' +
'</div>'
  }
}]);

