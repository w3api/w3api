---
title: DriverManager.setLogStream()
permalink: Java/DriverManager/setLogStream
date: 2021-01-11
key: JavaJava.D.DriverManager
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="setLogStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="1.2") public static void setLogStream(PrintStream out)
~~~

## Parámetros
* **PrintStream out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream out" %}

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
