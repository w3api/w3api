---
title: CachedRowSet.populate()
permalink: Java/CachedRowSet/populate
date: 2021-01-04
key: JavaJava.C.CachedRowSet
category: java
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
* **ResultSet rs**,  {% include w3api/param_description.html metodo=_data parametro="ResultSet rs" %}
* **ResultSet data**,  {% include w3api/param_description.html metodo=_data parametro="ResultSet data" %}
* **int startRow**,  {% include w3api/param_description.html metodo=_data parametro="int startRow" %}

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
{%- for _ldc in site.data.Java.C.CachedRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
