---
title: RowSetProvider.newFactory()
permalink: /Java/RowSetProvider/newFactory/
date: 2021-01-11
key: Java.R.RowSetProvider
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetProvider.metodos valor="newFactory" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static RowSetFactory newFactory() throws SQLException
public static RowSetFactory newFactory(String factoryClassName, ClassLoader cl) throws SQLException
~~~

## Parámetros
* **String factoryClassName**,  {% include w3api/param_description.html metodo=_dato parametro="String factoryClassName" %}
* **ClassLoader cl**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader cl" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetProvider](/Java/RowSetProvider/)

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
