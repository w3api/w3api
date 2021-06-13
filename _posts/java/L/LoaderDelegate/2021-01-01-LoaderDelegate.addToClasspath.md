---
title: LoaderDelegate.addToClasspath()
permalink: Java/LoaderDelegate/addToClasspath
date: 2021-01-11
key: Java.L.LoaderDelegate
category: java
tags: ['java se', 'jdk.jshell.execution', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoaderDelegate.metodos valor="addToClasspath" %}

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
[LoaderDelegate](/Java/LoaderDelegate/)

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
