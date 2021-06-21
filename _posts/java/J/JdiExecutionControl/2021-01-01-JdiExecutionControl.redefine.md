---
title: JdiExecutionControl.redefine()
permalink: /Java/JdiExecutionControl/redefine/
date: 2021-01-11
key: Java.J.JdiExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JdiExecutionControl.metodos valor="redefine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void redefine(ExecutionControl.ClassBytecodes[] cbcs) throws ExecutionControl.ClassInstallException, ExecutionControl.EngineTerminationException
~~~

## Parámetros
* **ExecutionControl.ClassBytecodes[] cbcs**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutionControl.ClassBytecodes[] cbcs" %}

## Excepciones
[ExecutionControl.ClassInstallException](/Java/ExecutionControl.ClassInstallException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

## Clase Padre
[JdiExecutionControl](/Java/JdiExecutionControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
