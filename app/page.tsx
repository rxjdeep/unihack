"use client"

import { supabase } from "@/lib/supabaseClient"

export default function Page() {

  async function testSupabase() {
    const { data, error } = await supabase.from("prefs").select("*")
    console.log("data:", data)
    console.log("error:", error)
  }

  async function insertTest() {
    const { data, error } = await supabase
      .from("prefs")
      .insert([{ item_name: "Milk", checked: true }])

    console.log("insert result:", data)
    console.log("insert error:", error)
  }

  return (
    <div>
      <h1>Grocery Checklist</h1>

      <div className="dairy">
        <label>
          <input type="checkbox" /> Milk
        </label>
        <label>
          <input type="checkbox" /> Cheese
        </label>
      </div>

      <div className="meat">
        <label>
          <input type="checkbox" /> Chicken
        </label>
        <label>
          <input type="checkbox" /> Beef
        </label>
      </div>

      <button onClick={testSupabase}>Test Supabase</button>

      <button onClick={insertTest}>Insert Test Row</button>

    </div>
  )
}
