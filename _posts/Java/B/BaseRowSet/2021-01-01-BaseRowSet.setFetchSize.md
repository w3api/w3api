---
title: BaseRowSet.setFetchSize()
permalink: /Java/BaseRowSet/setFetchSize/
date: 2021-01-11
key: Java.B.BaseRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setFetchSize" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFetchSize(int rows) throws SQLException
~~~

## Parámetros
* **int rows**,  {% include w3api/param_description.html metodo=_dato parametro="int rows" %}

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
