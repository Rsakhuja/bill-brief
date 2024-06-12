import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import UploadPDFCard from './PDFUpload/PDFUpload';
import AnalysisPage from './AnalysisPage/AnalysisPage';
import SignIn from './temp/temp';

function App() {
  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<UploadPDFCard/>}/>
        <Route exact path="/analysis" element={<AnalysisPage/>}/>
        <Route exact path="/signin" element={<SignIn/>}/>
      </Routes>
    </Router>
  );
}

export default App;
