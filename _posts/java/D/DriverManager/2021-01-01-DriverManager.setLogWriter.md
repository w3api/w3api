---
title: DriverManager.setLogWriter()
permalink: /Java/DriverManager/setLogWriter/
date: 2021-01-11
key: Java.D.DriverManager
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="setLogWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setLogWriter(PrintWriter out)
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}

## Excepciones
[SecurityException](/Java/SecurityException/)

## Clase Padre
[DriverManager](/Java/DriverManager/)

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
