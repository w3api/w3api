---
title: SerialClob.position()
permalink: Java/SerialClob/position
date: 2021-01-04
key: JavaJava.S.SerialClob
category: java
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
* **long start**,  {% include w3api/param_description.html metodo=_data parametro="long start" %}
* **Clob searchStr**,  {% include w3api/param_description.html metodo=_data parametro="Clob searchStr" %}
* **String searchStr**,  {% include w3api/param_description.html metodo=_data parametro="String searchStr" %}

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
{%- for _ldc in site.data.Java.S.SerialClob.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
