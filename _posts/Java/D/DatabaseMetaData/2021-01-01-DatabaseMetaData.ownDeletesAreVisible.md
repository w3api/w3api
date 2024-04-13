---
title: DatabaseMetaData.ownDeletesAreVisible()
permalink: /Java/DatabaseMetaData/ownDeletesAreVisible/
date: 2021-01-11
key: Java.D.DatabaseMetaData
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DatabaseMetaData.metodos valor="ownDeletesAreVisible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean ownDeletesAreVisible(int type) throws SQLException
~~~

## Parámetros
* **int type**,  {% include w3api/param_description.html metodo=_dato parametro="int type" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[DatabaseMetaData](/Java/DatabaseMetaData/)

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
