---
title: DriverManager.deregisterDriver()
permalink: /Java/DriverManager/deregisterDriver/
date: 2021-01-11
key: Java.D.DriverManager
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="deregisterDriver" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void deregisterDriver(Driver driver) throws SQLException
~~~

## Parámetros
* **Driver driver**,  {% include w3api/param_description.html metodo=_dato parametro="Driver driver" %}

## Excepciones
[SQLException](/Java/SQLException/), [SecurityException](/Java/SecurityException/)

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
