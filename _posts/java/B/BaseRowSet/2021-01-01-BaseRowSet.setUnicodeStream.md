---
title: BaseRowSet.setUnicodeStream()
permalink: /Java/BaseRowSet/setUnicodeStream/
date: 2021-01-11
key: Java.B.BaseRowSet
category: Java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BaseRowSet.metodos valor="setUnicodeStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public void setUnicodeStream(int parameterIndex, InputStream x, int length) throws SQLException
~~~

## Parámetros
* **InputStream x**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream x" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int parameterIndex**,  {% include w3api/param_description.html metodo=_dato parametro="int parameterIndex" %}

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
