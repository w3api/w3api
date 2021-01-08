---
title: CompositeName.addAll()
permalink: Java/CompositeName/addAll
date: 2021-01-04
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
* **int posn**,  {% include w3api/param_description.html metodo=_data parametro="int posn" %}
* **Name suffix**,  {% include w3api/param_description.html metodo=_data parametro="Name suffix" %}
* **Name n**,  {% include w3api/param_description.html metodo=_data parametro="Name n" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [InvalidNameException](/Java/InvalidNameException/)

## Clase Padre
[CompositeName](/Java/CompositeName/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeName.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
