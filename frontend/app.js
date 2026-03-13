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

async function savePrefs() {

  console.log("Save clicked")

  const username = localStorage.getItem("user")

  if (!username) {
    alert("User not logged in")
    return
  }

  // get user id
  const { data: userData, error: userError } = await supabase
    .from("users")
    .select("id")
    .eq("username", username)
    .limit(1)

  if (userError) {
    console.error(userError)
    alert("User lookup failed")
    return
  }

  const userId = userData[0].id

  // get checked foods
  const checkedFoods = document.querySelectorAll("input[type='checkbox']:checked")

  for (const food of checkedFoods) {

    const { error } = await supabase
      .from("prefs")
      .insert({
        user_id: userId,
        item_name: food.value,
        checked: true
      })

    if (error) {
      console.error(error)
    }

  }

  alert("Preferences saved!")
}

window.signup = signup
window.login = login
window.savePrefs = savePrefs
