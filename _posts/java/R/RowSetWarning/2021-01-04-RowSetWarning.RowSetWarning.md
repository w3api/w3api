---
title: RowSetWarning.RowSetWarning()
permalink: Java/RowSetWarning/RowSetWarning
date: 2021-01-04
key: JavaJava.R.RowSetWarning
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
* **int vendorCode**,  {% include w3api/param_description.html metodo=_data parametro="int vendorCode" %}
* **String SQLState**,  {% include w3api/param_description.html metodo=_data parametro="String SQLState" %}
* **String reason**,  {% include w3api/param_description.html metodo=_data parametro="String reason" %}

## Clase Padre
[RowSetWarning](/Java/RowSetWarning/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RowSetWarning.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
