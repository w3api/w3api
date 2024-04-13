---
title: NameParser.parse()
permalink: /Java/NameParser/parse/
date: 2021-01-11
key: Java.N.NameParser
category: Java
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
* **String name**,  {% include w3api/param_description.html metodo=_dato parametro="String name" %}

## Excepciones
[InvalidNameException](/Java/InvalidNameException/), [NamingException](/Java/NamingException/)

## Clase Padre
[NameParser](/Java/NameParser/)

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
