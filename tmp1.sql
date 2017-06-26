select a.wm_account_posiition_id, /*nvl(a,0),*/ b.limit_amount, /*comment_id,*/ a.field, a * b, b/a
from table
order by a.wm_account_posiition_id, b.limit_amount;