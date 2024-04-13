---
title: CachedRowSet.setMetaData()
permalink: /Java/CachedRowSet/setMetaData/
date: 2021-01-11
key: Java.C.CachedRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="setMetaData" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setMetaData(RowSetMetaData md) throws SQLException
~~~

## Parámetros
* **RowSetMetaData md**,  {% include w3api/param_description.html metodo=_dato parametro="RowSetMetaData md" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[CachedRowSet](/Java/CachedRowSet/)

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
