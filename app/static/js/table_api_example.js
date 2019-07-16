$(document).ready(function () {
    $.ajax({
        url: `/api/example`,
        success: function (data) {
            $('#table_api_example').DataTable({
                data: data,
                "columns": [
                    {"data": "nome"},
                    {"data": "idade"},
                    {"data": "cpf"},
                    {"data": "rg"},
                    {"data": "data_nasc"},
                    {"data": "celular"},
                    {"data": "altura"},
                    {"data": "peso"},
                    {"data": "tipo_sanguineo"},
                ],

                destroy: true,
                paging: false,
                language: {
                    "sEmptyTable": "Nenhum registro encontrado",
                    "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
                    "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
                    "sInfoFiltered": "(Filtrados de _MAX_ registros)",
                    "sInfoPostFix": "",
                    "sInfoThousands": ".",
                    "sLengthMenu": "_MENU_ Resultados por página",
                    "sLoadingRecords": "Carregando...",
                    "sProcessing": "Processando...",
                    "sZeroRecords": "Nenhum registro encontrado",
                    "sSearch": "Pesquisar",
                    "oPaginate": {
                        "sNext": "Próximo",
                        "sPrevious": "Anterior",
                        "sFirst": "Primeiro",
                        "sLast": "Último"
                    }
                },
                dom: 'Bfrtip',
                buttons: [
                    {
                        extend: 'excel',
                        className: 'btn bg-poupex text-white'
                    }, {
                        extend: 'csv',
                        className: 'btn bg-poupex text-white'
                    }, {
                        extend: 'pdf',
                        className: 'btn bg-poupex text-white'
                    }, {
                        extend: 'print',
                        className: 'btn bg-poupex text-white'
                    },
                ],

            }).order([1, 'asc']);
        },
    });
});
