---
title: SerialClob.setAsciiStream()
permalink: Java/SerialClob/setAsciiStream
date: 2021-01-04
key: JavaJava.S.SerialClob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialClob.metodos valor="setAsciiStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OutputStream setAsciiStream(long pos) throws SerialException, SQLException
~~~

## Parámetros
* **long pos**,  {% include w3api/param_description.html metodo=_data parametro="long pos" %}

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
