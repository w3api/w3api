---
title: DirectExecutionControl.classesRedefined()
permalink: Java/DirectExecutionControl/classesRedefined
date: 2021-01-04
key: JavaJava.D.DirectExecutionControl
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectExecutionControl.metodos valor="classesRedefined" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void classesRedefined(ExecutionControl.ClassBytecodes[] cbcs) throws ExecutionControl.NotImplementedException, ExecutionControl.EngineTerminationException
~~~

## Parámetros
* **ExecutionControl.ClassBytecodes[] cbcs**,  {% include w3api/param_description.html metodo=_data parametro="ExecutionControl.ClassBytecodes[] cbcs" %}

## Excepciones
[ExecutionControl.NotImplementedException](/Java/ExecutionControl.NotImplementedException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

## Clase Padre
[DirectExecutionControl](/Java/DirectExecutionControl/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DirectExecutionControl.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
