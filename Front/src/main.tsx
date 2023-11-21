import React from 'react'
import ReactDOM from 'react-dom/client'
import Title from './UIComponents/Title'
import GenerateButton from './UIComponents/GeneratePoem'
import './index.css'

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Title />
    <GenerateButton />
  </React.StrictMode>,
)
