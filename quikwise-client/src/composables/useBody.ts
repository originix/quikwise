export function useBody() {
    const bodyElement = document.body

    const clear = () => {
        bodyElement.className = ''
        bodyElement.style.overflow = ''
        bodyElement.style.paddingRight = ''
        bodyElement.style.paddingLeft = ''
    }

    return {
        body: bodyElement,
        clear: clear,
    }
}
