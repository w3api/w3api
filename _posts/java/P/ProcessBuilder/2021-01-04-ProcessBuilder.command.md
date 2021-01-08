---
title: ProcessBuilder.command()
permalink: Java/ProcessBuilder/command
date: 2021-01-04
key: JavaJava.P.ProcessBuilder
category: java
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
* **String... command**,  {% include w3api/param_description.html metodo=_data parametro="String... command" %}
* **List&lt;String&gt; command**,  {% include w3api/param_description.html metodo=_data parametro="List<String> command" %}

## Clase Padre
[ProcessBuilder](/Java/ProcessBuilder/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.ProcessBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
