---
title: JavaShellToolBuilder.start()
permalink: /Java/JavaShellToolBuilder/start/
date: 2021-01-11
key: Java.J.JavaShellToolBuilder
category: Java
tags: ['java se', 'jdk.jshell.tool', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaShellToolBuilder.metodos valor="start" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default int start(String... arguments) throws Exception
~~~

## Parámetros
* **String... arguments**,  {% include w3api/param_description.html metodo=_dato parametro="String... arguments" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[JavaShellToolBuilder](/Java/JavaShellToolBuilder/)

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
