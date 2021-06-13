---
title: BaseRowSet.setConcurrency()
permalink: /Java/BaseRowSet/setConcurrency/
date: 2021-01-11
key: Java.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setConcurrency" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setConcurrency(int concurrency) throws SQLException
~~~

## Parámetros
* **int concurrency**,  {% include w3api/param_description.html metodo=_dato parametro="int concurrency" %}

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
