import { createClient } from "https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm"

const supabase = createClient(
  "https://qinptrlkymbtenxlexhb.supabase.co",
  "sb_publishable_iMzglyd9ZcEtGPe-YwHSaA_Y92p3ZNL"
)

// signup function
async function signup() {
  const username = document.getElementById("username").value
  const password = document.getElementById("password").value

  const { data, error } = await supabase
    .from("users")
    .insert([{ username: username, password: password }])

  if (error) {
    console.log(error)
    alert("Signup failed")
  } else {
    alert("User created!")
  }
}

// login function
async function login() {
  const username = document.getElementById("username").value
  const password = document.getElementById("password").value

  const { data, error } = await supabase
    .from("users")
    .select("*")
    .eq("username", username)
    .eq("password", password)

  if (error) {
    console.log(error)
    alert("Login error")
    return
  }

  if (data.length > 0) {
    localStorage.setItem("user", username)
    window.location.href = "/main.html"
  } else {
    alert("Invalid login")
  }
}

window.signup = signup
window.login = login
