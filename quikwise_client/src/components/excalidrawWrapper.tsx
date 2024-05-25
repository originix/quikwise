'use client';
import { Excalidraw } from '@excalidraw/excalidraw';
import {
  ExcalidrawInitialDataState,
  ExcalidrawProps,
} from '@excalidraw/excalidraw/dist/excalidraw/types';

import '@excalidraw/excalidraw/index.css';
import { FC } from 'react';

const ExcalidrawWrapper: FC<ExcalidrawProps> = ({ initialData, onChange }) => {
  return (
    <>
      <Excalidraw initialData={initialData} onChange={onChange} />
    </>
  );
};

export default ExcalidrawWrapper;
