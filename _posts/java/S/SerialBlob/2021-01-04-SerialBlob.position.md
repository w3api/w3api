---
title: SerialBlob.position()
permalink: Java/SerialBlob/position
date: 2021-01-04
key: JavaJava.S.SerialBlob
category: java
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
* **byte[] pattern**,  {% include w3api/param_description.html metodo=_data parametro="byte[] pattern" %}
* **Blob pattern**,  {% include w3api/param_description.html metodo=_data parametro="Blob pattern" %}
* **long start**,  {% include w3api/param_description.html metodo=_data parametro="long start" %}

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
