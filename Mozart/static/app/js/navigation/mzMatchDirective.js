(function() {
  'use strict';
 
  function mozartMatchDirective() {
    return {
      restrict: 'A',
      require: 'ngModel',
      scope: {
        mzMatch: '='
      },
      link: function(scope, elem, attrs, ctrl){
        scope.compare = function(){
          return scope.mzMatch === ctrl.$modelValue;
        };
        scope.$watch(
          scope.compare, 
          function(currentValue) {
            ctrl.$setValidity('match', currentValue);
          }
        );
      }
    };
  }

  angular.module('mozArtApp')
    .directive('mzMatch', mozartMatchDirective);
})();