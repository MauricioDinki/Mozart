(function() {
  'use strict';

  function mozartModalDirective() {
    return {
      restrict: 'AEC',
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
    '<div class="modal-dialog-container" off-click="hideModal()" off-click-if="show">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div ng-transclude></div>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzModal', mozartModalDirective);
})();