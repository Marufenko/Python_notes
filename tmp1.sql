select a.wm_account_posiition_id, b.limit_amount from crdb_data.wm_account_position_history a
join crdb_data.wm_limit_position b on a.wm_limit_id = b.wm_limit_id and a.business_date = b.business_date and a.business_group_locaiton = b.business_group_location
join crdb_data.wm_limit_positionsdsd b on a.wm_limit_id = b.wm_limit_id and a.business_date = b.business_date and a.business_group_locaitonsdsdsd = b.business_group_locaitonsdsdsd
where a.business_date = '28-Apr-2017'
and a.business_group_location             ='WMCH' and a.exposure_asset_flag            = 'E'
group by a.business_group_location ,exposure_asset_flag
having a>3
order by a.sm, a.sdf,a.sdfs;
