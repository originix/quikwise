import { FieldErrors } from 'react-hook-form/dist/types/errors';
import { UseFormRegister, UseFormSetFocus, UseFormSetValue } from 'react-hook-form/dist/types/form';
import { FieldValues } from 'react-hook-form/dist/types/fields';

export interface IBaseDropdown {
  text: ReactNode;
  value: unknown;
}

export interface IBaseProps {
  errors?: FieldErrors;
  name: string;
  register: UseFormRegister<FieldValues>;
  setValue?: UseFormSetValue;
  setFocus?: UseFormSetFocus;
}

export interface IDropdownProps extends IBaseProps {
  buttonLabel?: ReactNode;
  options: IBaseDropdown[];
  onSelect: (value: unknown, deepValue?: unknown) => void;
  valueToPass?: unknown;
  dynamicData?: IBaseDropdown;
  flag?: {
    key: string;
    value: string;
  };
  enableSearch?: boolean;
  isMultiselect?: boolean;
  isObject?: boolean;
}
