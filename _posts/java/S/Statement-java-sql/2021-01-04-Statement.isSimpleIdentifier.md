---
title: Statement.isSimpleIdentifier()
permalink: Java/Statement-java-sql/isSimpleIdentifier
date: 2021-01-04
key: JavaJava.S.Statement-java-sql
category: java
tags: ['java se', 'java.sql', 'java.sql', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Statement-java-sql.metodos valor="isSimpleIdentifier" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean isSimpleIdentifier(String identifier) throws SQLException
~~~

## Parámetros
* **String identifier**,  {% include w3api/param_description.html metodo=_data parametro="String identifier" %}

## Excepciones
[SQLException](/Java/SQLException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Statement](/Java/Statement-java-sql/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.Statement-java-sql.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
