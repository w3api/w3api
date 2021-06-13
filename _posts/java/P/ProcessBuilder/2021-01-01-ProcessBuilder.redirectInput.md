---
title: ProcessBuilder.redirectInput()
permalink: /Java/ProcessBuilder/redirectInput/
date: 2021-01-11
key: Java.P.ProcessBuilder
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.ProcessBuilder.metodos valor="redirectInput" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ProcessBuilder.Redirect redirectInput()
public ProcessBuilder redirectInput(File file)
public ProcessBuilder redirectInput(ProcessBuilder.Redirect source)
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **ProcessBuilder.Redirect source**,  {% include w3api/param_description.html metodo=_dato parametro="ProcessBuilder.Redirect source" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

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
