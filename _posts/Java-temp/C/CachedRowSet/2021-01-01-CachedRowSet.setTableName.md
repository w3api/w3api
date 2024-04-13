---
title: CachedRowSet.setTableName()
permalink: /Java/CachedRowSet/setTableName/
date: 2021-01-11
key: Java.C.CachedRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="setTableName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setTableName(String tabName) throws SQLException
~~~

## Parámetros
* **String tabName**,  {% include w3api/param_description.html metodo=_dato parametro="String tabName" %}

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
