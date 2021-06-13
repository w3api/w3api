---
title: BaseRowSet.setFetchDirection()
permalink: /Java/BaseRowSet/setFetchDirection/
date: 2021-01-11
key: Java.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setFetchDirection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFetchDirection(int direction) throws SQLException
~~~

## Parámetros
* **int direction**,  {% include w3api/param_description.html metodo=_dato parametro="int direction" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[BaseRowSet](/Java/BaseRowSet/)

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
