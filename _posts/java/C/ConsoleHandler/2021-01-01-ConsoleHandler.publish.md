---
title: ConsoleHandler.publish()
permalink: /Java/ConsoleHandler/publish/
date: 2021-01-11
key: Java.C.ConsoleHandler
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConsoleHandler.metodos valor="publish" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void publish(LogRecord record)
~~~

## Parámetros
* **LogRecord record**,  {% include w3api/param_description.html metodo=_dato parametro="LogRecord record" %}

## Clase Padre
[ConsoleHandler](/Java/ConsoleHandler/)

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
