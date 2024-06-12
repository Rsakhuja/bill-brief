import './App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import UploadPDFCard from './PDFUpload/PDFUpload';
import AnalysisPage from './AnalysisPage/AnalysisPage';
import SignIn from './temp/temp';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<UploadPDFCard/>}/>
        <Route path="/analysis" element={<AnalysisPage/>}/>
        <Route path="/signin" element={<SignIn/>}/>
      </Routes>
    </Router>
  );
}

export default App;
