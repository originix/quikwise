'use client';
import { FC, useState } from 'react';
import NextImage from '@/components/NextImage';
import InputText from '@/components/inputs/Input';
import { Eye, EyeOff, LockKeyhole, Mail } from 'lucide-react';
import Button from '@/components/buttons/Button';
import { useForm } from 'react-hook-form';
import { IFormLogin } from '@/types';
import { LoginSchema } from '@/models';
import { yupResolver } from '@hookform/resolvers/yup';

const Login: FC = () => {
  const [showPassword, setShowPassword] = useState(false);
  const togglePasswordVisibility = () => setShowPassword(!showPassword);
  const {
    handleSubmit,
    register,
    formState: { errors },
  } = useForm<IFormLogin>({ resolver: yupResolver(LoginSchema) });

  const handleLogin = (params) => {
    // event.preventDefault();
    console.log(params);
    // Implement your authentication logic here
  };

  return (
    <div className='min-h-screen flex flex-col lg:flex-row'>
      <div className='flex-1 flex items-center justify-center bg-white p-8 lg:p-16'>
        <div className='max-w-md w-full space-y-8'>
          <div>
            <div className='flex gap-2 items-center'>
              <NextImage src='/text-logo.webp' alt='Text Logo' width={120} height={120} />
            </div>
            <h2 className='mt-6 text-3xl font-bold text-gray-900'>Log in to your Account</h2>
            <p className='mt-2 text-sm text-gray-600'>Welcome back! Select method to log in:</p>
          </div>
          <div className='flex space-x-4'>
            <Button variant='light' full>
              <NextImage
                className='mr-2 inline'
                src='/icons/google.svg'
                alt='google Logo'
                width={24}
                height={24}
              />{' '}
              Google
            </Button>
            <Button variant='light' full>
              <NextImage
                className='mr-2 inline'
                src='/icons/github.svg'
                alt='github Logo'
                width={24}
                height={24}
              />{' '}
              Github
            </Button>
          </div>
          <div className='relative'>
            <div className='absolute inset-0 flex items-center'>
              <div className='w-full border-t border-gray-300'></div>
            </div>
            <div className='relative flex justify-center text-sm'>
              <span className='px-2 bg-white text-gray-500'>or continue with email</span>
            </div>
          </div>
          <div className='mt-8 space-y-6'>
            <div className='-space-y-px'>
              <div>
                {/*<label htmlFor='email' className='sr-only'>*/}
                {/*  Email*/}
                {/*</label>*/}
                <div className='relative'>
                  <InputText
                    register={register}
                    name='email'
                    errors={errors}
                    type='email'
                    placeholder='you@example.com'
                    icon={Mail}
                  />
                </div>
              </div>
              <div>
                {/*<label htmlFor='password' className='sr-only'>*/}
                {/*  Password*/}
                {/*</label>*/}
                <div className='mt-1 relative'>
                  <InputText
                    register={register}
                    name='password'
                    errors={errors}
                    icon={LockKeyhole}
                    type={showPassword ? 'text' : 'password'}
                    placeholder='Your password'
                  />
                  <div className='absolute inset-y-0 right-0 pr-3 flex items-center'>
                    <button
                      type='button'
                      onClick={togglePasswordVisibility}
                      className='text-gray-500'
                    >
                      {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                    </button>
                  </div>
                </div>
              </div>
            </div>

            <div className='flex items-center justify-between'>
              <div className='flex items-center'>
                <input
                  id='remember_me'
                  name='remember_me'
                  type='checkbox'
                  className='h-4 w-4 text-primary focus:ring-primary-500 border-gray-300 rounded'
                />
                <label htmlFor='remember_me' className='ml-2 block text-sm text-gray-900'>
                  Remember me
                </label>
              </div>
              <div className='text-sm'>
                <a href='#' className='font-medium text-primary'>
                  Forgot Password?
                </a>
              </div>
            </div>

            <div>
              <Button
                onClick={handleSubmit((e) => {
                  handleLogin(e);
                })}
                variant='primary'
                full
                type='submit'
              >
                Login
              </Button>
            </div>
          </div>
          <div className='mt-6 text-center'>
            <a href='#' className='font-medium text-primary'>
              Don't have an account? Create an account
            </a>
          </div>
        </div>
      </div>
      <div className='hidden lg:flex flex-1 items-center justify-center bg-primary-600 text-white p-8'>
        <div className='max-w-md'>
          <h2 className='text-3xl font-bold'>Connect with every application</h2>
          <p className='mt-4 text-lg'>Everything you need in an easily customizable dashboard.</p>
          <NextImage
            src='/images/banner-1.png'
            alt='Illustration'
            width={500}
            height={500}
            className='mt-6'
          />
        </div>
      </div>
    </div>
  );
};

export default Login;
