---
title: SerialClob.SerialClob()
permalink: Java/SerialClob/SerialClob
date: 2021-01-11
key: JavaJava.S.SerialClob
category: java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SerialClob.constructores valor="SerialClob" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SerialClob(char[] ch) throws SerialException, SQLException
public SerialClob(Clob clob) throws SerialException, SQLException
~~~

## Parámetros
* **Clob clob**,  {% include w3api/param_description.html metodo=_dato parametro="Clob clob" %}
* **char[] ch**,  {% include w3api/param_description.html metodo=_dato parametro="char[] ch" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
