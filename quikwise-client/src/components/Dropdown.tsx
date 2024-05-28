'use client';
import { IBaseDropdown, IDropdownProps } from '@/types';
import { generateID, getTextFromReactNode } from '@/lib/helper';
import { FC, useEffect, useRef, useState } from 'react';
import InputText from '@/components/inputs/Input';
import { unionBy } from 'lodash';
import { X } from 'lucide-react';
import FormError from '@/components/form/FormError';
import { cn } from '@/lib/utils';

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
  setFocus,
}) => {
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef<HTMLDivElement>(null);
  const [searchTerm, setSearchTerm] = useState<string>('');
  const [multiselect, setMultiselect] = useState<IBaseDropdown[]>([]);
  const [height, setHeight] = useState<number>(0);
  const ref = useRef<HTMLInputElement>(null);

  const handleClickOutside = (event: MouseEvent) => {
    if (menuRef.current && !menuRef.current.contains(event.target as Node)) {
      setIsOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, []);

  const toggleMenu = (e: MouseEvent<HTMLElement>, flag?: boolean) => {
    e.stopPropagation();
    setIsOpen((prevIsOpen) => (flag ? flag : !prevIsOpen));
    setFocus(name);
  };

  const handleSelect = (value: IBaseDropdown) => {
    setIsOpen(false);
    setValue(name, value.value);
    if (isMultiselect) {
      setMultiselect((prevState) => unionBy([...prevState, value], 'value'));
      onSelect(multiselect, valueToPass);
      return;
    }
    if (isObject) {
      onSelect(value, valueToPass);
      setSearchTerm(value.text);
      return;
    }
    onSelect(value.value, valueToPass);
    setSearchTerm(value.text);
  };

  const mapOptions = () => {
    const allOptions = flag && flag.key === flag.value ? options.concat(dynamicData!) : options;
    return enableSearch
      ? allOptions.filter((option: IBaseDropdown) => {
          return getTextFromReactNode(option.text).toLowerCase().includes(searchTerm.toLowerCase());
        })
      : allOptions;
  };

  useEffect(() => {
    setHeight(ref.current?.clientHeight || 0);
  }, [isOpen, multiselect]);

  const onclickDeleteSelected = (e: MouseEvent<HTMLElement>, d: IBaseDropdown) => {
    e.stopPropagation();
    setMultiselect((prevState) => prevState.filter((x) => x.value !== d.value));
    onSelect(multiselect, valueToPass);
  };

  return (
    <>
      <div className='relative flex' ref={menuRef}>
        {enableSearch ? (
          <>
            {isMultiselect ? (
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
                {isOpen ? (
                  <InputText
                    borderRadius='none'
                    inputClassName={cn([isOpen ? 'visible' : 'invisible', 'h-[25px]'])}
                    placeholder='Search...'
                    register={register}
                    name={name}
                    errors={errors}
                    onChange={(e) => setSearchTerm(e as string)}
                    setFocus={setFocus}
                  />
                ) : (
                  <>
                    {!multiselect?.length ? (
                      <div className='flex items-center text-gray-400 text-md h-[25px] px-2'>
                        Please select
                      </div>
                    ) : null}
                  </>
                )}
              </div>
            ) : (
              <InputText
                placeholder='Search...'
                register={register}
                name={name}
                errors={errors}
                onChange={(e) => setSearchTerm(e as string)}
                onClick={(e) => toggleMenu(e)}
                setFocus={setFocus}
              />
            )}
          </>
        ) : buttonLabel ? (
          <div onClick={(e) => toggleMenu(e, true)} className='flex w-full'>
            {buttonLabel}
          </div>
        ) : (
          <>
            <InputText
              placeholder={searchTerm}
              register={register}
              name={name}
              errors={errors}
              readOnly
              onClick={(e) => toggleMenu(e)}
              setFocus={setFocus}
            />
          </>
        )}

        {isOpen && (
          <div
            style={{ top: `${enableSearch && isMultiselect ? `${height + 35}px` : ''}` }}
            className={`origin-top-right absolute mt-2 w-full rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 z-[200]  ${enableSearch && isMultiselect ? `` : enableSearch ? 'top-[35px]' : 'top-[35px]'}`}
          >
            <div role='menu' aria-orientation='vertical' aria-labelledby='options-menu'>
              {mapOptions().map((option: IBaseDropdown, index: number) => (
                <button
                  key={`${generateID()}-${index}`}
                  className='flex items-center px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 w-full'
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
