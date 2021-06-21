---
title: ProcessBuilder.command()
permalink: /Java/ProcessBuilder/command/
date: 2021-01-11
key: Java.P.ProcessBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.metodos valor="command" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<String> command()
public ProcessBuilder command(String... command)
public ProcessBuilder command(List<String> command)
~~~

## Parámetros
* **List&lt;String&gt; command**,  {% include w3api/param_description.html metodo=_dato parametro="List<String> command" %}
* **String... command**,  {% include w3api/param_description.html metodo=_dato parametro="String... command" %}

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
