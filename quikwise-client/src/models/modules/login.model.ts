import * as yup from 'yup';

export const LoginSchema = yup.object().shape({
  email: yup
    .string()
    .required('Email is a required field')
    .matches(/^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/, 'Email must be correctly'),
  password: yup.string().required('Password is a required field'),
});
