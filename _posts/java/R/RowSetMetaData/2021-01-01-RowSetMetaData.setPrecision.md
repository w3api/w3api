---
title: RowSetMetaData.setPrecision()
permalink: Java/RowSetMetaData/setPrecision
date: 2021-01-11
key: Java.R.RowSetMetaData
category: java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaData.metodos valor="setPrecision" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setPrecision(int columnIndex, int precision) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int precision**,  {% include w3api/param_description.html metodo=_dato parametro="int precision" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetMetaData](/Java/RowSetMetaData/)

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
