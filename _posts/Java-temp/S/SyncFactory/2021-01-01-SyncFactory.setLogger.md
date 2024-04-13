---
title: SyncFactory.setLogger()
permalink: /Java/SyncFactory/setLogger/
date: 2021-01-11
key: Java.S.SyncFactory
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncFactory.metodos valor="setLogger" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setLogger(Logger logger)
public static void setLogger(Logger logger, Level level)
~~~

## Parámetros
* **Level level**,  {% include w3api/param_description.html metodo=_dato parametro="Level level" %}
* **Logger logger**,  {% include w3api/param_description.html metodo=_dato parametro="Logger logger" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SyncFactory](/Java/SyncFactory/)

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
