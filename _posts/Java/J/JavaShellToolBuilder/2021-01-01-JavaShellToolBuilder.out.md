---
title: JavaShellToolBuilder.out()
permalink: /Java/JavaShellToolBuilder/out/
date: 2021-01-11
key: Java.J.JavaShellToolBuilder
category: Java
tags: ['java se', 'jdk.jshell.tool', 'jdk.jshell', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaShellToolBuilder.metodos valor="out" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
JavaShellToolBuilder out(PrintStream output)
JavaShellToolBuilder out(PrintStream cmdOut, PrintStream console, PrintStream userOut)
~~~

## Parámetros
* **PrintStream cmdOut**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream cmdOut" %}
* **PrintStream userOut**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream userOut" %}
* **PrintStream output**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream output" %}
* **PrintStream console**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream console" %}

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
