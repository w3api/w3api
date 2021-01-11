---
title: DriverManager.getConnection()
permalink: Java/DriverManager/getConnection
date: 2021-01-11
key: JavaJava.D.DriverManager
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DriverManager.metodos valor="getConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Connection getConnection(String url) throws SQLException
public static Connection getConnection(String url, String user, String password) throws SQLException
public static Connection getConnection(String url, Properties info) throws SQLException
~~~

## Parámetros
* **Properties info**,  {% include w3api/param_description.html metodo=_dato parametro="Properties info" %}
* **String url**,  {% include w3api/param_description.html metodo=_dato parametro="String url" %}
* **String user**,  {% include w3api/param_description.html metodo=_dato parametro="String user" %}
* **String password**,  {% include w3api/param_description.html metodo=_dato parametro="String password" %}

## Excepciones
[SQLException](/Java/SQLException/), [SQLTimeoutException](/Java/SQLTimeoutException/)

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
