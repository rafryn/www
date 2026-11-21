// Formularz zapisu – WERSJA TESTOWA: niczego nie wysyła, tylko sprawdza pola i pokazuje komunikat.
// Podłączenie wysyłki (wariant B lub C) zrobimy po decyzji Zarządu.
(function () {
  var form = document.getElementById('zgloszenie');
  var msg = document.getElementById('form-msg');
  if (!form) return;
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var bad = Array.prototype.find.call(form.elements, function (el) { return el.willValidate && !el.checkValidity(); });
    msg.hidden = false;
    if (bad) {
      msg.textContent = 'Uzupełnij wszystkie wymagane pola i zaznacz oba oświadczenia.';
      bad.focus();
      return;
    }
    msg.textContent = 'Wersja testowa: formularz działa poprawnie, ale nie wysyła jeszcze danych.';
  });
})();
