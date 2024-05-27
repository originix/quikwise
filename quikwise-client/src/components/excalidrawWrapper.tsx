'use client';
import { Excalidraw } from '@excalidraw/excalidraw';
import { ExcalidrawProps } from '@excalidraw/excalidraw/dist/excalidraw/types';
import { FC } from 'react';

import '@excalidraw/excalidraw/index.css';

const ExcalidrawWrapper: FC<ExcalidrawProps> = ({ initialData, onChange }) => {
  return (
    <>
      <Excalidraw initialData={initialData} onChange={onChange} />
    </>
  );
};

export default ExcalidrawWrapper;
