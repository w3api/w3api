---
title: JavaShellToolBuilder.err()
permalink: /Java/JavaShellToolBuilder/err/
date: 2021-01-11
key: Java.J.JavaShellToolBuilder
category: Java
tags: ['java se', 'jdk.jshell.tool', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaShellToolBuilder.metodos valor="err" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaShellToolBuilder err(PrintStream error)
JavaShellToolBuilder err(PrintStream cmdErr, PrintStream userErr)
~~~

## Parámetros
* **PrintStream userErr**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream userErr" %}
* **PrintStream error**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream error" %}
* **PrintStream cmdErr**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream cmdErr" %}

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
