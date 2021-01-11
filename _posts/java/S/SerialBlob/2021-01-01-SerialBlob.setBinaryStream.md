---
title: SerialBlob.setBinaryStream()
permalink: Java/SerialBlob/setBinaryStream
date: 2021-01-11
key: JavaJava.S.SerialBlob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.metodos valor="setBinaryStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OutputStream setBinaryStream(long pos) throws SerialException, SQLException
~~~

## Parámetros
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
