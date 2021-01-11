---
title: CompositeName.addAll()
permalink: Java/CompositeName/addAll
date: 2021-01-11
key: JavaJava.C.CompositeName
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeName.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Name addAll(int posn, Name n) throws InvalidNameException
public Name addAll(Name suffix) throws InvalidNameException
~~~

## Parámetros
* **Name suffix**,  {% include w3api/param_description.html metodo=_dato parametro="Name suffix" %}
* **Name n**,  {% include w3api/param_description.html metodo=_dato parametro="Name n" %}
* **int posn**,  {% include w3api/param_description.html metodo=_dato parametro="int posn" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/), [ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/)

## Clase Padre
[CompositeName](/Java/CompositeName/)

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
