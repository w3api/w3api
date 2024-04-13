---
title: JavaFileManager.handleOption()
permalink: /Java/JavaFileManager/handleOption/
date: 2021-01-11
key: Java.J.JavaFileManager
category: Java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileManager.metodos valor="handleOption" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean handleOption(String current, Iterator<String> remaining)
~~~

## Parámetros
* **String current**,  {% include w3api/param_description.html metodo=_dato parametro="String current" %}
* **Iterator&lt;String&gt; remaining**,  {% include w3api/param_description.html metodo=_dato parametro="Iterator<String> remaining" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[JavaFileManager](/Java/JavaFileManager/)

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
