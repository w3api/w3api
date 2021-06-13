---
title: XAConnection.getXAResource()
permalink: /Java/XAConnection/getXAResource/
date: 2021-01-11
key: Java.X.XAConnection
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XAConnection.metodos valor="getXAResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
XAResource getXAResource() throws SQLException
~~~

## Excepciones
[SQLException](/Java/SQLException/), [SQLFeatureNotSupportedException](/Java/SQLFeatureNotSupportedException/)

## Clase Padre
[XAConnection](/Java/XAConnection/)

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
