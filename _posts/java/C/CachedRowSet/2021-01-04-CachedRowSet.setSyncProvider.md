---
title: CachedRowSet.setSyncProvider()
permalink: Java/CachedRowSet/setSyncProvider
date: 2021-01-04
key: JavaJava.C.CachedRowSet
category: java
tags: ['java se', 'javax.sql.rowset', 'java.sql.rowset', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CachedRowSet.metodos valor="setSyncProvider" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setSyncProvider(String provider) throws SQLException
~~~

## Parámetros
* **String provider**,  {% include w3api/param_description.html metodo=_data parametro="String provider" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[CachedRowSet](/Java/CachedRowSet/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CachedRowSet.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
