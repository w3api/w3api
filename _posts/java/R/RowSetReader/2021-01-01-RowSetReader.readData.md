---
title: RowSetReader.readData()
permalink: Java/RowSetReader/readData
date: 2021-01-11
key: Java.R.RowSetReader
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetReader.metodos valor="readData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void readData(RowSetInternal caller) throws SQLException
~~~

## Parámetros
* **RowSetInternal caller**,  {% include w3api/param_description.html metodo=_dato parametro="RowSetInternal caller" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetReader](/Java/RowSetReader/)

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
