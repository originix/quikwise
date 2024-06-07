export function useScroll(ref?: string) {
    const selector = ref || '.c-body'
    const cBodyElement = document.querySelector(selector)

    return {
        toTop:
            cBodyElement?.scrollTo({ top: 0, behavior: 'smooth' }) ||
            (() => {}),
        toBottom:
            cBodyElement?.scrollTo({
                top: cBodyElement.scrollHeight,
                behavior: 'smooth',
            }) || (() => {}),
    }
}
