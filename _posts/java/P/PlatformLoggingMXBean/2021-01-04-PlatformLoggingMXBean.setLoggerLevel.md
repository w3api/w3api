---
title: PlatformLoggingMXBean.setLoggerLevel()
permalink: Java/PlatformLoggingMXBean/setLoggerLevel
date: 2021-01-04
key: JavaJava.P.PlatformLoggingMXBean
category: java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PlatformLoggingMXBean.metodos valor="setLoggerLevel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLoggerLevel(String loggerName, String levelName)
~~~

## Parámetros
* **String loggerName**,  {% include w3api/param_description.html metodo=_data parametro="String loggerName" %}
* **String levelName**,  {% include w3api/param_description.html metodo=_data parametro="String levelName" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[PlatformLoggingMXBean](/Java/PlatformLoggingMXBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PlatformLoggingMXBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
