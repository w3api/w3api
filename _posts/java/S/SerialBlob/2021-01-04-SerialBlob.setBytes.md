---
title: SerialBlob.setBytes()
permalink: Java/SerialBlob/setBytes
date: 2021-01-04
key: JavaJava.S.SerialBlob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.metodos valor="setBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int setBytes(long pos, byte[] bytes) throws SerialException, SQLException
public int setBytes(long pos, byte[] bytes, int offset, int length) throws SerialException, SQLException
~~~

## Parámetros
* **byte[] bytes**,  {% include w3api/param_description.html metodo=_data parametro="byte[] bytes" %}
* **long pos**,  {% include w3api/param_description.html metodo=_data parametro="long pos" %}
* **int length**,  {% include w3api/param_description.html metodo=_data parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_data parametro="int offset" %}

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
{%- for _ldc in site.data.Java.S.SerialBlob.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
