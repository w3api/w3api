---
title: DirectExecutionControl.throwConvertedOtherException()
permalink: Java/DirectExecutionControl/throwConvertedOtherException
date: 2021-01-11
key: JavaJava.D.DirectExecutionControl
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectExecutionControl.metodos valor="throwConvertedOtherException" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected String throwConvertedOtherException(Throwable ex) throws ExecutionControl.RunException, ExecutionControl.InternalException
~~~

## Parámetros
* **Throwable ex**,  {% include w3api/param_description.html metodo=_dato parametro="Throwable ex" %}

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
