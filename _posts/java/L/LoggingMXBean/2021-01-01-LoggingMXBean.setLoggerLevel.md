---
title: LoggingMXBean.setLoggerLevel()
permalink: Java/LoggingMXBean/setLoggerLevel
date: 2021-01-11
key: JavaJava.L.LoggingMXBean
category: java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LoggingMXBean.metodos valor="setLoggerLevel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLoggerLevel(String loggerName, String levelName)
~~~

## Parámetros
* **String levelName**,  {% include w3api/param_description.html metodo=_dato parametro="String levelName" %}
* **String loggerName**,  {% include w3api/param_description.html metodo=_dato parametro="String loggerName" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LoggingMXBean](/Java/LoggingMXBean/)

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
