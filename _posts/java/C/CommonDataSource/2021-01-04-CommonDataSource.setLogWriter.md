---
title: CommonDataSource.setLogWriter()
permalink: Java/CommonDataSource/setLogWriter
date: 2021-01-04
key: JavaJava.C.CommonDataSource
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CommonDataSource.metodos valor="setLogWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setLogWriter(PrintWriter out) throws SQLException
~~~

## Parámetros
* **PrintWriter out**,  {% include w3api/param_description.html metodo=_data parametro="PrintWriter out" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[CommonDataSource](/Java/CommonDataSource/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CommonDataSource.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
