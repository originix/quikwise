'use client';
import { convertToExcalidrawElements } from '@excalidraw/excalidraw';
import dynamic from 'next/dynamic';

const Excalidraw = dynamic(
  async () => (await import('@/components/excalidrawWrapper')).default,
  {
    ssr: false,
    loading: () => <p>Loading...</p>,
  },
);
const ExcalidrawWrapper: React.FC = () => {
  return (
    <div style={{ height: '100vh', width: '100wv' }}>
      <Excalidraw
        initialData={{
          elements: [
            {
              type: 'rectangle',
              version: 141,
              versionNonce: 361174001,
              isDeleted: false,
              id: 'oDVXy8D6rom3H1-LLH2-f',
              fillStyle: 'hachure',
              strokeWidth: 1,
              strokeStyle: 'solid',
              roughness: 1,
              opacity: 100,
              angle: 0,
              x: 100.50390625,
              y: 93.67578125,
              strokeColor: '#000000',
              backgroundColor: 'transparent',
              width: 186.47265625,
              height: 141.9765625,
              seed: 1968410350,
              groupIds: [],
            },
          ],
          // appState: { zenModeEnabled: true, viewBackgroundColor: "#a5d8ff" },
          // scrollToContent: true
        }}
        onChange={(e) => console.log(e)}
      />
    </div>
  );
};
export default ExcalidrawWrapper;
