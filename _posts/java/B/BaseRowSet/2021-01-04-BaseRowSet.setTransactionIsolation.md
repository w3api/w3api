---
title: BaseRowSet.setTransactionIsolation()
permalink: Java/BaseRowSet/setTransactionIsolation
date: 2021-01-04
key: JavaJava.B.BaseRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setTransactionIsolation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setTransactionIsolation(int level) throws SQLException
~~~

## Parámetros
* **int level**,  {% include w3api/param_description.html metodo=_data parametro="int level" %}

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
{%- for _ldc in site.data.Java.B.BaseRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
