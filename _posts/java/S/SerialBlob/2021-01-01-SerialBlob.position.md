---
title: SerialBlob.position()
permalink: /Java/SerialBlob/position/
date: 2021-01-11
key: Java.S.SerialBlob
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.metodos valor="position" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long position(byte[] pattern, long start) throws SerialException, SQLException
public long position(Blob pattern, long start) throws SerialException, SQLException
~~~

## Parámetros
* **Blob pattern**,  {% include w3api/param_description.html metodo=_dato parametro="Blob pattern" %}
* **byte[] pattern**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] pattern" %}
* **long start**,  {% include w3api/param_description.html metodo=_dato parametro="long start" %}

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
