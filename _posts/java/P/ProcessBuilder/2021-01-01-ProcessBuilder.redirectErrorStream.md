---
title: ProcessBuilder.redirectErrorStream()
permalink: /Java/ProcessBuilder/redirectErrorStream/
date: 2021-01-11
key: Java.P.ProcessBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.metodos valor="redirectErrorStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean redirectErrorStream()
public ProcessBuilder redirectErrorStream(boolean redirectErrorStream)
~~~

## Parámetros
* **boolean redirectErrorStream**,  {% include w3api/param_description.html metodo=_dato parametro="boolean redirectErrorStream" %}

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
