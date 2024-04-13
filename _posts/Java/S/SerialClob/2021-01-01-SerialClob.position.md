---
title: SerialClob.position()
permalink: /Java/SerialClob/position/
date: 2021-01-11
key: Java.S.SerialClob
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialClob.metodos valor="position" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long position(String searchStr, long start) throws SerialException, SQLException
public long position(Clob searchStr, long start) throws SerialException, SQLException
~~~

## Parámetros
* **String searchStr**,  {% include w3api/param_description.html metodo=_dato parametro="String searchStr" %}
* **Clob searchStr**,  {% include w3api/param_description.html metodo=_dato parametro="Clob searchStr" %}
* **long start**,  {% include w3api/param_description.html metodo=_dato parametro="long start" %}

## Excepciones
[SQLException](/Java/SQLException/), [SerialException](/Java/SerialException/)

## Clase Padre
[SerialClob](/Java/SerialClob/)

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
