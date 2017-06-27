select a.wm_account_posiition_id, /*nvl(a,0),*/ b.limit_amount, /*comment_id,*/ a.field, a * b, b/a
from table
where business_date = :BD and business_group_location = :LC --and snippet_ltv_band_lower<1