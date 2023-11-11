import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import Title from './UIComponents/Title'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Title />
  </React.StrictMode>,
)
