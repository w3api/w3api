---
title: DriverManager.getDriver()
permalink: Java/DriverManager/getDriver
date: 2021-01-11
key: JavaJava.D.DriverManager
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="getDriver" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Driver getDriver(String url) throws SQLException
~~~

## Parámetros
* **String url**,  {% include w3api/param_description.html metodo=_dato parametro="String url" %}

## Excepciones
[SQLException](/Java/SQLException/)

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
