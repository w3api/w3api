---
title: JavaShellToolBuilder.out()
permalink: Java/JavaShellToolBuilder/out
date: 2021-01-04
key: JavaJava.J.JavaShellToolBuilder
category: java
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
* **PrintStream output**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream output" %}
* **PrintStream userOut**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream userOut" %}
* **PrintStream cmdOut**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream cmdOut" %}
* **PrintStream console**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream console" %}

## Clase Padre
[JavaShellToolBuilder](/Java/JavaShellToolBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaShellToolBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
