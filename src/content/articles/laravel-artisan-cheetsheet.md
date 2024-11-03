---
title: Laravel Artisan Cheatsheet
publishDate: 2023-19-04 00:00:00
description: A searchable, bookmark cheatsheet for Laravel's Artisan commands.
image: https://upload.wikimedia.org/wikipedia/commons/thumb/5/51/Drupal_logo_-_gray.png/640px-Drupal_logo_-_gray.png
tags:
  - Tools
  - PHP
  - Development
  - Learn
---


# _complete
Internal command to provide shell completion suggestions

# Options

`api-version - The API version of the completion script` REQUIRED

`current - The index of the "input" array that the cursor is in (e.g. COMP_CWORD)` REQUIRED

`input - An array of input tokens (e.g. COMP_WORDS or argv)` REQUIRED

`shell - The shell type ("bash", "fish", "zsh")` REQUIRED

`symfony - deprecated` REQUIRED
```
    php artisan _complete [-s|--shell SHELL] [-i|--input INPUT] [-c|-
    -current CURRENT] [-a|--api-version API-VERSION] [-S|--symfony
    SYMFONY]

```

Search... Ctrl+K


-----

# clear-compiled
Remove the compiled class file


# db
Start a new database CLI session

# Options

`read - Connect to the read connection` OPTIONAL

`write - Connect to the write connection` OPTIONAL

# Arguments

`connection - The database connection that should be used` OPTIONAL
```
    php artisan db [--read] [--write] [--] [<connection>]

```

# clear-compiled
Remove the compiled class file
```
    php artisan clear-compiled

```

-----

# docs
Access the Laravel documentation


# down
Put the application into maintenance / demo mode

# Options

`redirect - The path that users should be redirected to` OPTIONAL

`refresh - The number of seconds after which the browser may refresh` OPTIONAL

`render - The view that should be prerendered for display during maintenance mode` OPTIONAL

`retry - The number of seconds after which the request may be retried` OPTIONAL

`secret - The secret phrase that may be used to bypass maintenance mode` OPTIONAL
```
    status - The status code that should be used when returning the maintenance mode response

```
OPTIONAL
```
    with-secret - Generate a random secret phrase that may be used to bypass maintenance mode

```
OPTIONAL
```
    php artisan down [--redirect [REDIRECT]] [--render [RENDER]] [-    retry [RETRY]] [--refresh [REFRESH]] [--secret [SECRET]] [--with    secret] [--status [STATUS]]

```

`browse - Open a browser instead of using headless mode` OPTIONAL


# docs
Access the Laravel documentation

# Arguments

`page - The documentation page to open` OPTIONAL

`section - The section of the page to open` OPTIONAL
```
    php artisan docs [<page> [<section>]]

```

-----

# help
Display help for a command

# Options

`format - The output format (txt, xml, json, or md)` REQUIRED

`raw - To output raw command help` OPTIONAL

# Arguments

`command_name - The command name` OPTIONAL
```
    php artisan help [--format FORMAT] [--raw] [--] [<command_name>]

```

# horizon
Start a master supervisor in the foreground

# Options

`environment - The environment name` OPTIONAL


-----

# list
List commands

# Options

`format - The output format (txt, xml, json, or md)` REQUIRED

`raw - To output raw command list` OPTIONAL

`short - To skip describing commands' arguments` OPTIONAL

# Arguments

`namespace - The namespace name` OPTIONAL
```
    php artisan list [--raw] [--format FORMAT] [--short] [--]

```

# inspire
Display an inspiring quote
```
    php artisan inspire

```

-----

# migrate
Run the database migrations

# Options

`database - The database connection to use` OPTIONAL

`force - Force the operation to run when in production` OPTIONAL

`graceful - Return a successful exit code even if an error occurs` OPTIONAL
```
    isolated - Do not run the command if another instance of the command is already running

```
OPTIONAL

`path - The path(s) to the migrations files to be executed` OPTIONAL

`pretend - Dump the SQL queries that would be run` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL

`schema-path - The path to a schema dump file` OPTIONAL

`seed - Indicates if the seed task should be re-run` OPTIONAL

`seeder - The class name of the root seeder` OPTIONAL

`step - Force the migrations to be run so they can be rolled back individually` OPTIONAL
```
    php artisan migrate [--database [DATABASE]] [--force] [--path
    [PATH]] [--realpath] [--schema-path [SCHEMA-PATH]] [--pretend] [-
    -seed] [--seeder [SEEDER]] [--step] [--graceful] [--isolated
    [ISOLATED]]

```

-----

# pail
Tails the application logs.


# pail
Tails the application logs.

# Options

`auth - Filter the logs by the given authenticated ID` OPTIONAL

`filter - Filter the logs by the given value` OPTIONAL

`level - Filter the logs by the given level` OPTIONAL

`message - Filter the logs by the given message` OPTIONAL

`timeout - The maximum execution time in seconds` OPTIONAL

`user - Filter the logs by the given authenticated ID (alias for --auth)` OPTIONAL
```
    php artisan pail [--filter [FILTER]] [--message [MESSAGE]] [-    level [LEVEL]] [--auth [AUTH]] [--user [USER]] [--timeout
    [TIMEOUT]]

```

`compact - Indicates whether the compact printer should be used` OPTIONAL


# serve
Serve the application on the PHP development server

# Options

`host - The host address to serve the application on` OPTIONAL

`no-reload - Do not reload the development server on .env file changes` OPTIONAL

`port - The port to serve the application on` OPTIONAL

`tries - The max number of ports to attempt to serve from` OPTIONAL
```
    php artisan serve [--host [HOST]] [--port [PORT]] [--tries
    [TRIES]] [--no-reload]

```

-----

`drop-databases - Indicates if the test databases should be dropped` OPTIONAL


`drop-databases - Indicates if the test databases should be dropped` OPTIONAL

`min - Indicates the minimum threshold enforcement for code coverage` OPTIONAL

`parallel - Indicates if the tests should run in parallel` OPTIONAL

`profile - Lists top 10 slowest tests` OPTIONAL

`recreate-databases - Indicates if the test databases should be re-created` OPTIONAL

`without-databases - Indicates if database configuration should be performed` OPTIONAL

`without-tty - Disable output to TTY` OPTIONAL
```
    php artisan test [--without-tty] [--compact] [--coverage] [--min
    [MIN]] [-p|--parallel] [--profile] [--recreate-databases] [--
    drop-databases] [--without-databases]

```

# ui
Swap the front-end scaffolding for the application

# Options

`auth - Install authentication UI scaffolding` OPTIONAL

`option - Pass an option to the preset command` OPTIONAL

# Arguments

`type - The preset type (bootstrap, vue, react)` REQUIRED


-----

# auth:clear-resets
Flush expired password reset tokens

# Arguments

`name - The name of the password broker` OPTIONAL
```
    php artisan auth:clear-resets [<name>]

```
```
    php artisan ui [--auth] [--option [OPTION]] [--] <type>

```

# Arguments


# breeze:install
Install the Breeze controllers and resources

# Options
```
    composer - Absolute path to the Composer binary which should be used to install packages

```
OPTIONAL

`dark - Indicate that dark mode support should be installed` OPTIONAL

`eslint - Indicates if ESLint with Prettier should be installed` OPTIONAL

`pest - Indicate that Pest should be installed` OPTIONAL

`ssr - Indicates if Inertia SSR support should be installed` OPTIONAL

`typescript - Indicates if TypeScript is preferred for the Inertia stack` OPTIONAL

# Arguments


-----

functional,react,vue,api) REQUIRED


# cache:clear
Flush the application cache

# Options

`tags - The cache tags you would like to clear` OPTIONAL

# Arguments

`store - The name of the store you would like to clear` OPTIONAL
```
    php artisan cache:clear [--tags [TAGS]] [--] [<store>]

```

functional,react,vue,api) REQUIRED
```
    php artisan breeze:install [--dark] [--pest] [--ssr] [--
    typescript] [--eslint] [--composer [COMPOSER]] [--] <stack>

```

-----

# Arguments


# cashier:webhook
Create the Stripe webhook to interact with Cashier.

# Options

`api-version - The Stripe API version the webhook should use` OPTIONAL

`disabled - Immediately disable the webhook after creation` OPTIONAL

`url - The URL endpoint for the webhook` OPTIONAL
```
    php artisan cashier:webhook [--disabled] [--url [URL]] [--api-
    version [API-VERSION]]

```

# Arguments

`store - The name of the store you would like to prune tags from` OPTIONAL
```
    php artisan cache:prune-stale-tags [<store>]

```

-----

# config:clear
Remove the configuration cache file


# config:publish
Publish configuration files to your application

# Options

`all - Publish all configuration files` OPTIONAL

`force - Overwrite any existing configuration files` OPTIONAL

# Arguments

`name - The name of the configuration file to publish` OPTIONAL
```
    php artisan config:publish [--all] [--force] [--] [<name>]

```

# config:clear
Remove the configuration cache file
```
    php artisan config:clear

```

-----

# Options


# db:seed
Seed the database with records

# Options

`class - The class name of the root seeder` OPTIONAL

`database - The database connection to seed` OPTIONAL

`force - Force the operation to run when in production` OPTIONAL

# Arguments

`class - The class name of the root seeder` OPTIONAL
```
    php artisan db:seed [--class [CLASS]] [--database [DATABASE]] [--
    force] [--] [<class>]

```

# Options

`databases - The database connections to monitor` OPTIONAL
```
    max - The maximum number of connections that can be open before an event is dispatched

```
OPTIONAL
```
    php artisan db:monitor [--databases [DATABASES]] [--max [MAX]]

```

-----

# db:table
Display information about the given database table

# Options

`database - The database connection` OPTIONAL

`json - Output the table information as JSON` OPTIONAL

# Arguments

`table - The name of the table` OPTIONAL
```
    php artisan db:table [--database [DATABASE]] [--json] [--]
    [<table>]

```
```
    php artisan db:show [--database [DATABASE]] [--json] [--counts]
    [--views] [--types]

```

-----

# Options

`all - Install a ChromeDriver binary for every OS` OPTIONAL

`detect - Detect the installed Chrome / Chromium version` OPTIONAL

`proxy - The proxy to download the binary through (example: "tcp://127.0.0.1:9000")` OPTIONAL

`ssl-no-verify - Bypass SSL certificate verification when installing through a proxy` OPTIONAL

# Arguments

`version -` OPTIONAL
```
    php artisan dusk:chrome-driver [--all] [--detect] [--proxy
    [PROXY]] [--ssl-no-verify] [--] [<version>]

```

# dusk:fails
Run the failing Dusk tests from the last run and stop on failure

# Options

`browse - Open a browser instead of using headless mode` OPTIONAL

`pest - Run the tests using Pest` OPTIONAL

`without-tty - Disable output to TTY` OPTIONAL
```
    php artisan dusk:fails [--browse] [--without-tty] [--pest]

```

-----

# dusk:install
Install Dusk into the application

# Options

`proxy - The proxy to download the binary through (example: "tcp://127.0.0.1:9000")` OPTIONAL

`ssl-no-verify - Bypass SSL certificate verification when installing through a proxy` OPTIONAL
```
    php artisan dusk:install [--proxy [PROXY]] [--ssl-no-verify]

```

# dusk:page
Create a new Dusk page class

# Arguments

`name - The name of the class` REQUIRED
```
    php artisan dusk:page <name>

```

-----

# dusk:purge
Purge dusk test debugging files

|SSppoonnssoorr aarrttiissaann..ppaaggee|33|
|---|---|


# env:decrypt
Decrypt an environment file

# Options

`cipher - The encryption cipher` OPTIONAL

`env - The environment to be decrypted` OPTIONAL

`filename - Filename of the decrypted file` OPTIONAL

`force - Overwrite the existing environment file` OPTIONAL

`key - The encryption key` OPTIONAL

`path - Path to write the decrypted file` OPTIONAL
```
    php artisan env:decrypt [--key [KEY]] [--cipher [CIPHER]] [--env
    [ENV]] [--force] [--path [PATH]] [--filename [FILENAME]]

```

# dusk:purge
Purge dusk test debugging files
```
    php artisan dusk:purge

## API 11.x Sponsor artisan.pageSponsor artisan.page 33

```

-----

# event:list
List the application's events and listeners

# Options

`event - Filter the events by name` OPTIONAL
```
    php artisan event:list [--event [EVENT]]

```

# event:cache
Discover and cache the application's events and listeners
```
    php artisan event:cache

```

-----

# fortify:install
Install all of the Fortify resources


# horizon:clear
Delete all of the jobs from the specified queue

# Options

`force - Force the operation to run when in production` OPTIONAL

`queue - The name of the queue to clear` OPTIONAL
```
    php artisan horizon:clear [--queue [QUEUE]] [--force]

```

# horizon:continue
Instruct the master supervisor to continue processing jobs
```
    php artisan horizon:continue

```

-----

# horizon:continue-supervisor
Instruct the supervisor to continue processing jobs


# horizon:forget
Delete a failed queue job

# Options

`all - Delete all failed jobs` OPTIONAL

# Arguments

`id - The ID of the failed job` OPTIONAL
```
    php artisan horizon:forget [--all] [--] [<id>]

```

# horizon:install
Install all of the Horizon resources
```
    php artisan horizon:install

```

-----

# horizon:pause-supervisor
Pause a supervisor

# Arguments

`name - The name of the supervisor to pause` REQUIRED
```
    php artisan horizon:pause-supervisor <name>

```

# horizon:publish
Publish all of the Horizon resources
```
    php artisan horizon:publish

```

# horizon:purge
Terminate any rogue Horizon processes


-----

# Options


# horizon:snapshot
Store a snapshot of the queue metrics
```
    php artisan horizon:snapshot

```

# Options

`signal - The signal to send to the rogue processes` OPTIONAL
```
    php artisan horizon:purge [--signal [SIGNAL]]

```

`delay` The number of seconds to delay failed jobs (Deprecated) OPTIONAL


# horizon:supervisor
Start a new supervisor

# Options

`auto-scaling-strategy - If supervisor should scale by jobs or time to complete` OPTIONAL
```
    backoff - The number of seconds to wait before retrying a job that encountered an uncaught

```
exception OPTIONAL

`balance - The balancing strategy the supervisor should apply` OPTIONAL
```
    balance-cooldown - The number of seconds to wait in between auto-scaling attempts

```
OPTIONAL
```
    balance-max-shift - The maximum number of processes to increase or decrease per one

```
scaling OPTIONAL

The number of seconds to delay failed jobs (Deprecated) OPTIONAL


-----

`max-jobs - The number of jobs to process before stopping a child process` OPTIONAL


`max-jobs - The number of jobs to process before stopping a child process` OPTIONAL

`max-processes - The maximum number of total workers to start` OPTIONAL

`max-time - The maximum number of seconds a child process should run` OPTIONAL

`memory - The memory limit in megabytes` OPTIONAL

`min-processes - The minimum number of workers to assign per queue` OPTIONAL

`nice - The process priority` OPTIONAL

`parent-id - The parent process ID` OPTIONAL

`paused - Start the supervisor in a paused state` OPTIONAL

`queue - The names of the queues to work` OPTIONAL

`rest - Number of seconds to rest between jobs` OPTIONAL

`sleep - Number of seconds to sleep when no job is available` OPTIONAL

`timeout - The number of seconds a child process can run` OPTIONAL

`tries - Number of times to attempt a job before logging it failed` OPTIONAL

`workers-name - The name that should be assigned to the workers` OPTIONAL

# Arguments

`name - The name of supervisor` REQUIRED

`connection - The name of the connection to work` REQUIRED
```
    php artisan horizon:supervisor [--balance [BALANCE]] [--delay
    [DELAY]] [--backoff [BACKOFF]] [--max-jobs [MAX-JOBS]] [--max-
    time [MAX-TIME]] [--force] [--max-processes [MAX-PROCESSES]] [--
    min-processes [MIN-PROCESSES]] [--memory [MEMORY]] [--nice
    [NICE]] [--paused] [--queue [QUEUE]] [--sleep [SLEEP]] [--timeout
    [TIMEOUT]] [--tries [TRIES]] [--auto-scaling-strategy [AUTO-
    SCALING-STRATEGY]] [--balance-cooldown [BALANCE-COOLDOWN]] [--
    balance-max-shift [BALANCE-MAX-SHIFT]] [--workers-name [WORKERS-
    NAME]] [--parent-id [PARENT-ID]] [--rest [REST]] [--] <name>
    <connection>

```

-----

# horizon:terminate
Terminate the master supervisor so it can be restarted

# Options

`wait - Wait for all workers to terminate` OPTIONAL
```
    php artisan horizon:terminate [--wait]

```

# horizon:supervisors
List all of the supervisors
```
    php artisan horizon:supervisors

```

# O ti


# horizon:timeout
Get the maximum timeout for the given environment

# Arguments

`environment - The environment name` OPTIONAL
```
    php artisan horizon:timeout [<environment>]

```

-----

exception OPTIONAL


exception OPTIONAL

`daemon - Run the worker in daemon mode (Deprecated)` OPTIONAL

`delay - The number of seconds to delay failed jobs (Deprecated)` OPTIONAL

`force - Force the worker to run even in maintenance mode` OPTIONAL

`max-jobs - The number of jobs to process before stopping` OPTIONAL

`max-time - The maximum number of seconds the worker should run` OPTIONAL

`memory - The memory limit in megabytes` OPTIONAL

`name - The name of the worker` OPTIONAL

`once - Only process the next job on the queue` OPTIONAL

`queue - The names of the queues to work` OPTIONAL

`rest - Number of seconds to rest between jobs` OPTIONAL

`sleep - Number of seconds to sleep when no job is available` OPTIONAL

`stop-when-empty - Stop when the queue is empty` OPTIONAL

`supervisor - The name of the supervisor the worker belongs to` OPTIONAL

`timeout - The number of seconds a child process can run` OPTIONAL

`tries - Number of times to attempt a job before logging it failed` OPTIONAL

# Arguments

`connection - The name of the queue connection to work` OPTIONAL
```
    php artisan horizon:work [--name [NAME]] [--delay [DELAY]] [--
    backoff [BACKOFF]] [--max-jobs [MAX-JOBS]] [--max-time [MAX-
    TIME]] [--daemon] [--force] [--memory [MEMORY]] [--once] [--stop-
    when-empty] [--queue [QUEUE]] [--sleep [SLEEP]] [--rest [REST]]
    [--supervisor [SUPERVISOR]] [--timeout [TIMEOUT]] [--tries
    [TRIES]] [--] [<connection>]

```

-----

# install:api
Create an API routes file and install Laravel Sanctum or Laravel Passport

# Options
```
    composer - Absolute path to the Composer binary which should be used to install packages

```
OPTIONAL

`force - Overwrite any existing API routes file` OPTIONAL

`passport - Install Laravel Passport instead of Laravel Sanctum` OPTIONAL

`without-migration-prompt - Do not prompt to run pending migrations` OPTIONAL
```
    php artisan install:api [--composer [COMPOSER]] [--force] [--
    passport] [--without-migration-prompt]

```

# inertia:stop-ssr
Stop the Inertia SSR server
```
    php artisan inertia:stop-ssr

```

-----

# install:broadcasting
Create a broadcasting channel routes file


# jetstream:install
Install the Jetstream components and resources

# Options

`api - Indicates if API support should be installed` OPTIONAL
```
    composer - Absolute path to the Composer binary which should be used to install packages

```
OPTIONAL

`dark - Indicate that dark mode support should be installed` OPTIONAL

`pest - Indicates if Pest should be installed` OPTIONAL

`ssr - Indicates if Inertia SSR support should be installed` OPTIONAL

`teams - Indicates if team support should be installed` OPTIONAL

`verification - Indicates if email verification support should be installed` OPTIONAL

# Arguments

`stack - The development stack that should be installed (inertia,livewire)` REQUIRED
```
    php artisan jetstream:install [--dark] [--teams] [--api] [--
    verification] [--pest] [--ssr] [--composer [COMPOSER]] [--]
    <stack>

```

-----

# key:generate
Set the application key


# livewire:attribute
Create a new Livewire attribute class

# Options

`force -` OPTIONAL

# Arguments

`name -` REQUIRED
```
    php artisan livewire:attribute [--force] [--] <name>

```

# key:generate
Set the application key

# Options

`force - Force the operation to run when in production` OPTIONAL

`show - Display the key instead of modifying files` OPTIONAL
```
    php artisan key:generate [--show] [--force]

```

-----

# livewire:configure-s3-upload-cleanup
Configure temporary file upload s3 directory to automatically cleanup files older than 24hrs


# livewire:copy
Copy a Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

`test -` OPTIONAL

# Arguments

`name -` REQUIRED

`new-name -` REQUIRED
```
    php artisan livewire:copy [--inline] [--force] [--test] [--]
    <name> <new-name>

```

# livewire:configure-s3-upload-cleanup
Configure temporary file upload s3 directory to automatically cleanup files older than 24hrs
```
    php artisan livewire:configure-s3-upload-cleanup

```

-----

# livewire:delete
Delete a Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

`test -` OPTIONAL

# Arguments

`name -` REQUIRED
```
    php artisan livewire:delete [--inline] [--force] [--test] [--]
    <name>

```
```
    php artisan livewire:cp [--inline] [--force] [--test] [--] <name>
    <new-name>

```

# livewire:layout


# livewire:form
Create a new Livewire form class

# Options

`force -` OPTIONAL

# Arguments

`name -` REQUIRED
```
    php artisan livewire:form [--force] [--] <name>

```

-----

# livewire:make
Create a new Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

`pest -` OPTIONAL

`stub - If you have several stubs, stored in subfolders` OPTIONAL

`test -` OPTIONAL

# Arguments

`name -` REQUIRED
```
    php artisan livewire:make [--force] [--inline] [--test] [--pest]
    [--stub [STUB]] [--] <name>

```

# livewire:move
Move a Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

# Arguments

`name -` REQUIRED


-----

# livewire:mv
Move a Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

# Arguments

`name -` REQUIRED

`new-name -` REQUIRED
```
    php artisan livewire:mv [--inline] [--force] [--] <name> <new-
    name>

```
```
    php artisan livewire:move [--force] [--inline] [--] <name> <new-
    name>

```

-----

# livewire:rm
Delete a Livewire component


# livewire:rm
Delete a Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

`test -` OPTIONAL

# Arguments

`name -` REQUIRED
```
    php artisan livewire:rm [--inline] [--force] [--test] [--] <name>

```

# livewire:stubs
Publish Livewire stubs
```
    php artisan livewire:stubs

```

-----

# make:cast
Create a new custom Eloquent cast class

# Options

`force - Create the class even if the cast already exists` OPTIONAL

`inbound - Generate an inbound cast class` OPTIONAL

# Arguments

`name - The name of the cast` REQUIRED
```
    php artisan make:cast [-f|--force] [--inbound] [--] <name>

```

# make:cache-table
Create a migration for the cache database table
```
    php artisan make:cache-table

```

-----

# make:channel
Create a new channel class


# make:class
Create a new class

# Options

`force - Create the class even if the class already exists` OPTIONAL

`invokable - Generate a single method, invokable class` OPTIONAL

# Arguments

`name - The name of the class` REQUIRED
```
    php artisan make:class [-i|--invokable] [-f|--force] [--] <name>

```

# make:command
Create a new Artisan command

# Options

`command - The terminal command that will be used to invoke the class` OPTIONAL

`force - Create the class even if the console command already exists` OPTIONAL

`pest - Generate an accompanying Pest test for the Console command` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Console command` OPTIONAL

`test - Generate an accompanying Test test for the Console command` OPTIONAL


-----

# make:component
Create a new view component class

# Options

`force - Create the class even if the component already exists` OPTIONAL

`inline - Create a component that renders an inline view` OPTIONAL

`path - The location where the component view should be created` REQUIRED

`pest - Generate an accompanying Pest test for the Component` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Component` OPTIONAL

`test - Generate an accompanying Test test for the Component` OPTIONAL

`view - Create an anonymous component with only a view` OPTIONAL

# Arguments

`name - The name of the component` REQUIRED
```
    php artisan make:component [--inline] [--view] [--path PATH] [-
    f|--force] [--test] [--pest] [--phpunit] [--] <name>

```
```
    php artisan make:command [-f|--force] [--command [COMMAND]] [--
    test] [--pest] [--phpunit] [--] <name>

```

-----

`requests - Generate FormRequest classes for store and update` OPTIONAL


# make:enum
Create a new enum

# Options

`force - Create the enum even if the enum already exists` OPTIONAL

`int - Generate an integer backed enum.` OPTIONAL

`string - Generate a string backed enum.` OPTIONAL

# Arguments

`name - The name of the enum` REQUIRED
```
    php artisan make:enum [-s|--string] [-i|--int] [-f|--force] [--]
    <name>

```

# make:event
Create a new event class

# Options

`force - Create the class even if the event already exists` OPTIONAL


-----

# make:exception
Create a new custom exception class

# Options

`force - Create the class even if the exception already exists` OPTIONAL

`render - Create the exception with an empty render method` OPTIONAL

`report - Create the exception with an empty report method` OPTIONAL

# Arguments

`name - The name of the exception` REQUIRED
```
    php artisan make:exception [-f|--force] [--render] [--report] [-
    -] <name>

```
```
    php artisan make:event [-f|--force] [--] <name>

```

-----

# make:job
Create a new job class

# Options

`force - Create the class even if the job already exists` OPTIONAL

`pest - Generate an accompanying Pest test for the Job` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Job` OPTIONAL

`sync - Indicates that job should be synchronous` OPTIONAL

`test - Generate an accompanying Test test for the Job` OPTIONAL

# Arguments

`name - The name of the job` REQUIRED
```
    php artisan make:job [-f|--force] [--sync] [--test] [--pest] [-    phpunit] [--] <name>

```

f h ddl


# Options

`force - Create the interface even if the interface already exists` OPTIONAL

# Arguments

`name - The name of the interface` REQUIRED
```
    php artisan make:interface [-f|--force] [--] <name>

```

-----

# make:listener
Create a new event listener class

# Options

`event - The event class being listened for` OPTIONAL

`force - Create the class even if the listener already exists` OPTIONAL

`pest - Generate an accompanying Pest test for the Listener` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Listener` OPTIONAL

`queued - Indicates the event listener should be queued` OPTIONAL

`test - Generate an accompanying Test test for the Listener` OPTIONAL

# Arguments

`name - The name of the listener` REQUIRED
```
    php artisan make:listener [-e|--event [EVENT]] [-f|--force] [-    queued] [--test] [--pest] [--phpunit] [--] <name>

```

`name - The name of the middleware` REQUIRED
```
    php artisan make:job-middleware [-f|--force] [--test] [--pest] [    -phpunit] [--] <name>

```

# Arguments


# make:livewire
Create a new Livewire component

# Options

`force -` OPTIONAL

`inline -` OPTIONAL

`pest -` OPTIONAL

`stub -` OPTIONAL

`test -` OPTIONAL

# Arguments


-----

# make:mail
Create a new email class

# Options

`force - Create the class even if the mailable already exists` OPTIONAL

`markdown - Create a new Markdown template for the mailable` OPTIONAL

`pest - Generate an accompanying Pest test for the Mailable` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Mailable` OPTIONAL

`test - Generate an accompanying Test test for the Mailable` OPTIONAL

`view - Create a new Blade template for the mailable` OPTIONAL

# Arguments

`name - The name of the mailable` REQUIRED
```
    php artisan make:mail [-f|--force] [-m|--markdown [MARKDOWN]] [--
    view [VIEW]] [--test] [--pest] [--phpunit] [--] <name>

```
```
    php artisan make:livewire [--force] [--inline] [--test] [--pest]
    [--stub [STUB]] [--] <name>

```

-----

# make:migration
Create a new migration file

# Options

`create - The table to be created` OPTIONAL

`fullpath - Output the full path of the migration (Deprecated)` OPTIONAL

`path - The location where the migration file should be created` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL

`table - The table to migrate` OPTIONAL

# Arguments

`name - The name of the migration` REQUIRED
```
    php artisan make:migration [--create [CREATE]] [--table [TABLE]]
    [--path [PATH]] [--realpath] [--fullpath] [--] <name>

```
```
    php artisan make:middleware [--test] [--pest] [--phpunit] [--]
    <name>

```

-----

```
pivot - Indicates if the generated model should be a custom intermediate table model

```

# make:notification
Create a new notification class

# Options

`force - Create the class even if the notification already exists` OPTIONAL

`markdown - Create a new Markdown template for the notification` OPTIONAL

`pest - Generate an accompanying Pest test for the Notification` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Notification` OPTIONAL

`test - Generate an accompanying Test test for the Notification` OPTIONAL

# Arguments

`name - The name of the notification` REQUIRED
```
    php artisan make:notification [-f|--force] [-m|--markdown
    [MARKDOWN]] [--test] [--pest] [--phpunit] [--] <name>

```

# make:notifications-table
Create a migration for the notifications table

```
    pivot - Indicates if the generated model should be a custom intermediate table model

```
OPTIONAL

`policy - Create a new policy for the model` OPTIONAL

`requests - Create new form request classes and use them in the resource controller` OPTIONAL

`resource - Indicates if the generated controller should be a resource controller` OPTIONAL

`seed - Create a new seeder for the model` OPTIONAL

`test - Generate an accompanying Test test for the Model` OPTIONAL

# Arguments

`name - The name of the model` REQUIRED
```
    php artisan make:model [-a|--all] [-c|--controller] [-f|--
    factory] [--force] [-m|--migration] [--morph-pivot] [--policy] [-
    s|--seed] [-p|--pivot] [-r|--resource] [--api] [-R|--requests] [-
    -test] [--pest] [--phpunit] [--] <name>

```

-----

# make:policy
Create a new policy class

# Options

`force - Create the class even if the policy already exists` OPTIONAL

`guard - The guard that the policy relies on` OPTIONAL

`model - The model that the policy applies to` OPTIONAL

# Arguments

`name - The name of the policy` REQUIRED
```
    php artisan make:policy [-f|--force] [-m|--model [MODEL]] [-g|--
    guard [GUARD]] [--] <name>

```
```
    php artisan make:notifications-table

```

-----

# make:provider
Create a new service provider class


# make:provider
Create a new service provider class

# Options

`force - Create the class even if the provider already exists` OPTIONAL

# Arguments

`name - The name of the provider` REQUIRED
```
    php artisan make:provider [-f|--force] [--] <name>

```

# make:queue-failed-table
Create a migration for the failed queue jobs database table
```
    php artisan make:queue-failed-table

```

-----

# make:request
Create a new form request class


# make:resource
Create a new resource

# Options

`collection - Create a resource collection` OPTIONAL

`force - Create the class even if the resource already exists` OPTIONAL

# Arguments

`name - The name of the resource` REQUIRED
```
    php artisan make:resource [-f|--force] [-c|--collection] [--]
    <name>

```

# make:rule
Create a new validation rule

# Options

`force - Create the class even if the rule already exists` OPTIONAL

`implicit - Generate an implicit rule` OPTIONAL

# Arguments

`name - The name of the rule` REQUIRED


-----

# make:scope
Create a new scope class

# Options

`force - Create the class even if the scope already exists` OPTIONAL

# Arguments

`name - The name of the scope` REQUIRED
```
    php artisan make:scope [-f|--force] [--] <name>

```

# make:session-table
Create a migration for the session database table
```
    php artisan make:session-table

```

-----

# make:test
Create a new test class


# make:test
Create a new test class

# Options

`force - Create the test even if the test already exists` OPTIONAL

`pest - Create a Pest test` OPTIONAL

`phpunit - Create a PHPUnit test` OPTIONAL

`unit - Create a unit test` OPTIONAL

# Arguments

`name - The name of the test` REQUIRED
```
    php artisan make:test [-f|--force] [-u|--unit] [--pest] [-    phpunit] [--] <name>

```

`pest - Generate an accompanying Pest test for the View` OPTIONAL


# make:trait
Create a new trait

# Options

`force - Create the trait even if the trait already exists` OPTIONAL

# Arguments

`name - The name of the trait` REQUIRED
```
    php artisan make:trait [-f|--force] [--] <name>

```

-----

`test - Generate an accompanying Test test for the View` OPTIONAL


# make:volt
Create a new Volt component

# Options

`class - Create a class based component` OPTIONAL

`force - Create the Volt component even if the component already exists` OPTIONAL

`functional - Create a functional component` OPTIONAL

`pest - Generate an accompanying Pest test for the Volt component` OPTIONAL

`phpunit - Generate an accompanying PHPUnit test for the Volt component` OPTIONAL

`test - Generate an accompanying Test test for the Volt component` OPTIONAL

# Arguments

`name - The name of the volt component` REQUIRED
```
    php artisan make:volt [--class] [--functional] [-f|--force] [-    test] [--pest] [--phpunit] [--] <name>

```

`force - Force the operation to run when in production` OPTIONAL


`test - Generate an accompanying Test test for the View` OPTIONAL

# Arguments

`name - The name of the view` REQUIRED
```
    php artisan make:view [--extension [EXTENSION]] [-f|--force] [--
    test] [--pest] [--phpunit] [--] <name>

```

-----

OPTIONAL


# migrate:refresh
Reset and re-run all migrations

# Options

`database - The database connection to use` OPTIONAL

`force - Force the operation to run when in production` OPTIONAL

`path - The path(s) to the migrations files to be executed` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL

`seed - Indicates if the seed task should be re-run` OPTIONAL

`seeder - The class name of the root seeder` OPTIONAL

`step - The number of migrations to be reverted & re-run` OPTIONAL


# migrate:install
Create the migration repository

# Options

`database - The database connection to use` OPTIONAL
```
    php artisan migrate:install [--database [DATABASE]]

```

-----

# migrate:reset
Rollback all database migrations

# Options

`database - The database connection to use` OPTIONAL

`force - Force the operation to run when in production` OPTIONAL

`path - The path(s) to the migrations files to be executed` OPTIONAL

`pretend - Dump the SQL queries that would be run` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL
```
    php artisan migrate:reset [--database [DATABASE]] [--force] [-    path [PATH]] [--realpath] [--pretend]

```
```
    php artisan migrate:refresh [--database [DATABASE]] [--force] [-    path [PATH]] [--realpath] [--seed] [--seeder [SEEDER]] [--step
    [STEP]]

```
```
php artisan migrate:rollback [--database [DATABASE]] [--force] [
```

# migrate:rollback
Rollback the last database migration

# Options

`batch - The batch of migrations (identified by their batch number) to be reverted` REQUIRED

`database - The database connection to use` OPTIONAL

`force - Force the operation to run when in production` OPTIONAL

`path - The path(s) to the migrations files to be executed` OPTIONAL

`pretend - Dump the SQL queries that would be run` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL

`step - The number of migrations to be reverted` OPTIONAL
```
    php artisan migrate:rollback [--database [DATABASE]] [--force] [-

```

-----

# model:prune
Prune models that are no longer needed

# Options

`chunk - The number of models to retrieve per chunk of models to be deleted` OPTIONAL

`except - Class names of the models to be excluded from pruning` OPTIONAL

`model - Class names of the models to be pruned` OPTIONAL

`path - Absolute path(s) to directories where models are located` OPTIONAL

`pretend - Display the number of prunable records found instead of deleting them` OPTIONAL
```
    php artisan model:prune [--model [MODEL]] [--except [EXCEPT]] [-    path [PATH]] [--chunk [CHUNK]] [--pretend]

```

# model:show
Sh i f ti b t El t d l


# migrate:status
Show the status of each migration

# Options

`database - The database connection to use` OPTIONAL

`path - The path(s) to the migrations files to use` OPTIONAL

`pending - Only list pending migrations` OPTIONAL
```
    realpath - Indicate any provided migration file paths are pre-resolved absolute paths

```
OPTIONAL
```
    php artisan migrate:status [--database [DATABASE]] [--pending
    [PENDING]] [--path [PATH]] [--realpath]

```

-----

# Options


# nova:action
Create a new action class

# Options

`destructive - Indicate that the action deletes / destroys resources` OPTIONAL

`queued - Indicates the action should be queued` OPTIONAL

# Arguments

`name - The name of the action` REQUIRED
```
    php artisan nova:action [--destructive] [--queued] [--] <name>

```

# nova:asset
Create a new asset

# Arguments

`name -` REQUIRED
```
    php artisan nova:asset <name>

```

-----

# nova:base-resource
Create a new base resource class


# nova:card
Create a new card

# Arguments

`name -` REQUIRED
```
    php artisan nova:card <name>

```

# nova:check-license
Verify your Nova license key
```
    php artisan nova:check-license

```

-----

# nova:dashboard
Create a new dashboard.

# Arguments

`name -` REQUIRED
```
    php artisan nova:dashboard <name>

```

# nova:filter
Create a new filter class

# Options

`boolean - Indicates if the generated filter should be a boolean filter` OPTIONAL

`date - Indicates if the generated filter should be a date filter` OPTIONAL

# Arguments

`name - The name of the filter` REQUIRED


-----

# nova:lens
Create a new lens class

# Arguments

`name - The name of the lens` REQUIRED
```
    php artisan nova:lens <name>

```

# nova:install
Install all of the Nova resources
```
    php artisan nova:install

```

-----

# nova:progress
Create a new metric (progress) class


# nova:repeatable
Create a new repeatable class

# Options

`model - The model class being represented.` REQUIRED

# Arguments

`name - The name of the repeatable` REQUIRED
```
    php artisan nova:repeatable [-m|--model MODEL] [--] <name>

```

# nova:progress
Create a new metric (progress) class

# Arguments

`name - The name of the metric` REQUIRED
```
    php artisan nova:progress <name>

```

-----

# nova:resource-tool
Create a new resource tool

# Arguments

`name -` REQUIRED
```
    php artisan nova:resource-tool <name>

```

# Options

`model - The model class being represented.` REQUIRED

# Arguments

`name - The name of the resource` REQUIRED
```
    php artisan nova:resource [-m|--model MODEL] [--] <name>

```

-----

# Arguments


# nova:translate
Create translation files for Nova

# Options

`force - Overwrite any existing files` OPTIONAL

# Arguments

`language -` REQUIRED
```
    php artisan nova:translate [--force] [--] <language>

```

# Arguments

`name - The name of the metric` REQUIRED
```
    php artisan nova:table <name>

```

-----

# nova:value
Create a new metric (single value) class

# Arguments

`name - The name of the metric` REQUIRED
```
    php artisan nova:value <name>

```

# nova:user
Create a new user
```
    php artisan nova:user

```

# octane:frankenphp
Start the Octane FrankenPHP server


# nova:upgrade
Upgrade Laravel Nova 3 to 4
```
    php artisan nova:upgrade

```

# octane:frankenphp
Start the Octane FrankenPHP server


-----

# Options


# Options

`admin-host - The host the admin server should be available on` OPTIONAL

`admin-port - The port the admin server should be available on` OPTIONAL

`caddyfile - The path to the FrankenPHP Caddyfile file` OPTIONAL

`host - The IP address the server should bind to` OPTIONAL
```
    http-redirect - Enable HTTP to HTTPS redirection (only enabled if --https is passed)

```
OPTIONAL
```
    https - Enable HTTPS, HTTP/2, and HTTP/3, and automatically generate and renew certificates

```
OPTIONAL

`log-level - Log messages at or above the specified log level` OPTIONAL

`max-requests - The number of requests to process before reloading the server` OPTIONAL

`poll - Use file system polling while watching in order to watch files over a network` OPTIONAL

`port - The port the server should be available on` OPTIONAL

`watch - Automatically reload the server when the application is modified` OPTIONAL

`workers - The number of workers that should be available to handle requests` OPTIONAL
```
    php artisan octane:frankenphp [--host [HOST]] [--port [PORT]] [-    admin-host [ADMIN-HOST]] [--admin-port [ADMIN-PORT]] [--workers
    [WORKERS]] [--max-requests [MAX-REQUESTS]] [--caddyfile
    [CADDYFILE]] [--https] [--http-redirect] [--watch] [--poll] [-    log-level [LOG-LEVEL]]

```

# octane:reload
Reload the Octane workers


# octane:install
Install the Octane components and resources

# Options

`force - Overwrite any existing configuration files` OPTIONAL

`server - The server that should be used to serve the application` OPTIONAL
```
    php artisan octane:install [--server [SERVER]] [--force]

```

-----

# Options


# octane:roadrunner
Start the Octane RoadRunner server

# Options

`host - The IP address the server should bind to` OPTIONAL

`log-level - Log messages at or above the specified log level` OPTIONAL

`max-requests - The number of requests to process before reloading the server` OPTIONAL

`poll - Use file system polling while watching in order to watch files over a network` OPTIONAL

`port - The port the server should be available on` OPTIONAL

`rpc-host - The RPC IP address the server should bind to` OPTIONAL

`rpc-port - The RPC port the server should be available on` OPTIONAL

`rr-config - The path to the RoadRunner .rr.yaml file` OPTIONAL

`watch - Automatically reload the server when the application is modified` OPTIONAL

`workers - The number of workers that should be available to handle requests` OPTIONAL
```
    php artisan octane:roadrunner [--host [HOST]] [--port [PORT]] [-    rpc-host [RPC-HOST]] [--rpc-port [RPC-PORT]] [--workers
    [WORKERS]] [--max-requests [MAX-REQUESTS]] [--rr-config [RR    CONFIG]] [--watch] [--poll] [--log-level [LOG-LEVEL]]

```

`host - The IP address the server should bind to` OPTIONAL


# Options

`server - The server that is running the application` OPTIONAL
```
    php artisan octane:reload [--server [SERVER]]

```

-----

[FrankenPHP only] OPTIONAL



[FrankenPHP only] OPTIONAL
```
    https - Enable HTTPS, HTTP/2, and HTTP/3, and automatically generate and renew certificates

```
[FrankenPHP only] OPTIONAL

`log-level - Log messages at or above the specified log level` OPTIONAL

`max-requests - The number of requests to process before reloading the server` OPTIONAL

`poll - Use file system polling while watching in order to watch files over a network` OPTIONAL

`port - The port the server should be available on [default: "8000"]` OPTIONAL

`rpc-host - The RPC IP address the server should bind to` OPTIONAL

`rpc-port - The RPC port the server should be available on` OPTIONAL

`rr-config - The path to the RoadRunner .rr.yaml file` OPTIONAL

`server - The server that should be used to serve the application` OPTIONAL
```
    task-workers - The number of task workers that should be available to handle tasks

```
OPTIONAL

`watch - Automatically reload the server when the application is modified` OPTIONAL

`workers - The number of workers that should be available to handle requests` OPTIONAL
```
    php artisan octane:start [--server [SERVER]] [--host [HOST]] [-    port [PORT]] [--admin-port [ADMIN-PORT]] [--rpc-host [RPC-HOST]]
    [--rpc-port [RPC-PORT]] [--workers [WORKERS]] [--task-workers
    [TASK-WORKERS]] [--max-requests [MAX-REQUESTS]] [--rr-config [RR    CONFIG]] [--caddyfile [CADDYFILE]] [--https] [--http-redirect] [    -watch] [--poll] [--log-level [LOG-LEVEL]]

```

# octane:stop
Stop the Octane server


# octane:status
Get the current status of the Octane server

# Options

`server - The server that is running the application` OPTIONAL
```
    php artisan octane:status [--server [SERVER]]

```

-----

# Options


# octane:swoole
Start the Octane Swoole server

# Options

`host - The IP address the server should bind to` OPTIONAL

`max-requests - The number of requests to process before reloading the server` OPTIONAL

`poll - Use file system polling while watching in order to watch files over a network` OPTIONAL

`port - The port the server should be available on` OPTIONAL
```
    task-workers - The number of task workers that should be available to handle tasks

```
OPTIONAL

`watch - Automatically reload the server when the application is modified` OPTIONAL

`workers - The number of workers that should be available to handle requests` OPTIONAL
```
    php artisan octane:swoole [--host [HOST]] [--port [PORT]] [-    workers [WORKERS]] [--task-workers [TASK-WORKERS]] [--max    requests [MAX-REQUESTS]] [--watch] [--poll]

```

# Options

`server - The server that is running the application` OPTIONAL
```
    php artisan octane:stop [--server [SERVER]]

```

# package:discover


# optimize:clear
Remove the cached bootstrap files
```
    php artisan optimize:clear

```

-----

# passport:client
Create a client for issuing access tokens

# Options

`client - Create a client credentials grant client` OPTIONAL

`name - The name of the client` OPTIONAL

`password - Create a password grant client` OPTIONAL

`personal - Create a personal access token client` OPTIONAL

`provider - The name of the user provider` OPTIONAL

`public - Create a public client (Auth code grant type only)` OPTIONAL

`redirect_uri - The URI to redirect to after authorization` OPTIONAL

`user_id - The user ID the client should be assigned to` OPTIONAL
```
    php artisan passport:client [--personal] [--password] [--client]
    [--name [NAME]] [--provider [PROVIDER]] [--redirect_uri
    [REDIRECT_URI]] [--user_id [USER_ID]] [--public]

```
```
    php artisan package:discover

```

-----

# passport:install
Run the commands necessary to prepare Passport for use


# passport:install
Run the commands necessary to prepare Passport for use

# Options

`force - Overwrite keys they already exist` OPTIONAL

`length - The length of the private key` OPTIONAL

`uuids - Use UUIDs for all client IDs` OPTIONAL
```
    php artisan passport:install [--uuids] [--force] [--length
    [LENGTH]]

```

# passport:purge
Purge revoked and / or expired tokens and authentication codes

# Options

`expired - Only purge expired tokens and authentication codes` OPTIONAL

`hours - The number of hours to retain expired tokens` OPTIONAL

`revoked - Only purge revoked tokens and authentication codes` OPTIONAL
```
    php artisan passport:purge [--revoked] [--expired] [--hours
    [HOURS]]

```

-----

# pennant:purge
Delete Pennant features from storage

# Options

`except - The features that should be excluded from purging` OPTIONAL

`except-registered - Purge all features except those registered` OPTIONAL

`store - The store to purge the features from` OPTIONAL

# Arguments

`features - The features to purge` OPTIONAL
```
    php artisan pennant:purge [--except [EXCEPT]] [--except-
    registered] [--store [STORE]] [--] [<features>...]

```

# pulse:check
Take a snapshot of the current server's pulse

# Options

`once - Take a single snapshot` OPTIONAL


-----

# pulse:clear
Delete all Pulse data from storage

# Options

`force - Force the operation to run when in production` OPTIONAL

`type - Only clear the specified type(s)` OPTIONAL
```
    php artisan pulse:clear [--type [TYPE]] [--force]

```

# pulse:restart
Restart any running "work" and "check" commands
```
    php artisan pulse:restart

```

-----

# queue:clear
Delete all of the jobs from the specified queue


# queue:clear
Delete all of the jobs from the specified queue

# Options

`force - Force the operation to run when in production` OPTIONAL

`queue - The name of the queue to clear` OPTIONAL

# Arguments

`connection - The name of the queue connection to clear` OPTIONAL
```
    php artisan queue:clear [--queue [QUEUE]] [--force] [--]
    [<connection>]

```

# queue:failed
List all of the failed queue jobs
```
    php artisan queue:failed

```

-----

# Arguments


# queue:listen
Listen to a given queue

# Options
```
    backoff - The number of seconds to wait before retrying a job that encountered an uncaught

```
exception OPTIONAL

`delay - The number of seconds to delay failed jobs (Deprecated)` OPTIONAL

`force - Force the worker to run even in maintenance mode` OPTIONAL

`memory - The memory limit in megabytes` OPTIONAL

`name - The name of the worker` OPTIONAL

`queue - The queue to listen on` OPTIONAL

`rest - Number of seconds to rest between jobs` OPTIONAL

`sleep - Number of seconds to sleep when no job is available` OPTIONAL

`timeout - The number of seconds a child process can run` OPTIONAL

`tries - Number of times to attempt a job before logging it failed` OPTIONAL

# Arguments

`connection - The name of connection` OPTIONAL
```
    php artisan queue:listen [--name [NAME]] [--delay [DELAY]] [-    backoff [BACKOFF]] [--force] [--memory [MEMORY]] [--queue
    [QUEUE]] [--sleep [SLEEP]] [--rest [REST]] [--timeout [TIMEOUT]]
    [--tries [TRIES]] [--] [<connection>]

```

# Options


# Arguments

`id - The ID of the failed job` REQUIRED
```
    php artisan queue:forget <id>

```

-----

OPTIONAL


# queue:prune-batches
Prune stale entries from the batches database

# Options

`cancelled - The number of hours to retain cancelled batch data` OPTIONAL

`hours - The number of hours to retain batch data` OPTIONAL

`unfinished - The number of hours to retain unfinished batch data` OPTIONAL
```
    php artisan queue:prune-batches [--hours [HOURS]] [--unfinished
    [UNFINISHED]] [--cancelled [CANCELLED]]

```

OPTIONAL

# Arguments

`queues - The names of the queues to monitor` REQUIRED
```
    php artisan queue:monitor [--max [MAX]] [--] <queues>

```

# queue:restart
Restart queue worker daemons after their current job


# queue:prune-failed
Prune stale entries from the failed jobs table

# Options

`hours - The number of hours to retain failed jobs data` OPTIONAL
```
    php artisan queue:prune-failed [--hours [HOURS]]

```

-----

# queue:retry
Retry a failed queue job

# Options

`queue - Retry all of the failed jobs for the specified queue` OPTIONAL

`range - Range of job IDs (numeric) to be retried (e.g. 1-5)` OPTIONAL

# Arguments

`id - The ID of the failed job or "all" to retry all jobs` OPTIONAL
```
    php artisan queue:retry [--queue [QUEUE]] [--range [RANGE]] [--]
    [<id>...]

```
```
    php artisan queue:restart

```

# queue:work


# queue:retry-batch
Retry the failed jobs for a batch

# Options
```
    isolated - Do not run the command if another instance of the command is already running

```
OPTIONAL

# Arguments

`id - The ID of the batch whose failed jobs should be retried` OPTIONAL
```
    php artisan queue:retry-batch [--isolated [ISOLATED]] [--]
    [<id>...]

```

-----

# Options
```
    backoff - The number of seconds to wait before retrying a job that encountered an uncaught

```
exception OPTIONAL

`daemon - Run the worker in daemon mode (Deprecated)` OPTIONAL

`delay - The number of seconds to delay failed jobs (Deprecated)` OPTIONAL

`force - Force the worker to run even in maintenance mode` OPTIONAL

`json - Output the queue worker information as JSON` OPTIONAL

`max-jobs - The number of jobs to process before stopping` OPTIONAL

`max-time - The maximum number of seconds the worker should run` OPTIONAL

`memory - The memory limit in megabytes` OPTIONAL

`name - The name of the worker` OPTIONAL

`once - Only process the next job on the queue` OPTIONAL

`queue - The names of the queues to work` OPTIONAL

`rest - Number of seconds to rest between jobs` OPTIONAL

`sleep - Number of seconds to sleep when no job is available` OPTIONAL

`stop-when-empty - Stop when the queue is empty` OPTIONAL

`timeout - The number of seconds a child process can run` OPTIONAL

`tries - Number of times to attempt a job before logging it failed` OPTIONAL

# Arguments

`connection - The name of the queue connection to work` OPTIONAL
```
    php artisan queue:work [--name [NAME]] [--queue [QUEUE]] [--
    daemon] [--once] [--stop-when-empty] [--delay [DELAY]] [--backoff
    [BACKOFF]] [--max-jobs [MAX-JOBS]] [--max-time [MAX-TIME]] [--
    force] [--memory [MEMORY]] [--sleep [SLEEP]] [--rest [REST]] [--
    timeout [TIMEOUT]] [--tries [TRIES]] [--json] [--] [<connection>]

```

-----

# reverb:restart
Restart the Reverb server


# reverb:start
Start the Reverb server

# Options

`debug - Indicates whether debug messages should be displayed in the terminal` OPTIONAL

`host - The IP address the server should bind to` OPTIONAL

`hostname - The hostname the server is accessible from` OPTIONAL

`port - The port the server should listen on` OPTIONAL
```
    php artisan reverb:start [--host [HOST]] [--port [PORT]] [--
    hostname [HOSTNAME]] [--debug]

```

# reverb:restart
Restart the Reverb server
```
    php artisan reverb:restart

```

-----

# route:list
List all registered routes

# Options

`domain - Filter the routes by domain` OPTIONAL

`except-path - Do not display the routes matching the given path pattern` OPTIONAL

`except-vendor - Do not display routes defined by vendor packages` OPTIONAL

`json - Output the route list as JSON` OPTIONAL

`method - Filter the routes by method` OPTIONAL

`name - Filter the routes by name` OPTIONAL

`only-vendor - Only display routes defined by vendor packages` OPTIONAL

`path - Only show routes matching the given path pattern` OPTIONAL

`reverse - Reverse the ordering of the routes` OPTIONAL

`sort - The column (domain, method, uri, name, action, middleware) to sort by` OPTIONAL
```
    php artisan route:list [--json] [--method [METHOD]] [--name
    [NAME]] [--domain [DOMAIN]] [--path [PATH]] [--except-path
    [EXCEPT-PATH]] [-r|--reverse] [--sort [SORT]] [--except-vendor]
    [--only-vendor]

```

# sail:install
Install Laravel Sail's default Docker Compose file


# sail:add
Add a service to an existing Sail installation

# Arguments

`services - The services that should be added` OPTIONAL
```
    php artisan sail:add [<services>]

```

-----

# Options


# sanctum:prune-expired
Prune tokens expired for more than specified number of hours

# Options

`hours - The number of hours to retain expired Sanctum tokens` OPTIONAL
```
    php artisan sanctum:prune-expired [--hours [HOURS]]

```

# sail:publish
Publish the Laravel Sail Docker files
```
    php artisan sail:publish

```

-----

# schedule:finish
Handle the completion of a scheduled command


# schedule:list
List all scheduled tasks

# Options

`next - Sort the listed tasks by their next due date` OPTIONAL

`timezone - The timezone that times should be displayed in` OPTIONAL
```
    php artisan schedule:list [--timezone [TIMEZONE]] [--next]

```

# schedule:interrupt
Interrupt the current schedule run
```
    php artisan schedule:interrupt

```

-----

# schedule:test
Run a scheduled command

# Options

`name - The name of the scheduled command to run` OPTIONAL
```
    php artisan schedule:test [--name [NAME]]

```

# schema:dump
Dump the given database schema

# Options

`database - The database connection to use` OPTIONAL

`path - The path where the schema dump file should be stored` OPTIONAL

`prune - Delete all existing migration files` OPTIONAL


-----

# scout:delete-index
Delete an index

# Arguments

`name - The name of the index` REQUIRED
```
    php artisan scout:delete-index <name>

```

# scout:delete-all-indexes
Delete all indexes
```
    php artisan scout:delete-all-indexes

```

-----

# scout:import
Import the given model into the search index


# scout:index
Create an index

# Options

`key - The name of the primary key` OPTIONAL

# Arguments

`name - The name of the index` REQUIRED
```
    php artisan scout:index [-k|--key [KEY]] [--] <name>

```

# scout:sync-index-settings
Sync your configured index settings with your search engine (Meilisearch)
```
    php artisan scout:sync-index-settings

```

# k i t ll


# scout:import
Import the given model into the search index

# Options
```
    chunk - The number of records to import at a time (Defaults to configuration value:

```
`scout.chunk.searchable`) OPTIONAL

# Arguments

`model - Class name of model to bulk import` REQUIRED
```
    php artisan scout:import [-c|--chunk [CHUNK]] [--] <model>

```

-----

# storage:link
Create the symbolic links configured for the application

# Options

`force - Recreate existing symbolic links` OPTIONAL

`relative - Create the symbolic link using relative paths` OPTIONAL
```
    php artisan storage:link [--relative] [--force]

```

# storage:unlink
Delete existing symbolic links configured for the application
```
    php artisan storage:unlink

```

-----

# telescope:prune
Prune stale entries from the Telescope database

# Options

`hours - The number of hours to retain Telescope data` OPTIONAL

`keep-exceptions - Retain exception data` OPTIONAL
```
    php artisan telescope:prune [--hours [HOURS]] [--keep-exceptions]

```

# telescope:clear
Delete all Telescope data from storage
```
    php artisan telescope:clear

```

-----

# telescope:publish
Publish all of the Telescope resources


# ui:auth
Scaffold basic login and registration views and routes

# Options

`force - Overwrite existing views by default` OPTIONAL

`views - Only scaffold the authentication views` OPTIONAL

# Arguments

`type - The preset type (bootstrap)` OPTIONAL
```
    php artisan ui:auth [--views] [--force] [--] [<type>]

```

# telescope:resume
Unpause all Telescope watchers
```
    php artisan telescope:resume

```

-----

# vendor:publish
Publish any publishable assets from vendor packages

# Options

`all - Publish assets for all service providers without prompt` OPTIONAL

`existing - Publish and overwrite only the files that have already been published` OPTIONAL

`force - Overwrite any existing files` OPTIONAL

`provider - The service provider that has assets you want to publish` OPTIONAL

`tag - One or many tags that have assets you want to publish` OPTIONAL

```
    php artisan vendor:publish [--existing] [--force] [--all] [--
    provider [PROVIDER]] [--tag [TAG]]

```

# view:clear
Clear all compiled view files
```
php artisan view:clear
```

-----

# volt:install
Install all of the Volt resources


# volt:install
Install all of the Volt resources
```
    php artisan volt:install

```

