---
title: RowSetWriter.writeData()
permalink: /Java/RowSetWriter/writeData/
date: 2021-01-11
key: Java.R.RowSetWriter
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetWriter.metodos valor="writeData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean writeData(RowSetInternal caller) throws SQLException
~~~

## Parámetros
* **RowSetInternal caller**,  {% include w3api/param_description.html metodo=_dato parametro="RowSetInternal caller" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetWriter](/Java/RowSetWriter/)

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
