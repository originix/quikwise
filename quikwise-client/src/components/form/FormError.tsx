import { FC, memo } from 'react';
import { FieldErrors } from 'react-hook-form/dist/types/errors';

type FormErrorProps = {
  error: FieldErrors;
};

const FormError: FC<FormErrorProps> = ({ error }) => {
  return (
    <>
      {error ? (
        <div className='form-error text-red-500 font-bold pt-2'>
          <span>{error}</span>
        </div>
      ) : undefined}
    </>
  );
};

export default memo(FormError);
