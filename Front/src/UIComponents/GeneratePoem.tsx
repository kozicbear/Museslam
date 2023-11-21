import React, {useState, useEffect} from 'react'
import styles from './GenerateButton.module.css'
import { useSpeechSynthesis } from 'react-speech-kit'

export default function GeneratePoem() {
    const [poem, setPoem] = useState(Object)
    const [text, setText] = useState("")
    const [showPoem, setShowPoem] = useState(false)
    const { speak, cancel } = useSpeechSynthesis()

    const handleClick = async () => {
        fetch("http://127.0.0.1:5000/api/poem").then(
            response => response.json()
        ).then(
            data => {
                const array = data.poem.map((line: String) => <div className={styles.line}> {line} </div>)
                const textToSpeech = data.poem.map((line: String) => line)
                setPoem(array)
                setText(textToSpeech)
                setShowPoem(true)
            }
        )
    }

    return (
        <div className={styles.wrapper}>
            <div onClick={handleClick} className={styles.generateButton}>Generate Poem</div>
            { showPoem && poem }
            <div className={styles.buttonWrapper}>
                <button className={styles.button} onClick={() => speak({
                        text:text
                    })}> 
                    Play 
                </button>
                <button className={styles.button} onClick={cancel}>
                    Stop
                </button>
            </div>
        </div>
    )
}