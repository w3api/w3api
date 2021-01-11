---
title: Attribute.remove()
permalink: Java/Attribute-javax-naming-directory/remove
date: 2021-01-11
key: JavaJava.A.Attribute-javax-naming-directory
category: java
tags: ['java se', 'javax.naming.directory', 'java.naming', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.Attribute-javax-naming-directory.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Object remove(int ix)
boolean remove(Object attrval)
~~~

## Parámetros
* **Object attrval**,  {% include w3api/param_description.html metodo=_dato parametro="Object attrval" %}
* **int ix**,  {% include w3api/param_description.html metodo=_dato parametro="int ix" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
