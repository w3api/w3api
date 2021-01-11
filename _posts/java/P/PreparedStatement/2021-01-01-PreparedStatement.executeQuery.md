---
title: PreparedStatement.executeQuery()
permalink: Java/PreparedStatement/executeQuery
date: 2021-01-11
key: JavaJava.P.PreparedStatement
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="executeQuery" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResultSet executeQuery() throws SQLException
~~~

## Excepciones
[SQLException](/Java/SQLException/), [SQLTimeoutException](/Java/SQLTimeoutException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

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
