---
title: JdiExecutionControl.vm()
permalink: /Java/JdiExecutionControl/vm/
date: 2021-01-11
key: Java.J.JdiExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JdiExecutionControl.metodos valor="vm" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract VirtualMachine vm() throws ExecutionControl.EngineTerminationException
~~~

## Excepciones
[ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

## Clase Padre
[JdiExecutionControl](/Java/JdiExecutionControl/)

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
