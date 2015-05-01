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
        function compare(){
          var valid = (scope.mzMatch === ctrl.$modelValue);
          console.log(valid);
          if(valid && elem.val().length >= 6) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
          else if(!elem.prev('label').hasClass('initial-label')){
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
          return valid;
        }
        scope.$watch(
          compare, 
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