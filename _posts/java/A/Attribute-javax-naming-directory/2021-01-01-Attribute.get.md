---
title: Attribute.get()
permalink: Java/Attribute-javax-naming-directory/get
date: 2021-01-11
key: JavaJava.A.Attribute-javax-naming-directory
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attribute-javax-naming-directory.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object get() throws NamingException
Object get(int ix) throws NamingException
~~~

## Parámetros
* **int ix**,  {% include w3api/param_description.html metodo=_dato parametro="int ix" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NamingException](/Java/NamingException/)

## Clase Padre
[Attribute](/Java/Attribute-javax-naming-directory/)

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
