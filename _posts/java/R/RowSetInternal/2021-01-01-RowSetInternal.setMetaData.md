---
title: RowSetInternal.setMetaData()
permalink: /Java/RowSetInternal/setMetaData/
date: 2021-01-11
key: Java.R.RowSetInternal
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetInternal.metodos valor="setMetaData" %}

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
[RowSetInternal](/Java/RowSetInternal/)

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
