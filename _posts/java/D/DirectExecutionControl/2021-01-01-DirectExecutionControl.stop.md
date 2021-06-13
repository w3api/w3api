---
title: DirectExecutionControl.stop()
permalink: /Java/DirectExecutionControl/stop/
date: 2021-01-11
key: Java.D.DirectExecutionControl
category: Java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DirectExecutionControl.metodos valor="stop" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void stop() throws ExecutionControl.EngineTerminationException, ExecutionControl.InternalException
~~~

## Excepciones
[ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

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
