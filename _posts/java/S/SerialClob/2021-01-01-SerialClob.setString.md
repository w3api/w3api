---
title: SerialClob.setString()
permalink: /Java/SerialClob/setString/
date: 2021-01-11
key: Java.S.SerialClob
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialClob.metodos valor="setString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int setString(long pos, String str) throws SerialException
public int setString(long pos, String str, int offset, int length) throws SerialException
~~~

## Parámetros
* **String str**,  {% include w3api/param_description.html metodo=_dato parametro="String str" %}
* **long pos**,  {% include w3api/param_description.html metodo=_dato parametro="long pos" %}
* **int length**,  {% include w3api/param_description.html metodo=_dato parametro="int length" %}
* **int offset**,  {% include w3api/param_description.html metodo=_dato parametro="int offset" %}

## Excepciones
[SerialException](/Java/SerialException/)

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
