---
title: PreparedStatement.executeUpdate()
permalink: /Java/PreparedStatement/executeUpdate/
date: 2021-01-11
key: Java.P.PreparedStatement
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PreparedStatement.metodos valor="executeUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
int executeUpdate() throws SQLException
~~~

## Excepciones
[SQLException](/Java/SQLException/), [SQLTimeoutException](/Java/SQLTimeoutException/)

## Clase Padre
[PreparedStatement](/Java/PreparedStatement/)

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
