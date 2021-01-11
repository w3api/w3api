---
title: RemoteExecutionControl.redefine()
permalink: Java/RemoteExecutionControl/redefine
date: 2021-01-11
key: JavaJava.R.RemoteExecutionControl
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RemoteExecutionControl.metodos valor="redefine" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void redefine(ExecutionControl.ClassBytecodes[] cbcs) throws ExecutionControl.ClassInstallException, ExecutionControl.NotImplementedException, ExecutionControl.EngineTerminationException
~~~

## Parámetros
* **ExecutionControl.ClassBytecodes[] cbcs**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutionControl.ClassBytecodes[] cbcs" %}

## Excepciones
[ExecutionControl.ClassInstallException](/Java/ExecutionControl.ClassInstallException/), [ExecutionControl.NotImplementedException](/Java/ExecutionControl.NotImplementedException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

## Clase Padre
[RemoteExecutionControl](/Java/RemoteExecutionControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
