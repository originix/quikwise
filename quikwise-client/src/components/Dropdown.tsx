'use client';
import { FC, useCallback, useEffect, useMemo, useReducer, useRef, useState } from 'react';
import { unionBy } from 'lodash';
import { X } from 'lucide-react';
import { IBaseDropdown, IDropdownProps, TIDropdownReducer } from '@/types';
import { generateID, getTextFromReactNode } from '@/lib/helper';
import InputText from '@/components/inputs/Input';
import FormError from '@/components/form/FormError';
import { cn } from '@/lib/utils';
import { useForm } from 'react-hook-form';
import { EBaseDropdownReducer } from '@/constant/dropdown';

const Dropdown: FC<IDropdownProps> = ({
  buttonLabel,
  options,
  onSelect,
  valueToPass,
  dynamicData,
  flag,
  enableSearch = false,
  isMultiselect = false,
  isObject = false,
  errors,
  name,
  register,
  setValue,
  label,
  getValues,
  placeholder = 'Please select',
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [multiselect, setMultiselect] = useReducer(reducer, []);
  const singleSelect = useRef<IBaseDropdown>();
  const [height, setHeight] = useState<number>(0);
  const ref = useRef<HTMLInputElement>(null);

  const { register: DRegister, setFocus: DSetFocus, setValue: DSetValue } = useForm();

  const handleClickOutside = useCallback((event: MouseEvent) => {
    if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
      setIsOpen(false);
    }
  }, []);

  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [handleClickOutside]);

  useEffect(() => {
    setHeight(ref.current?.clientHeight || 0);
  }, [isOpen, multiselect]);

  const toggleMenu = useCallback(
    (e: MouseEvent<HTMLElement>, flag?: boolean) => {
      e.stopPropagation();
      setIsOpen((prevIsOpen) => (flag ? flag : !prevIsOpen));
      DSetFocus(name);
    },
    [name, DSetFocus],
  );

  function reducer(state: IBaseDropdown[], action: TIDropdownReducer) {
    switch (action.type) {
      case EBaseDropdownReducer.CREATE: {
        const u = unionBy([...state, action.payload], 'value');
        onSelect(u, valueToPass);
        return u;
      }
      case 'delete': {
        const ps = state.filter((x: IBaseDropdown) => action.payload.value !== x.value);
        onSelect(ps, valueToPass);
        setValue(
          name,
          ps.map((x: IBaseDropdown) => x.value),
        );
        return ps;
      }
    }
  }

  const reset = useCallback(() => {
    setValue(name, null);
    singleSelect.current = { text: null, value: null };
  }, [name, setValue]);

  const handleSelect = useCallback(
    (value: IBaseDropdown) => {
      setIsOpen(false);
      setSearchTerm('');
      DSetValue(name, '');
      if (isMultiselect) {
        setMultiselect({ type: EBaseDropdownReducer.CREATE, payload: value });
        // onSelect(multiselect, valueToPass);
        // setValue(
        //   name,
        //   multiselect.map((x: IBaseDropdown) => x.value),
        // );
        singleSelect!.current = value;
        return;
      }

      onSelect(isObject ? value : value.value, valueToPass);
      setValue(name, isObject ? value : value.value);
      if (value?.value === singleSelect?.current?.value) {
        reset();
        onSelect(value.value, valueToPass);
      } else {
        singleSelect!.current = value;
      }
    },
    [isMultiselect, isObject, multiselect, name, onSelect, setValue, valueToPass],
  );

  const mapOptions = useMemo(() => {
    const allOptions = flag && flag.key === flag.value ? options.concat(dynamicData!) : options;
    return enableSearch
      ? allOptions.filter((option: IBaseDropdown) =>
          getTextFromReactNode(option.text).toLowerCase().includes(searchTerm.toLowerCase()),
        )
      : allOptions;
  }, [dynamicData, enableSearch, flag, options, searchTerm]);

  const onclickDeleteSelected = useCallback(
    (e: MouseEvent<HTMLElement>, d: IBaseDropdown) => {
      e.stopPropagation();
      setMultiselect({ type: EBaseDropdownReducer.DELETE, payload: d });
      // onSelect(multiselect, valueToPass);
    },
    [multiselect, onSelect, valueToPass],
  );

  const CInputText = () => {
    return (
      <>
        {enableSearch ? (
          <InputText
            borderRadius='none'
            inputClassName={cn([isOpen ? '' : '', 'h-[25px]'])}
            placeholder={enableSearch ? 'Search...' : ''}
            register={DRegister}
            name={name}
            onChange={(e) => setSearchTerm(e as string)}
            setFocus={DSetFocus}
            readOnly={!enableSearch}
          />
        ) : (
          CText()
        )}
      </>
    );
  };

  const CText = () => {
    return (
      <div
        className={cn([
          'flex items-center text-gray-400 px-[13px]',
          'h-[25px]',
          isMultiselect && multiselect.length && 'h-auto',
          singleSelect!.current?.text && 'text-black',
        ])}
      >
        {!isMultiselect ? singleSelect!.current?.text || placeholder : ''}
      </div>
    );
  };

  return (
    <>
      {label && <label className='label'>{label}</label>}
      <div className='relative flex' ref={menuRef}>
        {buttonLabel ? (
          <div onClick={(e) => toggleMenu(e, true)} className='flex w-full'>
            {buttonLabel}
          </div>
        ) : (
          <div
            className={cn([
              'py-2 flex flex-col flex-1 w-full border rounded-md border-gray-300 active:border-primary-600 focus:border-primary-600 focus-within:border-primary-600 focus-visible:border-primary-600',
            ])}
            onClick={(e) => toggleMenu(e, true)}
          >
            {multiselect?.length ? (
              <div className='flex gap-2 flex-row flex-0 flex-wrap px-2.5' ref={ref}>
                {multiselect.map((x: IBaseDropdown) => {
                  return (
                    <div
                      className='p-1 bg-gray-200 rounded-md relative flex items-center text-xs h-[25px]'
                      key={`multi-${x.value}`}
                    >
                      {x.text}
                      <X
                        className='w-[12px] cursor-pointer'
                        onClick={(e) => onclickDeleteSelected(e, x)}
                      />
                    </div>
                  );
                })}
              </div>
            ) : null}
            {isOpen ? CInputText() : <>{!multiselect?.length ? CText() : null}</>}
          </div>
        )}
        {isOpen && (
          <div
            style={{ top: `${enableSearch && isMultiselect ? `${height + 35}px` : ''}` }}
            className={`origin-top-right absolute mt-2 w-full rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-[200]  ${enableSearch && isMultiselect ? `` : enableSearch ? 'top-[35px]' : 'top-[35px]'}`}
          >
            <div role='menu' aria-orientation='vertical' aria-labelledby='options-menu'>
              {mapOptions.map((option: IBaseDropdown, index: number) => (
                <button
                  key={`${generateID()}-${index}`}
                  className={cn([
                    'flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 w-full',
                    singleSelect.current?.value === option.value && 'bg-gray-100',
                    multiselect?.find((x) => x.value === option.value) && 'bg-gray-100',
                  ])}
                  role='menuitem'
                  onClick={() => handleSelect(option)}
                >
                  {option.text}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>
      <FormError error={errors ? errors[name]?.message : undefined} />
    </>
  );
};

export default Dropdown;
