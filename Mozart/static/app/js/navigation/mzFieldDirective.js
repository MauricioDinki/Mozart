(function() {
  'use strict';
 
  function mozartFieldDirective() {
    return {
      restrict: 'A',
      scope: false,
      transclude: false,
      link: function(scope, elem, attrs){
        if(elem.val() !== '') {
          elem.prev('label').removeClass('initial-label');
          elem.removeClass('empty-initial-field'); 
          elem.prev('label').addClass('non-active-label');
          elem.addClass('active-field');
        }
        elem.focus(function(){
          if(elem.prev('label').hasClass('initial-label')) {
            elem.prev('label').removeClass('initial-label');
          }
          else {
            elem.prev('label').removeClass('non-active-label');
          }
          elem.prev('label').addClass('active-label');
          elem.removeClass('empty-initial-field'); 
          elem.addClass('active-field');
        });
        elem.blur(function(){
          elem.prev('label').removeClass('active-label');
          if(elem.val() === '' && !((elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) || (elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')))){
            elem.removeClass('active-field');
            elem.addClass('empty-initial-field');
            if(elem.prop('tagName') === 'SELECT') {
              elem.prev('label').addClass('non-active-label');
            }
            else{
              elem.prev('label').addClass('initial-label');
            }
          }
          else {
            elem.prev('label').addClass('non-active-label');
          }
          if(elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
          if(elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
        });
        elem.keyup(function() {
          if(elem.hasClass('ng-invalid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('valid-state')) {
              elem.prev('label').removeClass('valid-state');
            }
            elem.prev('label').addClass('invalid-state');
          }
          else if(elem.hasClass('ng-valid') && elem.hasClass('ng-dirty')) {
            if(elem.prev('label').hasClass('invalid-state')) {
              elem.prev('label').removeClass('invalid-state');
            }
            elem.prev('label').addClass('valid-state');
          }
        });
      }
    };
  }

  angular.module('mozArtApp')
    .directive('mzField', mozartFieldDirective);
})();