(function() {
  'use strict';

  function mozartModalDirective() {
    return {
      restrict: 'E',
      scope: {
        show: '=',
        modalTitle: '@'
      },
      transclude: true,
      template: '<div class="modal-dialog-shadow" ng-show="show">' +
    '<div class="modal-dialog-container">' +
      '<h2 ng-bind="modalTitle"></h2><hr/>' +
      '<div ng-transclude></div>' +
    '</div>' +
  '</div>'
    };
  }

  angular.module('mozArtApp')
    .directive('mzModal', mozartModalDirective);
})();