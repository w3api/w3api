---
title: subprocess
permalink: /Python/subprocess
date: 2021-01-01
key: Python.S.subprocess
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.S.subprocess.description }}

## Funciones
* [call](/Python/subprocess/call/)
* [check_call](/Python/subprocess/check_call/)
* [check_output](/Python/subprocess/check_output/)
* [getoutput](/Python/subprocess/getoutput/)
* [getstatusoutput](/Python/subprocess/getstatusoutput/)
* [run](/Python/subprocess/run/)

## Clases
* [CompletedProcess](/Python/subprocess/CompletedProcess/)
* [Popen](/Python/subprocess/Popen/)
* [STARTUPINFO](/Python/subprocess/STARTUPINFO/)

## Excepciones
* [CalledProcessError](/Python/subprocess/CalledProcessError/)
* [SubprocessError](/Python/subprocess/SubprocessError/)
* [TimeoutExpired](/Python/subprocess/TimeoutExpired/)

## Constantes
* [ABOVE_NORMAL_PRIORITY_CLASS](/Python/subprocess/ABOVE_NORMAL_PRIORITY_CLASS/)
* [BELOW_NORMAL_PRIORITY_CLASS](/Python/subprocess/BELOW_NORMAL_PRIORITY_CLASS/)
* [CREATE_BREAKAWAY_FROM_JOB](/Python/subprocess/CREATE_BREAKAWAY_FROM_JOB/)
* [CREATE_DEFAULT_ERROR_MODE](/Python/subprocess/CREATE_DEFAULT_ERROR_MODE/)
* [CREATE_NEW_CONSOLE](/Python/subprocess/CREATE_NEW_CONSOLE/)
* [CREATE_NEW_PROCESS_GROUP](/Python/subprocess/CREATE_NEW_PROCESS_GROUP/)
* [CREATE_NO_WINDOW](/Python/subprocess/CREATE_NO_WINDOW/)
* [DETACHED_PROCESS](/Python/subprocess/DETACHED_PROCESS/)
* [DEVNULL](/Python/subprocess/DEVNULL/)
* [HIGH_PRIORITY_CLASS](/Python/subprocess/HIGH_PRIORITY_CLASS/)
* [IDLE_PRIORITY_CLASS](/Python/subprocess/IDLE_PRIORITY_CLASS/)
* [NORMAL_PRIORITY_CLASS](/Python/subprocess/NORMAL_PRIORITY_CLASS/)
* [PIPE](/Python/subprocess/PIPE/)
* [REALTIME_PRIORITY_CLASS](/Python/subprocess/REALTIME_PRIORITY_CLASS/)
* [STARTF_USESHOWWINDOW](/Python/subprocess/STARTF_USESHOWWINDOW/)
* [STARTF_USESTDHANDLES](/Python/subprocess/STARTF_USESTDHANDLES/)
* [STDOUT](/Python/subprocess/STDOUT/)
* [STD_ERROR_HANDLE](/Python/subprocess/STD_ERROR_HANDLE/)
* [STD_INPUT_HANDLE](/Python/subprocess/STD_INPUT_HANDLE/)
* [STD_OUTPUT_HANDLE](/Python/subprocess/STD_OUTPUT_HANDLE/)
* [SW_HIDE](/Python/subprocess/SW_HIDE/)

## Ejemplo
~~~python
{{ site.data.Python.S.subprocess.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.subprocess.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
