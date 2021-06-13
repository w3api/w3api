---
title: RowSetWarning.RowSetWarning()
permalink: Java/RowSetWarning/RowSetWarning
date: 2021-01-11
key: Java.R.RowSetWarning
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RowSetWarning.constructores valor="RowSetWarning" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public RowSetWarning()
public RowSetWarning(String reason)
public RowSetWarning(String reason, String SQLState)
public RowSetWarning(String reason, String SQLState, int vendorCode)
~~~

## Parámetros
* **String reason**,  {% include w3api/param_description.html metodo=_dato parametro="String reason" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_dato parametro="String SQLState" %}
* **int vendorCode**,  {% include w3api/param_description.html metodo=_dato parametro="int vendorCode" %}

## Clase Padre
[RowSetWarning](/Java/RowSetWarning/)

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
