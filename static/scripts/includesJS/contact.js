// Coloque aqui os scripts relacionado a "Contatos"
$("#contact-form").submit(function(e) {
    e.preventDefault();

    const name = $('input[name = name]').val()
    const cnpj = $('input[name = cnpj').val()
    const email = $('input[name = email]').val()
    const occupation= $('input[name = occupation]').val()
    const message = $('input[name = message]').val()

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