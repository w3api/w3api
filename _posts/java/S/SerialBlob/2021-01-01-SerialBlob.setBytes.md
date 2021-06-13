---
title: SerialBlob.setBytes()
permalink: /Java/SerialBlob/setBytes/
date: 2021-01-11
key: Java.S.SerialBlob
category: Java
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
* **long pos**,  {% include w3api/param_description.html metodo=_dato parametro="long pos" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **byte[] bytes**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] bytes" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

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
