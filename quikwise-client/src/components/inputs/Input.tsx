'use client';
import { ChangeEvent, FC, ForwardRefExoticComponent, RefAttributes, useEffect } from 'react';
import { LucideProps } from 'lucide-react';
import FormError from '@/components/form/FormError';
import { IBaseProps } from '@/types';
import { cn } from '@/lib/utils';

interface IInputProps extends IBaseProps {
  onChange?: (
    event: ChangeEvent<HTMLInputElement> | ChangeEvent<HTMLTextAreaElement> | string,
  ) => void;
  placeholder?: string;
  disabled?: boolean;
  width?: string;
  borderRadius?: 'rounded' | 'semi' | 'none';
  icon?: ForwardRefExoticComponent<Omit<LucideProps, 'ref'> & RefAttributes<SVGSVGElement>>;
  className?: string;
  readOnly?: boolean;
  onClick?: (e: MouseEvent<HTMLInputElement>) => void;
  type?: string;
  inputClassName?: string;
}

const InputText: FC<IInputProps> = ({
  onChange,
  onClick,
  placeholder,
  disabled = false,
  width = 'w-full',
  borderRadius = 'semi',
  icon: Icon,
  className,
  readOnly = false,
  type = 'text',
  errors,
  name,
  register,
  inputClassName,
  setFocus,
}) => {
  const borderRadiusClass = () => {
    switch (borderRadius) {
      case 'rounded':
        return 'rounded-lg border-gray-300 focus:ring-primary-600';
      case 'semi':
        return 'rounded-md border-gray-300 focus:ring-primary-600';
      case 'none':
        return 'rounded-none border-transparent focus:ring-transparent active:ring-transparent';
      default:
        return '';
    }
  };

  useEffect(() => {
    if (setFocus) setFocus(name);
  }, [setFocus]);

  return (
    <>
      <div
        className={`flex items-center gap-2 justify-start relative bg-transparent ${width} ${borderRadiusClass()} ${className}`}
      >
        {Icon && <Icon className='w-[28.55px] absolute left-2 text-gray-400' />}
        <input
          {...register(name)}
          readOnly={readOnly}
          className={cn([
            inputClassName,
            Icon ? 'pl-10' : '',
            `border-gray-300 resize-none focus:border-transparent outline-none text-black transition-all duration-200 ease-in-out w-full placeholder-gray-400 text-md`,
            `${borderRadiusClass()}`,
          ])}
          type={type}
          placeholder={placeholder}
          disabled={disabled}
          onChange={(event) => {
            onChange ? onChange!(event.target.value) : null;
          }}
          onClick={(e) => {
            onClick ? onClick!(e) : null;
          }}
        />
      </div>
      <FormError error={errors ? errors[name]?.message : undefined} />
    </>
  );
};

export default InputText;
