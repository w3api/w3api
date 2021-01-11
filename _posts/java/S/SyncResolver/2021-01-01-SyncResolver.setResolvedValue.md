---
title: SyncResolver.setResolvedValue()
permalink: Java/SyncResolver/setResolvedValue
date: 2021-01-11
key: JavaJava.S.SyncResolver
category: java
tags: ['java se', 'javax.sql.rowset.spi', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SyncResolver.metodos valor="setResolvedValue" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setResolvedValue(int index, Object obj) throws SQLException
void setResolvedValue(String columnName, Object obj) throws SQLException
~~~

## Parámetros
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
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
