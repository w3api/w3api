---
title: Statement.setEscapeProcessing()
permalink: /Java/Statement-java-sql/setEscapeProcessing/
date: 2021-01-11
key: Java.S.Statement-java-sql
category: Java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="setEscapeProcessing" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setEscapeProcessing(boolean enable) throws SQLException
~~~

## Parámetros
* **boolean enable**,  {% include w3api/param_description.html metodo=_dato parametro="boolean enable" %}

## Excepciones
[SQLException](/Java/SQLException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

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
