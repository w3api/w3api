---
title: ProcessBuilder.ProcessBuilder()
permalink: /Java/ProcessBuilder/ProcessBuilder/
date: 2021-01-11
key: Java.P.ProcessBuilder
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.constructores valor="ProcessBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProcessBuilder(String... command)
public ProcessBuilder(List<String> command)
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

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
