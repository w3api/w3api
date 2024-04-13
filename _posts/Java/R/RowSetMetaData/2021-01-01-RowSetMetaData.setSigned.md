---
title: RowSetMetaData.setSigned()
permalink: /Java/RowSetMetaData/setSigned/
date: 2021-01-11
key: Java.R.RowSetMetaData
category: Java
tags: ['java se', 'javax.sql', 'java.sql', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetMetaData.metodos valor="setSigned" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSigned(int columnIndex, boolean property) throws SQLException
~~~

## Parámetros
* **int columnIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int columnIndex" %}
* **boolean property**,  {% include w3api/param_description.html metodo=_dato parametro="boolean property" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[RowSetMetaData](/Java/RowSetMetaData/)

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
