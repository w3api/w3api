---
title: PooledConnection.getConnection()
permalink: /Java/PooledConnection/getConnection/
date: 2021-01-11
key: Java.P.PooledConnection
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PooledConnection.metodos valor="getConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Connection getConnection() throws SQLException
~~~

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[PooledConnection](/Java/PooledConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
