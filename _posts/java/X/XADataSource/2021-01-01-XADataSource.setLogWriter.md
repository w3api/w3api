---
title: XADataSource.setLogWriter()
permalink: /Java/XADataSource/setLogWriter/
date: 2021-01-11
key: Java.X.XADataSource
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.X.XADataSource.metodos valor="setLogWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLogWriter(PrintWriter out) throws SQLException
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_dato parametro="PrintWriter out" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[XADataSource](/Java/XADataSource/)

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
