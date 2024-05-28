import { ReactNode } from 'react';
import { customAlphabet } from 'nanoid';

export function getFromLocalStorage(key: string): string | null {
  return typeof window !== 'undefined' ? window.localStorage.getItem(key) : null;
}

export function getFromSessionStorage(key: string): string | null {
  return typeof window !== 'undefined' ? window.sessionStorage.getItem(key) : null;
}

export function generateID(n?: number) {
  const nanoid = customAlphabet(
      '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
      10
  );
  return nanoid(n || 12);
}

export function getTextFromReactNode(node: ReactNode): string {
  if (node == null) return '';

  switch (typeof node) {
    case 'string':
    case 'number':
      return node.toString();

    case 'boolean':
      return '';

    case 'object': {
      if (node instanceof Array) return node.map(getTextFromReactNode).join('');

      if ('props' in node) return getTextFromReactNode(node.props.children);
    } // eslint-ignore-line no-fallthrough

    default:
      console.warn('Unresolved `node` of type:', typeof node, node);
      return '';
  }
}
