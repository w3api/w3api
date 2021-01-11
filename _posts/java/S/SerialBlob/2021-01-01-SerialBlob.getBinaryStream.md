---
title: SerialBlob.getBinaryStream()
permalink: Java/SerialBlob/getBinaryStream
date: 2021-01-11
key: JavaJava.S.SerialBlob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.metodos valor="getBinaryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStream getBinaryStream() throws SerialException
public InputStream getBinaryStream(long pos, long length) throws SQLException
~~~

## Parámetros
* **long length**,  {% include w3api/param_description.html metodo=_dato parametro="long length" %}
* **long pos**,  {% include w3api/param_description.html metodo=_dato parametro="long pos" %}

## Excepciones
[SQLException](/Java/SQLException/), [SerialException](/Java/SerialException/)

## Clase Padre
[SerialBlob](/Java/SerialBlob/)

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
