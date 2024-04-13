---
title: CachedRowSet.populate()
permalink: /Java/CachedRowSet/populate/
date: 2021-01-11
key: Java.C.CachedRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="populate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void populate(ResultSet data) throws SQLException
void populate(ResultSet rs, int startRow) throws SQLException
~~~

## Parámetros
* **int startRow**,  {% include w3api/param_description.html metodo=_dato parametro="int startRow" %}
* **ResultSet rs**,  {% include w3api/param_description.html metodo=_dato parametro="ResultSet rs" %}
* **ResultSet data**,  {% include w3api/param_description.html metodo=_dato parametro="ResultSet data" %}

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
