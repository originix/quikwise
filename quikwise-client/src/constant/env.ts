export const isProd = process.env.NODE_ENV === 'production';
export const showLogger = process.env.NEXT_PUBLIC_SHOW_LOGGER === 'true' ?? false;
