// Copyright (c) 2023, Techmaniacc and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Stock Entry Server Script"] = {
  filters: [
    {
      fieldname: "stock_entry_type",

      label: "Stock Entry Type",

      fieldtype: "Link",

      options: "Stock Entry Type",
    },

    {
      fieldname: "posting_date",

      label: "From Date",

      fieldtype: "Date",
    },
    {
      fieldname: "posting_time",

      label: "To Date",

      fieldtype: "Date",
    },

    {
      fieldname: "source_warehouse_address",

      label: "Source Warehouse Address",

      fieldtype: "Link",

      options: "Address",
    },
    {
      fieldname: "vehicle",

      label: "Vehicle",

      fieldtype: "Link",

      options: "Vehicle",
    },

    {
      fieldname: "target_warehouse_address",

      label: "Target Warehouse Address",

      fieldtype: "Link",

      options: "Address",
    },
  ],
};
