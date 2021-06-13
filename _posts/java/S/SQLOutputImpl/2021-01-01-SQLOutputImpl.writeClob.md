---
title: SQLOutputImpl.writeClob()
permalink: /Java/SQLOutputImpl/writeClob/
date: 2021-01-11
key: Java.S.SQLOutputImpl
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutputImpl.metodos valor="writeClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeClob(Clob x) throws SQLException
~~~

## Parámetros
* **Clob x**,  {% include w3api/param_description.html metodo=_dato parametro="Clob x" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[SQLOutputImpl](/Java/SQLOutputImpl/)

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
