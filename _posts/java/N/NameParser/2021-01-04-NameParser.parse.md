---
title: NameParser.parse()
permalink: Java/NameParser/parse
date: 2021-01-04
key: JavaJava.N.NameParser
category: java
tags: ['java se', 'javax.naming', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NameParser.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Name parse(String name) throws NamingException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[NamingException](/Java/NamingException/), [InvalidNameException](/Java/InvalidNameException/)

## Clase Padre
[NameParser](/Java/NameParser/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NameParser.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
