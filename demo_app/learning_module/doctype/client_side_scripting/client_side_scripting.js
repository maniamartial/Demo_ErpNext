// Copyright (c) 2023, Techmaniacc and contributors
// For license information, please see license.txt

frappe.ui.form.on("Client Side Scripting", {
  after_save: function (frm) {
    frappe.msgprint(
      __("The full name is '{0}'", [
        frm.doc.first_name +
          " " +
          frm.doc.middle_name +
          " " +
          frm.doc.last_name,
      ])
    );
  },
});
//   refresh: function (frm) {
//     frappe.msgrint("Hello Mania");
//     frappe.throw("This is an error");
//   },

//   onload: function (frm) {
//     frappe.msgprint("Hello mania am comng home");
//   },

// after_save:function(frm){
// 	frappe.throw("After save youve doen great jo")
// }

//   age: function (frm) {
//     frappe.msg("Hello D-Code from 'age' filedname events");
//   },

//   family_members_form_rendered: function (frm) {
//     frappe.msgprint("Hello Mania");
//   },
// });

// frappe.ui.form.on("Family Members"),
//   {
//     name1: function (frm) {
//       frappe.msgprint("Hello childname 1");
//     },
//   };
