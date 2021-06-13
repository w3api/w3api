---
title: DirectExecutionControl.throwConvertedInvocationException()
permalink: /Java/DirectExecutionControl/throwConvertedInvocationException/
date: 2021-01-11
key: Java.D.DirectExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectExecutionControl.metodos valor="throwConvertedInvocationException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String throwConvertedInvocationException(Throwable cause) throws ExecutionControl.RunException, ExecutionControl.InternalException
~~~

## Parámetros
* **Throwable cause**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable cause" %}

## Excepciones
[ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/), [ExecutionControl.RunException](/Java/ExecutionControl.RunException/)

## Clase Padre
[DirectExecutionControl](/Java/DirectExecutionControl/)

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
