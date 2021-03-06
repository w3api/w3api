---
title: DatabaseMetaData.supportsConvert()
permalink: /Java/DatabaseMetaData/supportsConvert/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="supportsConvert" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean supportsConvert() throws SQLException
boolean supportsConvert(int fromType, int toType) throws SQLException
~~~

## Parámetros
* **int toType**,  {% include w3api/param_description.html metodo=_dato parametro="int toType" %}
* **int fromType**,  {% include w3api/param_description.html metodo=_dato parametro="int fromType" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[DatabaseMetaData](/Java/DatabaseMetaData/)

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
