$(document).ready(function () {
    $('#table_encargos').DataTable({
        dom: 'fBlrtip',
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
        "language": {
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
        }
    });
    $('#table_encargos_length').addClass('mt-3')
});
