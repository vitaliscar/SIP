// Oculta la barra de scroll y muestra el indicador solo si hay scroll disponible en la sidebar
(function() {
  function updateSidebarScrollIndicator() {
    var nav = document.querySelector('.sidebar__nav');
    var indicator = nav.querySelector('.sidebar__scroll-indicator');
    if (!nav || !indicator) return;
    if (nav.scrollHeight > nav.clientHeight + 2) {
      nav.classList.add('scrollable');
    } else {
      nav.classList.remove('scrollable');
    }
  }
  document.addEventListener('DOMContentLoaded', updateSidebarScrollIndicator);
  window.addEventListener('resize', updateSidebarScrollIndicator);
  var nav = document.querySelector('.sidebar__nav');
  if (nav) nav.addEventListener('scroll', updateSidebarScrollIndicator);
})();
