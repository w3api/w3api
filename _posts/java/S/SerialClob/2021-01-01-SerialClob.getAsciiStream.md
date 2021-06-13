---
title: SerialClob.getAsciiStream()
permalink: /Java/SerialClob/getAsciiStream/
date: 2021-01-11
key: Java.S.SerialClob
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialClob.metodos valor="getAsciiStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream getAsciiStream() throws SerialException, SQLException
~~~

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
