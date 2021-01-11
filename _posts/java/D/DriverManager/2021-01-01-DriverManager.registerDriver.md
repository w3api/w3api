---
title: DriverManager.registerDriver()
permalink: Java/DriverManager/registerDriver
date: 2021-01-11
key: JavaJava.D.DriverManager
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="registerDriver" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void registerDriver(Driver driver) throws SQLException
public static void registerDriver(Driver driver, DriverAction da) throws SQLException
~~~

## Parámetros
* **Driver driver**,  {% include w3api/param_description.html metodo=_dato parametro="Driver driver" %}
* **DriverAction da**,  {% include w3api/param_description.html metodo=_dato parametro="DriverAction da" %}

## Excepciones
[SQLException](/Java/SQLException/), [NullPointerException](/Java/NullPointerException/)

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
