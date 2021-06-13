---
title: SerialBlob.getBytes()
permalink: /Java/SerialBlob/getBytes/
date: 2021-01-11
key: Java.S.SerialBlob
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.metodos valor="getBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public byte[] getBytes(long pos, int length) throws SerialException
~~~

## Parámetros
* **long pos**,  {% include w3api/param_description.html metodo=_dato parametro="long pos" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}

## Excepciones
[SerialException](/Java/SerialException/)

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
