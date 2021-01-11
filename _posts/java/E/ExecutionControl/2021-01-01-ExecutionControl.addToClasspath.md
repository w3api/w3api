---
title: ExecutionControl.addToClasspath()
permalink: Java/ExecutionControl/addToClasspath
date: 2021-01-11
key: JavaJava.E.ExecutionControl
category: java
tags: ['java se', 'jdk.jshell.spi', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.ExecutionControl.metodos valor="addToClasspath" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addToClasspath(String path) throws ExecutionControl.EngineTerminationException, ExecutionControl.InternalException
~~~

## Parámetros
* **String path**,  {% include w3api/param_description.html metodo=_dato parametro="String path" %}

## Excepciones
[ExecutionControl.InternalException](/Java/ExecutionControl.InternalException/), [ExecutionControl.EngineTerminationException](/Java/ExecutionControl.EngineTerminationException/)

## Clase Padre
[ExecutionControl](/Java/ExecutionControl/)

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
