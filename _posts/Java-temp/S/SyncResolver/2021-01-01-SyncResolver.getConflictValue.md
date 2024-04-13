---
title: SyncResolver.getConflictValue()
permalink: /Java/SyncResolver/getConflictValue/
date: 2021-01-11
key: Java.S.SyncResolver
category: Java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncResolver.metodos valor="getConflictValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object getConflictValue(int index) throws SQLException
Object getConflictValue(String columnName) throws SQLException
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **String columnName**,  {% include w3api/param_description.html metodo=_dato parametro="String columnName" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[SyncResolver](/Java/SyncResolver/)

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
