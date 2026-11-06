(function () {
  var EMAIL = "info@arcmetal.si";

  var toggle = document.getElementById("menu-toggle");
  var nav = document.getElementById("nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      toggle.textContent = open ? "Zapri" : "Meni";
    });
  }

  function openMail(subject, body) {
    window.location.href = "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subject) + "&body=" + encodeURIComponent(body);
  }

  // Kontaktni obrazec: dokler ni povezan s storitvijo za obrazce, odpre e-poštni program s pripravljenim sporočilom.
  document.querySelectorAll(".js-contact").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var note = form.querySelector(".form-note");
      if (!form.checkValidity()) {
        note.textContent = "Izpolnite ime, e-pošto in sporočilo ter potrdite strinjanje z obdelavo podatkov.";
        form.reportValidity && form.reportValidity();
        return;
      }
      var f = form.elements;
      var body = "Ime: " + f.ime.value + "\nPodjetje: " + f.podjetje.value + "\nE-pošta: " + f.email.value +
        "\nTelefon: " + f.telefon.value + "\nStoritev: " + f.storitev.value + "\n\n" + f.sporocilo.value;
      openMail("Povpraševanje: " + f.storitev.value, body);
      note.textContent = "Odpira se vaš e-poštni program s pripravljenim sporočilom. Če se ne odpre, nam pišite na " + EMAIL + ".";
    });
  });

  document.querySelectorAll(".js-partner").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var note = form.parentNode.querySelector(".form-note");
      var input = form.querySelector("input[type=email]");
      if (!input.checkValidity() || !input.value) {
        note.textContent = "Vpišite veljaven e-poštni naslov.";
        return;
      }
      openMail("Mreža partnerjev", "Zanima nas sodelovanje z ARC METAL.\nE-pošta: " + input.value);
      note.textContent = "Odpira se vaš e-poštni program. Lahko nam pišete tudi na " + EMAIL + ".";
    });
  });
})();


// Nova stran se vedno odpre na vrhu (razen ob skoku na sidro, npr. #povprasevanje)
(function () {
  try { if ("scrollRestoration" in history) history.scrollRestoration = "manual"; } catch (e) {}
  if (!location.hash) {
    window.scrollTo(0, 0);
    // v predogledu je stran v okvirju: poskusi premakniti tudi okvir na vrh
    var top = function () { try { document.body.scrollIntoView({ block: "start" }); } catch (e) {} };
    top();
    window.addEventListener("load", top);
  }
})();
