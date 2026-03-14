export default function Page() {
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
    </div>
  );
}