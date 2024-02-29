/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
    ],
    theme: {
        extend: {
            colors: {
                'corduroy': {
                    '50': '#f6f7f6',
                    '100': '#e3e5e2',
                    '200': '#c5cac5',
                    '300': '#a0a8a0',
                    '400': '#7c857c',
                    '500': '#646e64',
                    '600': '#4d544e',
                    '700': '#3f463f',
                    '800': '#353a35',
                    '900': '#2f322f',
                    '950': '#181b18',
                },
                'blue-chill': {
                    '50': '#f2f9f9',
                    '100': '#ddeff0',
                    '200': '#bfe0e2',
                    '300': '#92cace',
                    '400': '#5faab1',
                    '500': '#438e96',
                    '600': '#3b757f',
                    '700': '#356169',
                    '800': '#325158',
                    '900': '#2d464c',
                    '950': '#1a2c32',
                },
                
            }
        },
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
