---
title: LogManager.readConfiguration()
permalink: /Java/LogManager/readConfiguration/
date: 2021-01-11
key: Java.L.LogManager
category: Java
tags: ['java se', 'java.util.logging', 'java.logging', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LogManager.metodos valor="readConfiguration" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void readConfiguration() throws IOException, SecurityException
public void readConfiguration(InputStream ins) throws IOException, SecurityException
~~~

## Parámetros
* **InputStream ins**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream ins" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IOException](/Java/IOException/)

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
