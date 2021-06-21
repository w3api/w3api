---
title: ProcessBuilder.redirectError()
permalink: /Java/ProcessBuilder/redirectError/
date: 2021-01-11
key: Java.P.ProcessBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.metodos valor="redirectError" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProcessBuilder.Redirect redirectError()
public ProcessBuilder redirectError(File file)
public ProcessBuilder redirectError(ProcessBuilder.Redirect destination)
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **ProcessBuilder.Redirect destination**,  {% include w3api/param_description.html metodo=_dato parametro="ProcessBuilder.Redirect destination" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[ProcessBuilder](/Java/ProcessBuilder/)

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
