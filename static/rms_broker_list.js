$(document).ready(function () {
    
    loadRmsTableData(1);

    $('#btn-search').on('click', function () {
        loadRmsTableData(1);
    });

    $('#btn-search-clear').on('click', function () {
        $('#search').val('');
        loadRmsTableData(1);
    });

    function loadRmsTableData(page) {
      const search = $('#search').val();
      $.getJSON(`/api/rms_trade_list?page=${page}&search=${search}`, function (data) {
        const rows = data.items.map(item => `
                      <tr>
                          <td>${item.id}</td>
                          <td>${item.trade_date}</td>
                          <td>${item.total_value}</td>
                          <td>${item.total_trades}</td>
                      </tr>
                  `).join('');
        $('#trade-summary-table').html(rows);
        
        $('#current_page').text(data.current_page);
        $('#per_page').text(data.per_page);
        $('#total').text(data.total);

        const pagination = generatePagination(data.pages, data.current_page);
        $('#pagination').html(pagination);

        $('.page-link').click(function (e) {
          e.preventDefault();
          loadRmsTableData($(this).data('page'));
        });

      });
    }
  });


  function generatePagination(pages, currentPage) {
    let pagination = '';

    // Previous button
    if (currentPage > 1) {
      pagination += `
            <li class="page-item">
                <a class="page-link" href="#" data-page="${currentPage - 1}">Prev</a>
            </li>
        `;
    }

    // First few pages and ellipsis if necessary
    if (currentPage > 3) {
      pagination += `
                <li class="page-item"><a class="page-link" href="#" data-page="1">1</a></li>
                <li class="page-item"><a class="page-link" href="#" data-page="2">2</a></li>
                <li class="page-item disabled"><span class="page-link">...</span></li>
            `;
    }

    // Pages around the current page
    let start = Math.max(1, currentPage - 2);
    let end = Math.min(pages, currentPage + 2);

    for (let i = start; i <= end; i++) {
      pagination += `
                <li class="page-item ${i === currentPage ? 'active' : ''}">
                    <a class="page-link" href="#" data-page="${i}">${i}</a>
                </li>
            `;
    }

    // Last few pages and ellipsis if necessary
    if (currentPage < pages - 2) {
      pagination += `
                <li class="page-item disabled"><span class="page-link">...</span></li>
                <li class="page-item"><a class="page-link" href="#" data-page="${pages - 1}">${pages - 1}</a></li>
                <li class="page-item"><a class="page-link" href="#" data-page="${pages}">${pages}</a></li>
            `;
    }

    // Next button
    if (currentPage < pages) {
      pagination += `
                <li class="page-item">
                    <a class="page-link" href="#" data-page="${currentPage + 1}">Next</a>
                </li>
            `;
    }

    return pagination;
  }