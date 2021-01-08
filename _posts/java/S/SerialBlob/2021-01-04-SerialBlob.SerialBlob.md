---
title: SerialBlob.SerialBlob()
permalink: Java/SerialBlob/SerialBlob
date: 2021-01-04
key: JavaJava.S.SerialBlob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialBlob.constructores valor="SerialBlob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerialBlob(byte[] b) throws SerialException, SQLException
public SerialBlob(Blob blob) throws SerialException, SQLException
~~~

## Parámetros
* **byte[] b**,  {% include w3api/param_description.html metodo=_data parametro="byte[] b" %}
* **Blob blob**,  {% include w3api/param_description.html metodo=_data parametro="Blob blob" %}

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
