---
title: SQLOutputImpl.writeURL()
permalink: /Java/SQLOutputImpl/writeURL/
date: 2021-01-11
key: Java.S.SQLOutputImpl
category: Java
tags: ['java se', 'javax.sql.rowset.serial', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SQLOutputImpl.metodos valor="writeURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void writeURL(URL url) throws SQLException
~~~

## Parámetros
* **URL url**,  {% include w3api/param_description.html metodo=_dato parametro="URL url" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[SQLOutputImpl](/Java/SQLOutputImpl/)

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
