---
title: RowSetMetaDataImpl.setScale()
permalink: Java/RowSetMetaDataImpl/setScale
date: 2021-01-11
key: JavaJava.R.RowSetMetaDataImpl
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaDataImpl.metodos valor="setScale" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setScale(int columnIndex, int scale) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **int scale**,  {% include w3api/param_description.html metodo=_dato parametro="int scale" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetMetaDataImpl](/Java/RowSetMetaDataImpl/)

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