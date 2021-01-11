---
title: LogManager.addLogger()
permalink: Java/LogManager/addLogger
date: 2021-01-11
key: JavaJava.L.LogManager
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogManager.metodos valor="addLogger" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addLogger(Logger logger)
~~~

## Parámetros
* **Logger logger**,  {% include w3api/param_description.html metodo=_dato parametro="Logger logger" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LogManager](/Java/LogManager/)

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
