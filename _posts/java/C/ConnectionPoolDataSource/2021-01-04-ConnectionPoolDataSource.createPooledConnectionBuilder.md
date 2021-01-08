---
title: ConnectionPoolDataSource.createPooledConnectionBuilder()
permalink: Java/ConnectionPoolDataSource/createPooledConnectionBuilder
date: 2021-01-04
key: JavaJava.C.ConnectionPoolDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConnectionPoolDataSource.metodos valor="createPooledConnectionBuilder" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default PooledConnectionBuilder createPooledConnectionBuilder() throws SQLException
~~~

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[ConnectionPoolDataSource](/Java/ConnectionPoolDataSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConnectionPoolDataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
