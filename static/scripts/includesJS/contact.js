$("#contact-content-form").submit(function(e) {
     e.preventDefault();

     const name = $('input[name = name]').val()
     const cnpj = $('input[name = cnpj').val()
     const email = $('input[name = email]').val()
     const occupation = $('input[name = occupation]').val()
     const message = $('textarea[name = message]').val()

     document.getElementById('contact-content-form-reset').click();

     const token = jQuery("[name=csrfmiddlewaretoken]").val();

     $.ajax({
        type: 'POST',
        url: '/contact/',
        data:
           { 'csrfmiddlewaretoken': token,
             'name' : name,
             'cnpj' : cnpj,
             'email' : email,
             'occupation' : occupation,
             'message' : message
            },
   })
 })