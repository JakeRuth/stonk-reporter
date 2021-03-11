const {
  createElement,
  Fragment,
  useState,
} = React;

const onButtonClick = (ticker) => {
  window.location = `https://foz7iasje5.execute-api.us-east-2.amazonaws.com/singleCompany?ticker=${ticker}`;
};

const onButtonClick2 = (ticker) => {
  window.location = `https://foz7iasje5.execute-api.us-east-2.amazonaws.com/multipleCompanies?ticker=${ticker}`;
};

function App() {
  const [tickerInput, setTickerInput] = useState('');

  const onTickerChange = (e) => {
    setTickerInput(e.target.value);
  };

  const onButtonClickWrapper = () => {
    onButtonClick(tickerInput);
  };

  const onButton2ClickWrapper = () => {
    onButtonClick2(tickerInput);
  };

  return (
    <div className="content">
      <h1 className="text">Stonk Analyzer (Beta)</h1>
      <div className="inputContainer">
        <span className="text inputLabel">Single stonk ticker: </span>
        <input className="tickerInput" name="ticker" onChange={onTickerChange} />
      </div>
      <button className="createSheetButton" onClick={onButtonClickWrapper} type="button">Analyze stonk</button>
      <div className="inputContainer">
        <span className="text inputLabel">Multiple stonk tickers (i.e. AAPL,TSLA,ZM): </span>
        <input className="tickerInput" name="ticker" onChange={onTickerChange} />
      </div>
      <button className="createSheetButton" onClick={onButton2ClickWrapper} type="button">Analyze stonks</button>
      <p className="text">
        US Tickers only for now. (Will support non US ticker types soon).
      </p>
      <p className="text">
        This is beta software, expect bugs/weird things.
      </p>
    </div>
  );
}

ReactDOM.render(
  createElement(App),
  document.querySelector('#reactjs-root'),
);
