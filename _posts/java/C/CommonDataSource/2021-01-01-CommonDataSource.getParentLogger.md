---
title: CommonDataSource.getParentLogger()
permalink: /Java/CommonDataSource/getParentLogger/
date: 2021-01-11
key: Java.C.CommonDataSource
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommonDataSource.metodos valor="getParentLogger" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Logger getParentLogger() throws SQLFeatureNotSupportedException
~~~

## Excepciones
[SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[CommonDataSource](/Java/CommonDataSource/)

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
